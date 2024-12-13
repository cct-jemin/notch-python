from fastapi import HTTPException
from app.config import massupload_config,v2ScopeCategoryConfig
import logging
import pandas as pd
from app.schemas import massupload_validation_schema
import re
import asyncio
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from openpyxl import load_workbook
from typing import Dict, List, Any

labelIgnore = ['category','custom']

executor = ThreadPoolExecutor()

async def sheetWiseValidation(filePath):
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
        tasks.append(validate_sheet(sheetName, sheetData,sheetWiseData))
        
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
        return {"isAllSheetValid":True,"sheetWiseData" : sheetWiseData['sheets']}


async def validate_sheet(sheetName, sheetData,sheetWiseData):
    await asyncio.to_thread(sync_validate,sheetName,sheetData,sheetWiseData)
   
    
    
def sync_validate(sheetName, sheetData, sheetWiseData):
    # start_time = time.time()
    # print(f"Start processing sheet: {sheetName} at {start_time:.2f}")
    maxAllowedColumnNumber = 25
    headerStartIndexColumnNumber = 13
    sheetInfo = massupload_validation_schema.massUploadValidationSchema["sheetMapping"][sheetName.lower()]
    sectionNameMapping = massupload_validation_schema.massUploadValidationSchema['sectionNameMapping']
    sectionNameMappingReverse = reverseObject(sectionNameMapping)
   #for now take data from config file
    scope = str(sheetInfo['scope'])
    category = sheetInfo['category']
    sheetWiseData['sheets'][sheetName] = {"scope" : scope, "category" : category, "data" : [], "sectionPointer" : '', "validationStr" : ''}
    section_pointer_name = None
    valid_section_name_array = [
        sectionNameMappingReverse[sectionPointer]
        for sectionPointer in sheetInfo['sectionPointer']
        if sectionPointer in sectionNameMappingReverse
    ]
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

        elif row[0] and section_pointer_name != 'company information' and row[0].lower() not in labelIgnore:
            sheetWiseData['sheets'][sheetName]['validationStr'] += (
                f"<li>Row - {i+1} : Invalid Section name. It should be one of these {', '.join(valid_section_name_array)}.</li>"
            )
            break
        
        # Category validation
        if section_pointer_name != 'company information':
            attributeCategoryFields = v2ScopeCategoryConfig.scopeConfig[scope][category]
            if row[0] and row[0].strip().lower() == "category":
                print(attributeCategoryFields['label'].strip().lower(),"----")
                # Check if the attributeCategoryFields label matches the category in sheet_data
                if attributeCategoryFields and attributeCategoryFields['label'].strip().lower() != sheetData[0][1].strip().lower():
                    sheetWiseData['sheets'][sheetName]['validationStr'] += f"<li>Row - {i + 1} : Invalid Category name {sheetData[0][1]}. It should be {attributeCategoryFields['label']}.</li>"
                    break
            # attributeSubCategoryFields = get_attribute_subcategories(v2ScopeCategoryConfig.scopeConfig)


    sheetWiseData['sheets'][sheetName]['data'] = sheetData
    # print(f"Finished processing sheet: {sheetName} at {time.time():.2f}, duration: {time.time() - start_time:.2f} seconds")
    
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