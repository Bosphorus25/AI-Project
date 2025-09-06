from fastapi import FastAPI,HTTPException    # the FastAPI class is import from a dependency fastapi
from pydantic import BaseModel
app = FastAPI()          # here object is creating app the main application to make apis 

@app.get("/student/{id}")
def data(id: int):
    try:
        database = {
            1: {"name": "ali", "class": 10},
            2: {"name": "sami", "class": 10},
            3: {"name": "faiq", "class": 10},
            4: {"name": "hamza", "class": 10},
            5: {"name": "roby", "class": 10},
        }
        if id not in database:
            raise HTTPException(status_code=404, detail="student not found")
        return{
            "status": "sucess",
            "message": "student found sucessfully",
            "data": database[id]
        }
    except HTTPException as e:
        return{
            "status": "error",
            "message": e.detail,
            "data": None
        }
    except Exception as e:
        return{
            "status": "error",
            "message": str(e),
            "data": None
        }




@app.get("/search")
def search(class_: int):
    try:
        database = {
            1: {"student 1": "ali", "student 2": "saim"},
            2: {"student 1": "sami", "student 2": "hamza"},
            3: {"student 1": "faiq", "student 2": "asad"},
            4: {"student 1": "hamza", "student 2": "amjad"},
            5: {"student 1": "roby", "student 2": "ahmed"},
        }
        if class_ not in database:
            raise HTTPException(status_code=404, detail="class not found")
        return{
            "status": "sucess",
            "message": "class found sucessfully",
            "data": database[class_]
        }
    except HTTPException as e:
        return{
            "status": "error",
            "message": str(e),
            "data": None
        }
    except Exception as e:
        return{
            "status": "error",
            "message": str(e),
            "data": None
        }
    


class data(BaseModel):
    id: int
    name: str
    class_: int

@app.post("/add_student")
def school(data: data):
    try:
        database = {
            1: {"name": "ali", "class": 10},
            2: {"name": "sami", "class": 10},
            3: {"name": "faiq", "class": 10},
            4: {"name": "hamza", "class": 10},
            5: {"name": "roby", "class": 10},
        }
        if data.id in database:
            raise HTTPException(status_code=409, detail="student already exist")
        database[data.id] = {"name": data.name, "class_": data.class_}           # in database make key which comes from data.id and its values are = {"name": data.name, "class_": data.class_} this
        return{
             "status": "sucess",
            "message": "student added sucessfully",
            "data": database[data.id]                  # return from database .id of class data
        }
    except HTTPException as e:
        return{
            "status": "error",
            "message": str(e),
            "data": None
        }
    except Exception as e:
        return{
            "status": "error",
            "message": str(e),
            "data": None
        }
