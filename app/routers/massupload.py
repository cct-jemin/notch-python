from fastapi import APIRouter,File, UploadFile,HTTPException,Form
from app.config import massupload_config
import os
import logging
from app.helpers import massupload_utils
import time
from pydantic import BaseModel
from typing import Optional


router = APIRouter()

@router.post("/")
async def sheet_wise_mass_upload(file: UploadFile = File(...),org_id: str = Form(...),site_id: Optional[str] = Form(None) ):
    # start_time = time.time()
    # print(f"Task start time {start_time:.2f}")
    # validate upload file extension
    if not any(file.filename.endswith(ext) for ext in massupload_config.EXTENSION):
        message = "Unsupported file type.upload only xlsx file"
        logging.error(message)
        return {
            "code": "400",
            "status": False,
            "message": message
        }
    
    # try :
        # Upload file on local
    uploadpath = massupload_config.FILE_UPLOAD_PATH
    if not os.path.exists(uploadpath):
        os.makedirs(uploadpath)
        
    requestParam = {}
    requestParam.update({
        'filePath':os.path.join(uploadpath, file.filename), 
        'org_id': org_id,
        'site_id': site_id,
        'admin_email':'',
        'company_name':'',
    })
    with open(requestParam['filePath'],'wb') as buffer:
        buffer.write(await file.read())  
        
    response = await massupload_utils.sheetWiseValidation(requestParam)
    
    # print(f"Finished task:{time.time():.2f}, duration: {time.time() - start_time:.2f} seconds")
    if response['isAllSheetValid'] :
        return {"message":"file uploaded successfully","validationObj":response['validationObj']}
    else :
        return response
    
    # except Exception as e:
    #     logging.error(e)
    #     print(e)
    #     raise HTTPException(
    #         status_code=500,
    #         detail=f"error in script: {e}"
    #     )
        
   
