from fastapi import APIRouter, HTTPException
from utils.authentication_utils import validation

students_router = APIRouter(
    prefix= "/students",
    tags= ["students"]
)

@students_router.get("/welcome")
def wow():
    return{"message":"welcome to fastapi"}

@students_router.get("/cnic/{student_cnic}")     # this function linked with utils
def authentic(student_cnic: int):
    check = validation(student_cnic)
    return{
        "status": "sucess",
        "message": "cnic entered sucessfully",
        "data": check
        }
  

    


@students_router.get("/test/{number}")         # path example
def wow(number: int):
    return{"marks in test":number}

@students_router.get("/id/{number}")         # path and query example
def data(number: int, class_: int, name: str):
    return{"id":number,
           "class": class_,
           "name": name
        }
