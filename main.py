from fastapi import FastAPI, Request   # the FastAPI class is import from a dependency fastapi
from fastapi.staticfiles import StaticFiles          # staticfiles makes a folder static means available to anyone
from routers import route_1_parameters  # import this file from this folder
from routers import routes_2_parameters
from routers import route_3_file_handlling
from routers import route_4_no_sql_practice
from routers import route_5_sql_practice
from utils.exception_handling import add_exception_handlers  # importing handlers file from utils
import time, os
import config
app = FastAPI()          # here object is creating app the main application to make apis 

add_exception_handlers(app)          # handlers are connected with main 

os.makedirs( config.static_folder_files_upload, exist_ok= True)       # make sure folder exist if not make it

# mount the folder static so files can be assed via url
app.mount("/static", StaticFiles(directory=config.Upload_folder), name="static")

# adding middleware

@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()

    response = await call_next(request)

    process_time = time.time() - start_time
    print(f"Request: {request.url.path} completed in {process_time:.2f}s")

    return response



@app.get("/")              # this is a decorator and making a request of get at home page /
def test():             # when request is called this function called
    return{"message":"welcome to FastAPI"}



app.include_router(route_1_parameters.students_router)    # from file route_1_parameters import students_router
app.include_router(routes_2_parameters.school_router)
app.include_router(route_3_file_handlling.files_router)
app.include_router(route_4_no_sql_practice.mdcat_router)
app.include_router(route_5_sql_practice.degree_router)
#poetry run uvicorn main:app --reload