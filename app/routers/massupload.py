from fastapi import APIRouter,File, UploadFile,HTTPException
from app.config import massupload_config
import os
import logging
from app.helpers import massupload_utils
import time

router = APIRouter()

@router.post("/v2/carbon_data/sheet_wise_mass_upload")
async def sheet_wise_mass_upload(file:UploadFile = File(...)):
    start_time = time.time()
    print(f"Task start time {start_time:.2f}")
    # validate upload file extension
    if not any(file.filename.endswith(ext) for ext in massupload_config.EXTENSION):
        message = "Unsupported file type.upload only xlsx file"
        logging.error(message)
        return {
            "code": "400",
            "status": False,
            "message": message
        }
    
    try :
        # Upload file on local
        uploadpath = massupload_config.FILE_UPLOAD_PATH
        if not os.path.exists(uploadpath):
            os.makedirs(uploadpath)
            
        filePath = os.path.join(uploadpath, file.filename)
        with open(filePath,'wb') as buffer:
          buffer.write(await file.read())  
          
        response = await massupload_utils.sheetWiseValidation(filePath)
        
        print(f"Finished task:{time.time():.2f}, duration: {time.time() - start_time:.2f} seconds")
        if response['isAllSheetValid'] :
            return {"message":"file uploaded successfully","sheetdata":response['sheetWiseData']}
        else :
            return response
    
    except Exception as e:
        logging.error(e)
        print(e)
        raise HTTPException(
            status_code=500,
            detail=f"error in script: {e}"
        )
        
   
