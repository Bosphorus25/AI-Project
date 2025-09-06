from fastapi import FastAPI     # the FastAPI class is import from a dependency fastapi

app = FastAPI()          # here object is creating app the main application to make apis 

@app.get("/")              # this is a decorator and making a request of get at home page /
def check():             # when request is called this function called
    return{"message":"sucessfull"}

@app.get("/welcome")
def wow():
    return{"message":"welcome to fastapi"}


@app.get("/test/{number}")         # path example
def wow(number: int):
    return{"marks in test":number}

@app.get("/id/{number}")         # path and query example
def data(number: int, class_: int, name: str):
    return{"id":number,
           "class": class_,
           "name": name
        }



#poetry run uvicorn main:app --reload