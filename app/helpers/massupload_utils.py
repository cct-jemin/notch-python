from fastapi import HTTPException
from app.config import massupload_config
import logging
import pandas as pd
from app.schemas import massupload_validation_schema
import re

async def sheetWiseValidation(filePath):
    print("validation function call")
    excel_data = pd.ExcelFile(filePath, engine='openpyxl')
    sheetNamesAarry = excel_data.sheet_names
    sheetWiseData = {'sheets' : {}, 'validationStr' : ''}
    for sheetName in sheetNamesAarry:
        
        if sheetName.lower() not in massupload_validation_schema.massUploadValidationSchema["sheetMapping"] :
            continue     
        
        sheetInfo = massupload_validation_schema.massUploadValidationSchema["sheetMapping"][sheetName.lower()]
        df = excel_data.parse(sheetName,header=None)
        df = df.fillna(value='')
        sheetData = df.values.tolist()
        
        
        return {"isAllSheetValid":True,"sheetWiseData" : sheetWiseData['sheets']}

def lower_case(value: str) -> str:
    """Convert a string to lowercase and strip whitespace."""
    return re.sub(r'\s+', ' ', value.strip().lower())