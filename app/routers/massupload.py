from fastapi import APIRouter,File, UploadFile,HTTPException
from app.config import massupload_config
import os
import logging

router = APIRouter()

@router.post("/v2/carbon_data/sheet_wise_mass_upload")
async def sheet_wise_mass_upload(file:UploadFile = File(...)):
    if not any(file.filename.endswith(ext) for ext in massupload_config.EXTENSION):
        message = "Unsupported file type.upload only xlsx file"
        logging.error(message)
        raise HTTPException(status_code=400,detail=message) 
    
    try :
        uploadpath = massupload_config.FILE_UPLOAD_PATH
        if not os.path.exists(uploadpath):
            os.makedirs(uploadpath)
            
        file_location = os.path.join(uploadpath, file.filename)
        with open(file_location,'wb') as buffer:
          buffer.write(await file.read())  
          
        return {"message":"file uploaded successfully"}
    
    except Exception as e:
        logging.error(e)
        print(e)
        raise HTTPException(
            status_code=500,
            detail=f"error in script: {e}"
        )
   
