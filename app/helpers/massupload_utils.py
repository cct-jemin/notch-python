from fastapi import HTTPException
from app.config import massupload_config,v2ScopeCategoryConfig,v2ReportFieldsConfig
import logging
import pandas as pd
from app.schemas import massupload_validation_schema
import re
import asyncio
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime,timedelta
from openpyxl import load_workbook
from typing import Dict, List, Any
from collections import Counter
import copy


labelIgnore = ['category','custom']
sectionVal = {
    "section_1": "Company Information",
    "section_2": "Employee Commuting",
    "section_3": "Business Travel",
    "section_4": "Energy",
    "section_5": "Fuels",
    "section_6": "Detailed Carbon",
}
monthYearHeader = []
executor = ThreadPoolExecutor()

async def sheetWiseValidation(requestParam):
    filePath = requestParam['filePath']
    workbook = load_workbook(filePath, read_only=True)
    sheetNamesAarry = workbook.sheetnames
    sheetWiseData = {'sheets' : {}, 'validationStr' : ''}
    start_time = datetime.now()
    print(f"Start Time: {start_time.isoformat()}")
    tasks = []
    for sheetName in sheetNamesAarry:
        
        if sheetName.lower() not in massupload_validation_schema.massUploadValidationSchema["sheetMapping"] :
            continue     
    
        sheet = workbook[sheetName]
        sheetData = [[cell.value if cell.value is not None else '' for cell in row] for row in sheet.iter_rows()]
        # print(sheetData,"---")
        # tasks.append(validate_sheet(requestParam,sheetName, sheetData,sheetWiseData))
        sync_validate(requestParam,sheetName, sheetData,sheetWiseData)
        
    # Execute all tasks concurrently
    await asyncio.gather(*tasks)
    end_time = datetime.now()
    duration = (end_time - start_time).total_seconds()
    print(f"End Time: {end_time.isoformat()}")
    print(f"Duration: {duration:.2f} seconds")
        
    validation_obj = []
    if not sheetWiseData.get("sheets", {}):  # Check if the "sheets" dictionary is empty
        validation_obj.append({
            "sheetName": "No Sheets",
            "validation": ["Please upload valid sheet"]
        })
        
    for sheet_name, sheet_data in sheetWiseData.get("sheets", {}).items():
        validation_str = sheet_data.get("validationStr", "").strip()
        if validation_str:
            # Extract content between <li> and </li> tags
            matches = re.findall(r"<li>(.*?)<\/li>", validation_str)
            # Remove any extra whitespace and filter out empty values
            html_array = [match.strip() for match in matches if match.strip()]
            validation_obj.append({"sheetName": sheet_name, "validation": html_array})
            
    if validation_obj :
        return {"isAllSheetValid":False,"validationObj": validation_obj}
    else :
        if requestParam['isBenchmark']:
            print(requestParam['monthYearHeader'],"aaaaaaaaaa")
        else :
            print(requestParam['monthYearHeader'],"-------------------")
        return {"isAllSheetValid":True,"validationObj": validation_obj}


async def validate_sheet(requestParam,sheetName, sheetData,sheetWiseData):
    await asyncio.to_thread(sync_validate,requestParam,sheetName,sheetData,sheetWiseData)
   
    
    
def sync_validate(requestParam,sheetName, sheetData, sheetWiseData):
    # start_time = time.time()
    # print(f"Start processing sheet: {sheetName} at {start_time:.2f}")
    sectionWiseSheetData = {}
    maxAllowedColumnNumber = 25
    headerStartIndexColumnNumber = 13
    headerPeriodArr = []
    requestParam.update({
        'maxAllowedColumnNumber': maxAllowedColumnNumber,
        'headerStartIndexColumnNumber': headerStartIndexColumnNumber,
        'sheetName': sheetName,
        'headerPeriodArr':headerPeriodArr
    })
    sheetInfo = massupload_validation_schema.massUploadValidationSchema["sheetMapping"][sheetName.lower()]
    sectionNameMapping = massupload_validation_schema.massUploadValidationSchema['sectionNameMapping']
    sectionNameMappingReverse = reverseObject(sectionNameMapping)
   #for now take data from config file
    scope = str(sheetInfo['scope'])
    category = sheetInfo['category']
    requestParam.update({'scope': scope, 'category': category})
    sheetWiseData['sheets'][sheetName] = {"scope" : scope, "category" : category, "data" : [], "sectionPointer" : '', "validationStr" : ''}
    section_pointer_name = None
    section_pointer = ''
    valid_section_name_array = [
        sectionNameMappingReverse[sectionPointer]
        for sectionPointer in sheetInfo['sectionPointer']
        if sectionPointer in sectionNameMappingReverse
    ]
    headerRow = []
    for i, row in enumerate(sheetData):
        # validation of row 1 column 1.
        if i == 0:
            first_cell_value = lower_case(row[0])
            if not category and first_cell_value != "company information":
                sheetWiseData['sheets'][sheetName]['validationStr'] += (
                    f"<li>Row - 1 : Invalid names. It should be Company Information.</li>"
                )
                break    
            elif not category and first_cell_value == "company information":
                section_pointer_name = first_cell_value
            elif category and first_cell_value == "category":
                section_pointer_name = lower_case(sheetData[1][0]) if len(sheetData) > 1 else None
            else:
                sheetWiseData['sheets'][sheetName]['validationStr'] += (
                    f"<li>Row - 1 : Invalid {row[0]}. It should be Category.</li>"
                )
                break  
            
        # Filter out rows where all cells are null
        if all(cell is None or cell == '' for cell in row):
            continue

        # Trim strings in the row
        row = [cell.strip() if isinstance(cell, str) else cell for cell in row]
        
        # Slice columns to only include the maximum allowed number
        row = row[:maxAllowedColumnNumber]
        sheetData[i] = row
        
        # section validation
        if row[0] and row[0].lower() in valid_section_name_array:
            section_pointer_name = row[0].lower()
            section_pointer = sectionNameMapping[section_pointer_name]
            sheetWiseData['sheets'][sheetName]['sectionPointer'] = section_pointer
            # requestParam['sectionPointer'] = sectionNameMapping[section_pointer_name]
            requestParam['sectionPointer'] = section_pointer

        elif row[0] and section_pointer_name != 'company information' and row[0].lower() not in labelIgnore:
            sheetWiseData['sheets'][sheetName]['validationStr'] += (
                f"<li>Row - {i+1} : Invalid Section name. It should be one of these {', '.join(valid_section_name_array)}.</li>"
            )
            break
        
        # Category validation
        if section_pointer_name != 'company information':
            attributeCategoryFields = v2ScopeCategoryConfig.scopeConfig[scope][category]
            attributeSubCategoryFields = get_attribute_subcategories(v2ScopeCategoryConfig.scopeConfig)
            requestParam['attributeCategoryFields'] = attributeCategoryFields
            # print(lower_case(sheetData[i][0]),"aaa")
            # print(section_pointer_name,"section_pointer_name")
            if row[0] and row[0].strip().lower() == "category":
                # Check if the attributeCategoryFields label matches the category in sheet_data
                if attributeCategoryFields and attributeCategoryFields['label'].strip().lower() != sheetData[0][1].strip().lower():
                    sheetWiseData['sheets'][sheetName]['validationStr'] += f"<li>Row - {i + 1} : Invalid Category name {sheetData[0][1]}. It should be {attributeCategoryFields['label']}.</li>"
                    break
            elif  lower_case(sheetData[i][0]) == 'custom' or lower_case(sheetData[i][2]) == 'custom' :
                if attributeSubCategoryFields and sheetData[i][1] in attributeSubCategoryFields :
                    sheetWiseData['sheets'][sheetName]['validationStr'] =  f"<li>Row - {i + 1} : Custom project sub-category name should not be same as standard sub-category {sheetData[i][1]}.</li>"
                    break
                else :
                    sheetWiseData['sheets'][sheetName]['validationStr'] += sheetWiseSectionPropertiesValidation(requestParam, section_pointer, sheetData, i)
                    sheetWiseData['sheets'][sheetName]['validationStr'] += sheetWiseValueValidation(requestParam, sheetData, i, headerRow)
                
            elif  lower_case(sheetData[i][0]) == section_pointer_name :
                headers = massupload_validation_schema.massUploadValidationSchema['headerMapping'][section_pointer]
                if headers:
                    headerRow = sheetData[i]
                    sheetWiseData['sheets'][sheetName]['validationStr'] += sheetWiseHeaderValidation(requestParam,section_pointer, headers, sheetData, i)
                    sheetWiseData['sheets'][sheetName]['validationStr'] += sheetWiseHeaderPeriodValidation(requestParam, section_pointer, sheetData, i)
               
            else :
                #Property and value validation
                sheetWiseData['sheets'][sheetName]['validationStr'] += sheetWiseSectionPropertiesValidation(requestParam, section_pointer, sheetData, i)
                sheetWiseData['sheets'][sheetName]['validationStr'] += sheetWiseValueValidation(requestParam, sheetData, i,headerRow)
        
        elif  lower_case(sheetData[i][0]) == section_pointer_name :
                headers = massupload_validation_schema.massUploadValidationSchema['headerMapping'][section_pointer]
                if headers:
                    headerRow = sheetData[i]
                    #Header validation
                    sheetWiseData['sheets'][sheetName]['validationStr'] += sheetWiseHeaderValidation(requestParam,section_pointer, headers, sheetData, i)
                    sheetWiseData['sheets'][sheetName]['validationStr'] += sheetWiseHeaderPeriodValidation(requestParam, section_pointer, sheetData, i)
        else :
            #Property and value validation
            sheetWiseData['sheets'][sheetName]['validationStr'] += sheetWiseSectionPropertiesValidation(requestParam, section_pointer, sheetData, i)
            sheetWiseData['sheets'][sheetName]['validationStr'] += sheetWiseValueValidation(requestParam, sheetData, i,headerRow)
            
        if section_pointer not in sectionWiseSheetData:
            sectionWiseSheetData[section_pointer] = []

        sectionWiseSheetData[section_pointer].append(sheetData[i])
            
    sheetWiseData['sheets'][sheetName]['data'] = sectionWiseSheetData;   
    if not requestParam['isBenchmark']:
        if len(requestParam['monthYearHeader']) == 12:
            monthYearDates = sorted(
                datetime.strptime(value + '-01', '%b-%Y-%d') for value in requestParam['monthYearHeader']
            )
            yearMonth = '202101'
            benchmarkDate = datetime.strptime(yearMonth[:4] + '-' + yearMonth[4:] + '-01', '%Y-%m-%d')
            if benchmarkDate > monthYearDates[0]:
                sheetWiseData['sheets'][sheetName]['validationStr'] += f"<li>Data should be greater or equal to your site benchmark period.</li>"
            elif benchmarkDate < monthYearDates[0]:
                previousMonth = (monthYearDates[0] - timedelta(days=1)).strftime('%b-%Y')
                checkExists = True
                if not checkExists:
                    sheetWiseData['sheets'][sheetName]['validationStr'] +=  f'<li>Please insert {previousMonth} month-year data first.</li>'
     
    # if  requestParam['isBenchmark']:
    #     print(requestParam['headerPeriodArr'],"1111111111")  
                
                
                

    # sheetWiseData['sheets'][sheetName]['data'] = sheetData
    # print(f"Finished processing sheet: {sheetName} at {time.time():.2f}, duration: {time.time() - start_time:.2f} seconds")
    
def sheetWiseHeaderValidation(request_param,section_pointer, headers, sheetData, i):
    validation_str = ""
    actual_header = []
    
    # Validate column length
    if len(sheetData[i]) != request_param['maxAllowedColumnNumber']:
        validation_str += (
            f"<li>Row - {i + 1}: Section ({sectionVal[section_pointer]}) Header Not valid </li>"
        )

    # Slice header based on section
    if section_pointer == "section_1":
        actual_header = sheetData[i][:2]
    elif section_pointer in {"section_2", "section_3", "section_4", "section_5"}:
        actual_header = sheetData[i][:9]
    elif section_pointer == "section_6":
        actual_header = sheetData[i][:7]
    

    # Normalize header to lowercase and remove None values
    actual_header = [
        str(name).lower() for name in actual_header if name is not None
    ]
    
    # Find the difference between valid and actual headers
    diff_header = list(set(headers) - set(actual_header))
    if diff_header:
        diff_header = [header.capitalize() for header in diff_header]
        validation_str += (
            f"<li>Row - {i + 1}: Section ({sectionVal[section_pointer]}) ["
            + ", ".join(diff_header)
            + "] Header Not found </li>"
        )

    return validation_str

def sheetWiseHeaderPeriodValidation(requestParam, sectionPointer, sheetData, rowIndex):
    validationStr = ''
    periodHeaderArr = []

    def convertAndValidateHeader(header):
        if header == '':
            return None
        try:
            if isinstance(header, (int, float)):
                headerDate = excelDateToFormatedDate(header).strftime("%b-%Y").lower()
            elif isinstance(header, str):
                headerDate = header.strip().lower()
                if not validateDate(headerDate):
                    raise ValueError(f"{header}: Header Not Valid. Follow this format: (Jan-2019)")
            else:
                raise ValueError("Header cannot be None")
            return headerDate
        except ValueError as e:
            nonlocal validationStr
            validationStr += f"<li>Row - {rowIndex + 1}: {str(e)}</li>"
            return None

    # Validate and process header periods
    for header in sheetData[rowIndex][requestParam['headerStartIndexColumnNumber']:]:
        headerPeriod = convertAndValidateHeader(header)
        if headerPeriod:  # Only add if the header is valid
            periodHeaderArr.append(headerPeriod)
            
    if len(periodHeaderArr) < 12:
        validationStr += f"<li>Row - {rowIndex + 1}: Must have at least 12 months and year headers.</li>"
        

    # Validate sorted and current date constraints
    sortedDates = sorted(
        [datetime.strptime(h, "%b-%Y") for h in periodHeaderArr if h],
        reverse=False
    )
    if sortedDates and sortedDates[-1] > datetime.now():
        validationStr += f"<li>Row - {rowIndex + 1}: Month and year headers must be prior to the current month/year.</li>"

    # Check for duplicate headers
    if periodHeaderArr:
        monthYearHeader = [re.sub(r'^b-', '', h) for h in periodHeaderArr if h]
        duplicates = [item for item, count in Counter(periodHeaderArr).items() if count > 1]
        if duplicates:
            validationStr += f"<li>Row - {rowIndex + 1}: Duplicate headers found ({', '.join(duplicates)}).</li>"
            
        # print(periodHeaderArr,"periodHeaderArr")
        monthYearDates = sorted(
            datetime.strptime(value + '-01', '%b-%Y-%d') for value in periodHeaderArr
        )
    
        yearMonth = '202101'
        benchmarkDate = datetime.strptime(yearMonth[:4] + '-' + yearMonth[4:] + '-01', '%Y-%m-%d')
            
        # if benchmarkDate > monthYearDates[0]:
        #     validationStr += f"<li>Row - {rowIndex + 1}: Benchmark Period should be greater or equal to your site benchmark period.</li>"

        if benchmarkDate == monthYearDates[0]:
            requestParam['isBenchmark'] = True 
            requestParam['headerPeriodArr'] =  list(set(requestParam['headerPeriodArr'] + monthYearHeader))
            if not requestParam.get('monthYearHeader'):
                requestParam['monthYearHeader'] = {}
                
            if sectionPointer not in requestParam['monthYearHeader']:
                requestParam['monthYearHeader'][sectionPointer] = []
                
            requestParam['monthYearHeader'][sectionPointer] = periodHeaderArr
            
        else :
            requestParam['isBenchmark'] = False 
             # Match headers with global monthYearHeader
            if not requestParam.get('monthYearHeader'):
                requestParam['monthYearHeader'] =  [re.sub(r'^b-', '', h) for h in periodHeaderArr if h]
                requestParam['baseHeader'] = sectionPointer
            else:
                # currentHeaders = [h.replace("b-", "") for h in periodHeaderArr if h]
                currentHeaders = [re.sub(r'^b-', '', h) for h in periodHeaderArr if h]
                if not set(requestParam['monthYearHeader']) == set(currentHeaders):
                    validationStr += (
                        f"<li>Row - {rowIndex + 1}: Month-year headers should match with "
                        f"{requestParam['baseHeader']} month-year headers.</li>"
                    )
   

    return validationStr

def sheetWiseValueValidation(requestParam, sheetData, rowIndex,headerRow):
    validationStr = ''
    isValidate = True
    for index in range(requestParam['headerStartIndexColumnNumber'], len(sheetData[rowIndex])):
        columnName = headerRow[index]
        if isinstance(headerRow[index], (int, float)):
            columnName = excelDateToFormatedDate(headerRow[index]).strftime("%b-%Y")

        cellValue = sheetData[rowIndex][index]
        if isValidate:
            if cellValue == '':
                validationStr += f"<li>Row - {rowIndex + 1} : Value required in {columnName} column.</li>"
            # Check if the value is less than 0
            elif isinstance(cellValue, (int, float)) and cellValue < 0:
                validationStr += f"<li>Row - {rowIndex + 1} : Value must be 0 or higher in {columnName} column.</li>"
            

        # Check if the value is not numeric
        if cellValue != '' and not isinstance(cellValue, (int, float)):
            validationStr += f"<li>Row - {rowIndex + 1} : Value must be numeric in {columnName} column.</li>"

    return validationStr

def sheetWiseSectionPropertiesValidation(requestParam, sectionPointer, sheetData, rowIndex):
    validationStr = ''
    if sectionPointer == 'section_1':
        companyInfoField = sheetData[rowIndex][0]
        companyInfoCustomField = sheetData[rowIndex][1]
        sectionFields = v2ReportFieldsConfig.fieldsConfig['companyInfoFields']
        
        sectionLabel = ['custom 1', 'custom 2', 'custom 3'] + [
            field['label'].strip().lower() for field in sectionFields.values()
        ]
        # Convert the companyInfoField to lowercase for case-insensitive comparisons
        if companyInfoField is not None:
            companyInfoFieldStr = companyInfoField.strip().lower()

            # Validate if companyInfoField matches any valid label
            if companyInfoFieldStr not in sectionLabel:
                validationStr += (
                    f"<li>Row - {rowIndex + 1}: ({sectionVal[sectionPointer]}) "
                    f"{companyInfoField.strip()} value not match with {', '.join(sectionLabel)}.</li>"
                )

            # Custom field-specific validations
            if companyInfoFieldStr.startswith('custom'):
                if not companyInfoCustomField:
                    validationStr += (
                        f"<li>Row - {rowIndex + 1}: ({sectionVal[sectionPointer]}) "
                        f"custom type must be required for {companyInfoField}.</li>"
                    )
            elif companyInfoCustomField:
                validationStr += (
                    f"<li>Row - {rowIndex + 1}: ({sectionVal[sectionPointer]}) "
                    f"custom type should be blank for {companyInfoField}.</li>"
                )
    elif sectionPointer == 'section_2' or sectionPointer == 'section_3' :
        SheetDataObj = {
            "attributeSubCategory": sheetData[rowIndex][1] if sheetData[rowIndex][1] else "blank",
            "type": sheetData[rowIndex][2],
            "subType": sheetData[rowIndex][3],
            "unit": sheetData[rowIndex][4] if sheetData[rowIndex][4] else "blank",
        }
        validationStr +=  validateFields(requestParam , SheetDataObj, sheetData, rowIndex)
        params = [
            {
            'fieldName' : 'Cost/Unit',
            'required' : True,
            'type' : 'number',
            'sheetData' : sheetData[rowIndex][5]
            },
            {
            'fieldName' : 'Driver Name',
            'required' : False,
            'type' : 'string',
            'sheetData' : sheetData[rowIndex][6]
            },
            {
            'fieldName' : 'Registration',
            'required' : False,
            'type' : 'string',
            'sheetData' : sheetData[rowIndex][7]
            },
        ]
        validationStr +=  fieldTypeValidation(params,rowIndex)
    elif sectionPointer == 'section_4' :
        energyFields = ["green electricity", "electricity", "gas" ,"steam"]
        SheetDataObj = {
            'attributeSubCategory' : sheetData[rowIndex][1] if sheetData[rowIndex][1] else "blank",
            'type' : sheetData[rowIndex][2],
            'subType' : sheetData[rowIndex][3],
            'unit' : sheetData[rowIndex][4] if sheetData[rowIndex][4] else "blank",
            'workplace' : sheetData[rowIndex][6] if sheetData[rowIndex][6] else "blank",
            'meterName' : sheetData[rowIndex][7],
            'meterNumber' : sheetData[rowIndex][8]
        }
        if SheetDataObj['attributeSubCategory'].strip().lower() not in energyFields:
            validationStr += (
                f"<li>Row - {rowIndex + 1}: Invalid Sub-Category ({SheetDataObj['attributeSubCategory']}) "
                f"It should be one of these {energyFields}.</li>"
            )
        else :
            validationStr +=  validateFields(requestParam , SheetDataObj, sheetData, rowIndex)
            params = [
                {
                'fieldName' : 'Cost/Unit',
                'required' : True,
                'type' : 'number',
                'sheetData' : sheetData[rowIndex][5]
                },
                {
                'fieldName' : 'Meter Name',
                'required' : False,
                'type' : 'string',
                'sheetData' : sheetData[rowIndex][7]
                },
                {
                'fieldName' : 'Meter Number',
                'required' : False,
                'type' : 'string',
                'sheetData' : sheetData[rowIndex][8]
                },
            ]
            validationStr +=  fieldTypeValidation(params, rowIndex)
    elif sectionPointer == 'section_5' :
        SheetDataObj = {
            'attributeSubCategory' : sheetData[rowIndex][1] if sheetData[rowIndex][1] else "blank",
            'type' : sheetData[rowIndex][2] if sheetData[rowIndex][1] else "blank",
            'subType' : sheetData[rowIndex][3],
            'unit' : sheetData[rowIndex][4] if sheetData[rowIndex][4] else "blank",
            'workplace' : sheetData[rowIndex][6] if sheetData[rowIndex][6] else "blank",
            'customName' : sheetData[rowIndex][7],
            'carbonFactor' : sheetData[rowIndex][8],
        }
        fuelsFields  = ['fuels', 'fugitive emissions']
        if SheetDataObj['attributeSubCategory'].strip().lower() not in fuelsFields:
            validationStr += (
                f"<li>Row - {rowIndex + 1}: Invalid Sub-Category ({SheetDataObj['attributeSubCategory']}) "
                f"It should be one of these {fuelsFields}.</li>"
            )
        else : 
            validationStr +=  validateFields(requestParam , SheetDataObj, sheetData, rowIndex)
            params = [
                {
                    'fieldName' : 'Cost/Unit',
                    'required' : True,
                    'type' : 'number',
                    'sheetData' : sheetData[rowIndex][5]
                }
            ]
            validationStr +=  fieldTypeValidation(params, rowIndex)
    elif sectionPointer == 'section_6' :
        SheetDataObj = {
            'attributeType': sheetData[rowIndex][0],
            'attributeSubCategory' : sheetData[rowIndex][1],
            'type' : sheetData[rowIndex][2],
            'subType' : sheetData[rowIndex][3] ,
            'unit' : sheetData[rowIndex][4],
        }
        if isinstance(SheetDataObj['type'], str) and SheetDataObj['type'].strip().lower() == 'custom' or SheetDataObj['attributeType'].strip().lower() == 'custom' :
            isTypeRequired = True
            if SheetDataObj['attributeType'].strip().lower() == 'custom' and (not SheetDataObj.get('subType') or SheetDataObj['subType'] is None):
                isTypeRequired = False
                
            params = [
                {
                'fieldName' : 'Sub - Category',
                'required' : True,
                'type' : 'string',
                'sheetData' : SheetDataObj['attributeSubCategory']
                },
                {
                'fieldName' : 'Type',
                'required' : isTypeRequired,
                'type' : 'string',
                'sheetData' : SheetDataObj['type']
                },
                {
                'fieldName' : 'sub-type',
                'required' : False,
                'type' : 'string',
                'sheetData' : SheetDataObj['subType']
                },
                {
                'fieldName' : 'Unit',
                'required' : True,
                'type' : 'string',
                'sheetData' : SheetDataObj['unit']
                },
                {
                'fieldName' : 'Co2 Unit/Kg',
                'required' : True,
                'type' : 'number',
                'sheetData' : sheetData[rowIndex][6]
                }
            ]
            validationStr +=  fieldTypeValidation(params,rowIndex)
        else :
            validationStr +=  validateFields(requestParam , SheetDataObj, sheetData, rowIndex)
            params = [
                {
                    'fieldName' : 'Co2 Unit/Kg',
                    'required' : '',
                    'type' : 'number',
                    'sheetData' : sheetData[rowIndex][6]
                },
            ]
            validationStr +=  fieldTypeValidation(params, rowIndex)
        params = [
            {
            'fieldName' : 'Cost/Unit',
            'required' : True,
            'type' : 'number',
            'sheetData' : sheetData[rowIndex][5]
            }
        ]
        validationStr +=  fieldTypeValidation(params, rowIndex)

    return validationStr


def validateFields(request_param, sheet_data_obj, sheet_data, row_index):
    section_fields = request_param["attributeCategoryFields"].get("attributeSubCategory", {})
    validation_str = ''
    attribute_sub_category_valid = False
    is_type_valid = False
    is_sub_type_valid = False
    attribute_sub_category_labels = []
    custom_project_found = False
    category = request_param["category"]
    scopeValue = request_param.get("scope")

    # Attribute sub-category validation
    if section_fields != "userdefine":
        # workplace validation
        if request_param["sectionPointer"] in ["section_4", "section_5"]:
            workplaceSheet = sheet_data_obj['workplace'].strip().lower()
            if workplaceSheet not in ['home', 'office']:
                validation_str += (
                    f"<li>Row - {row_index + 1}: Invalid workplace {sheet_data_obj['workplace']}. "
                    f"It should be home or office.</li>"
                )
            elif scopeValue == "1" and workplaceSheet != "office":
                validation_str += (
                    f"<li>Row - {row_index + 1}: Invalid workplace {sheet_data_obj['workplace']}. "
                    f"It should be office.</li>"
                )
            elif scopeValue == "2" and sheet_data_obj["attributeSubCategory"].strip().lower() in ["fuels", "fugitive emissions"] and workplaceSheet != "home":
                validation_str += (
                    f"<li>Row - {row_index + 1}: Invalid workplace {sheet_data_obj['workplace']}. "
                    f"It should be home.</li>"
                )
            elif scopeValue == "3" and workplaceSheet != "home":
                validation_str += (
                    f"<li>Row - {row_index + 1}: Invalid workplace {sheet_data_obj['workplace']}. "
                    f"It should be home22.</li>"
                )

            # Validation for meter name, meter number, and sub-type for home workplace
            if request_param["sectionPointer"] == "section_4" and workplaceSheet == "home":
                if sheet_data_obj.get("meterName"):
                    validation_str += (
                        f"<li>Row - {row_index + 1}: Meter Name should be blank for home.</li>"
                    )
                if sheet_data_obj.get("meterNumber"):
                    validation_str += (
                        f"<li>Row - {row_index + 1}: Meter Number should be blank for home.</li>"
                    )
                if sheet_data_obj.get("subType"):
                    validation_str += (
                        f"<li>Row - {row_index + 1}: Sub-type should be blank for home.</li>"
                    )
            
        for key, section_field in section_fields.items():
            if key == "custom":
                custom_project_found = True
            
            fieldData = copy.deepcopy(section_field)
            attribute_sub_category_field = section_field.get("sheetLabel") or section_field.get("label")
            attribute_sub_category_labels.append(attribute_sub_category_field)
            if attribute_sub_category_field.strip().lower() == sheet_data_obj["attributeSubCategory"].strip().lower():
                attribute_sub_category_valid = True
                type_labels = []

                # Handling 'plane' specific logic
                if key == "plane":
                    attributeSubCategoryPlane = copy.deepcopy(fieldData['type'])
                    fieldData["type"] = {
                        "domestic": attributeSubCategoryPlane["plane"]["options"]["domestic"],
                        "shortHaul": attributeSubCategoryPlane["plane"]["options"]["shortHaul"],
                        "longHaul": attributeSubCategoryPlane["plane"]["options"]["longHaul"],
                        "international": attributeSubCategoryPlane["plane"]["options"]["international"],
                    }
                    if request_param["sectionPointer"] == "section_5":
                        fieldData["type"].update({
                            "economy": attributeSubCategoryPlane["plane"]["options"]["economy"],
                            "business": attributeSubCategoryPlane["plane"]["options"]["business"]
                        })
                    fieldData["unit"] = attributeSubCategoryPlane["plane"]["unit"]
                    
                    
                for type_key, type_field in fieldData["type"].items():
                    typeFields = copy.deepcopy(type_field)
                    # print(typeFields,"11111111111111111111111111111111111")
                    type_label = typeFields.get("sheetLabel") or typeFields.get("label")
                    type_labels.append(type_label)
                    options = typeFields.get("options", {})
                    if type_label.strip().lower() == sheet_data_obj["type"].strip().lower():
                        is_type_valid = True
                        units = [unit.strip().lower() for unit in typeFields.get("unit", [])]
                        if typeFields.get("unit", []) and len(options) == 0 and sheet_data_obj["unit"].strip().lower() not in units:
                            validation_str += (
                                f"<li>Row - {row_index + 1}: Invalid unit {sheet_data_obj['unit']}. "
                                f"It should be one of these: {', '.join(units)}.</li>"
                            )
                            
                        if sheet_data_obj["attributeSubCategory"].strip().lower() == 'plane':
                            attributeSubCategoryUnit = fieldData['unit']
                            if sheet_data_obj["unit"].strip().lower() not in attributeSubCategoryUnit:
                                validation_str += (
                                    f"<li>Row - {row_index + 1}: Invalid unit {sheet_data_obj['unit']}. "
                                    f"It should be one of these: {', '.join(attributeSubCategoryUnit)}.</li>"
                                )
                               
                        subtype_labels = []
                        for sub_type_key, sub_type_field in options.items():
                            subTypeFields = typeFields['options'][sub_type_key]
                            # print( typeFields['options'],"qqqq")
                            sub_type_label = subTypeFields.get("sheetLabel") or subTypeFields.get("label")
                            subtype_labels.append(sub_type_label)
                            if sub_type_label.strip().lower() == sheet_data_obj["subType"].strip().lower():
                                is_sub_type_valid = True
                                # print("innnnn",subTypeFields)
                                # Validate energy source
                                if category == "purchasedEnergy" and "generated" in subTypeFields.get("source", []):
                                    validation_str += (
                                        f"<li>Row - {row_index + 1}: Invalid subtype {sheet_data_obj['subType']}. "
                                        f"It should be {options['grid']['label']}.</li>"
                                    )
                                elif category == "generatedElectricity" and "non-generated" in subTypeFields.get("source", []):
                                    generated_labels = [
                                        option["label"]
                                        for option in options.values()
                                        if "generated" in option.get("source", [])
                                    ]
                                    validation_str += (
                                        f"<li>Row - {row_index + 1}: Invalid subtype {sheet_data_obj['subType']}. "
                                        f"It should be one of these: {', '.join(generated_labels)}.</li>"
                                    )
                                # Validate unit for sub-type
                                if subTypeFields.get("unit", []) :
                                    units = [unit.strip().lower() for unit in subTypeFields.get("unit", [])]
                                else :
                                    units = [unit.strip().lower() for unit in typeFields.get("unit", [])]
                                    
                                if sheet_data_obj["unit"].strip().lower() not in units:
                                    validation_str += (
                                        f"<li>Row - {row_index + 1}: Invalid unit {sheet_data_obj['unit']}. "
                                        f"It should be one of these: {', '.join(units)}.</li>"
                                    )

                        if not is_sub_type_valid and subtype_labels:
                            validation_str += (
                                f"<li>Row - {row_index + 1}: Invalid sub-type {sheet_data_obj['subType'] or 'blank'}. "
                                f"It should be one of these: {', '.join(subtype_labels)}.</li>"
                            )

                if not is_type_valid and type_labels:
                    validation_str += (
                        f"<li>Row - {row_index + 1}: Invalid type {sheet_data_obj['type'] or 'blank'}. "
                        f"It should be one of these: {', '.join(type_labels)}.</li>"
                    )

        if not attribute_sub_category_valid:
            validation_str += (
                f"<li>Row - {row_index + 1}: Invalid sub-category {sheet_data_obj['attributeSubCategory']}. "
                f"It should be one of these: {', '.join(attribute_sub_category_labels)}.</li>"
            )
            if custom_project_found:
                validation_str += (
                    f"<li>Row - {row_index + 1}: For Custom project, 'Custom' should be added in 'Detailed Carbon' column.</li>"
                )

    elif section_fields == "userdefine":
        validation_str += (
            f"<li>Row - {row_index + 1}: Invalid type {sheet_data_obj['type']}. It should be 'Custom'.</li>"
        )
    else:
        validation_str += (
            f"<li>Row - {row_index + 1}: Invalid sub-category {sheet_data_obj['attributeSubCategory']}.</li>"
        )

    return validation_str

def fieldTypeValidation(params,rowIndex):
    validationStr = ""
    if params:
        for obj in params:
            fieldName = obj.get('fieldName', 'unknown')
            sheetDataValue = obj.get('sheetData')
            required = obj.get('required', False)
            expectedType = obj.get('type')

            # Convert expected type to Python type
            pythonType = str if expectedType == 'string' else (int, float) if expectedType == 'number' else None
            # Check if sheetDataValue matches expected type
            if pythonType and sheetDataValue and not isinstance(sheetDataValue, pythonType):
                validationStr += (
                    f"<li>Row - {rowIndex + 1}: Invalid field {fieldName}. "
                    f"It shoulds be {expectedType}.</li>"
                )

            # Handle required validations
            if required:
                if expectedType == 'number' and not isinstance(sheetDataValue, (int, float)):
                    validationStr += (
                        f"<li>Row - {rowIndex + 1}: Invalid field {fieldName}. "
                        f"It should not be blank and should be a number.</li>"
                    )
                elif expectedType == 'string':
                    if isinstance(sheetDataValue, (int, float)):
                        validationStr += (
                            f"<li>Row - {rowIndex + 1}: Invalid field {fieldName}. "
                            f"It should not be a number.</li>"
                        )
                    elif not sheetDataValue:
                        validationStr += (
                            f"<li>Row - {rowIndex + 1}: Invalid field {fieldName}. "
                            f"It should not be blank.</li>"
                        )
            # Handle non-required fields with unexpected data
            elif required == '' and sheetDataValue:
                validationStr += (
                    f"<li>Row - {rowIndex + 1}: Invalid field {fieldName}. "
                    f"It shouldss be blank.</li>"
                )

    return validationStr

    
    
def lower_case(value: str) -> str:
    """Convert a string to lowercase and strip whitespace."""
    return re.sub(r'\s+', ' ', value.strip().lower())

def reverseObject(obj):
    return {v: k for k, v in obj.items()}

def get_attribute_subcategories(config: Dict[str, Any]) -> List[str]:
    """
    Recursively traverses the config to extract attribute subcategories.
    """
    subcategories = []

    def traverse(obj):
        for key, value in obj.items():
            if key == "attributeSubCategory" and isinstance(value, dict):
                for sub_key, sub_value in value.items():
                    if sub_key != "custom" and sub_value != "userdefine":
                        subcategories.append(sub_value.get("label", ""))
            elif isinstance(value, dict):
                traverse(value)

    traverse(config)
    return subcategories

def excelDateToFormatedDate(excel_date: float) -> str:
    """Convert Excel date to a JS-like date string."""
    start_date = datetime(1899, 12, 30)
    result_date = start_date + timedelta(days=excel_date)
    return result_date.strftime('%b-%Y')

def validateDate(date_str: str) -> bool:
    """Validate date in the format Month-Year (e.g., Jan-2019)."""
    return bool(re.match(r'^[a-zA-Z]{3}-\d{4}$', date_str))