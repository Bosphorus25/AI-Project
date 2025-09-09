from fastapi import APIRouter, File, UploadFile, Form
import shutil
import os
import config


files_router = APIRouter(
    prefix= "/files",
    tags= ["files"]
)



# mount the folder static so files can be assed via url
# files_router.mount("/static", StaticFiles(directory=Upload_folder), name="static") 
# mount only works with app of FastAPI not with APIrouter thats why moved to main

# endpoint to upload files
@files_router.post("/upload")
def upload_file(file: UploadFile = File(...)):   # file: is a variable that recive this UploadFile of type File(...)
    file_path = os.path.join(config.Upload_folder, file.filename) # make a path to save like upload_files/filename.png
    with open(file_path, "wb") as buffer:        # Opens the file in write-binary (wb) mod "wb" = create new file or overwrite existing one in binary mode.
        shutil.copyfileobj(file.file, buffer)           #Copies the content of uploaded file (file.file) into your local file (buffer).                            
    file_url = f"/static/{file.filename}"                #make a url to return user to assess file later
    return{
        "file name": file.filename, "file url": file_url
    }