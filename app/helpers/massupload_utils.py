from fastapi import HTTPException
from app.config import massupload_config
import logging
import pandas as pd
from app.schemas import massupload_validation_schema
import re
import asyncio
import time

async def sheetWiseValidation(filePath):
    start_time = time.time()
    print(f"validation start time {start_time:.2f}")
    excel_data = pd.ExcelFile(filePath, engine='openpyxl')
    sheetNamesAarry = excel_data.sheet_names
    sheetWiseData = {'sheets' : {}, 'validationStr' : ''}
    tasks = []
    for sheetName in sheetNamesAarry:
        
        if sheetName.lower() not in massupload_validation_schema.massUploadValidationSchema["sheetMapping"] :
            continue     
    
        df = excel_data.parse(sheetName,header=None)
        df = df.fillna(value='')
        sheetData = df.values.tolist()
        tasks.append(validate_and_insert(sheetName, sheetData,sheetWiseData))
        
    # Execute all tasks concurrently
    await asyncio.gather(*tasks)
    print(f"Finished validation time:{time.time():.2f}, duration: {time.time() - start_time:.2f} seconds")
        
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

def lower_case(value: str) -> str:
    """Convert a string to lowercase and strip whitespace."""
    return re.sub(r'\s+', ' ', value.strip().lower())

async def validate_and_insert(sheetName, sheetData,sheetWiseData):
    start_time = time.time()
    print(f"Start processing sheet: {sheetName} at {start_time:.2f}")
    sheetInfo = massupload_validation_schema.massUploadValidationSchema["sheetMapping"][sheetName.lower()]
   #for now take data from config file
    scope = sheetInfo['scope']
    category = sheetInfo['category']
    
    sheetWiseData['sheets'][sheetName.lower()] = {"scope" : scope, "category" : category, "data" : [], "sectionPointer" : '', "validationStr" : ''}
    
    section_pointer_name = None
    first_cell_value = lower_case(sheetData[0][0])
    
    #first row column validation
    if not category and first_cell_value != "company information":
        sheetWiseData['sheets'][sheetName.lower()]['validationStr'] += (
            f"<li>Row - 1 : Invalid name. It should be Company Information.</li>"
        )
    elif not category and first_cell_value == "company information":
        section_pointer_name = first_cell_value
    elif category and first_cell_value == "category":
        section_pointer_name = lower_case(sheetData[1][0]) if len(sheetData) > 1 else None
    else:
        sheetWiseData['sheets'][sheetName.lower()]['validationStr'] += (
            f"<li>Row - 1 : Invalid {sheetData[0][0]}. It should be Category.</li>"
        )
    print(section_pointer_name)    
    sheetWiseData['sheets'][sheetName.lower()]['data'] = sheetData
    await asyncio.sleep(0.1)
    print(f"Finished processing sheet: {sheetName} at {time.time():.2f}, duration: {time.time() - start_time:.2f} seconds")