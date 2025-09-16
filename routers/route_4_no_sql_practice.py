from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from bson.objectid import  ObjectId
from utils.setup_mongodb_sql_atlas import db # db dummy was imported here

collection = db["test_db"]

mdcat_router = APIRouter(
    prefix= "/mdcat",
    tags= ["mdcat"]
)

class student_info(BaseModel):
    name: str
    address: str
    age: int
    roll_no: int


@mdcat_router.post("/add_one_student")
def add_student(student_information: student_info):      # in this function a document is inserted in collection
    student_1 = collection.insert_one({
        "name": student_information.name,               # .insert_one tested 
        "address": student_information.address,
        "age": student_information.age,
        "roll_no": student_information.roll_no
    })
    return{
        "status": "student added sucessfully",
        "error": None,
        "id": str(student_1.inserted_id)               # .inserted_id tested inserted is method of pymongo
    }

@mdcat_router.post("/add_many_students")
def add_many_students(student_information: List[student_info]):
    student_dict = []
    for s in student_information:
        student_dict.append({
            "name": s.name,
            "address": s.address,
            "age": s.age,
            "roll_no": s.roll_no
        })
    all_students = collection.insert_many(student_dict)     # .insert_many tested
    return{
        "status": "students added sucessfully",
        "error": None,
        "ids": [str(_id) for _id in all_students.inserted_ids]            
    }         # return a string of _id by a loop for every _id in list all_students where id is inserted
    
@mdcat_router.get("/get_all_students")
def get_all_students():
    student_list = []
    for students in collection.find():
        students["_id"] = str(students["_id"])          # .find tested
        student_list.append(students)
    return{
    "status": "all students in collection test_db",
    "error": None,
    "data": student_list
    }

@mdcat_router.get("/get_one_student")
def get_one_students(name: str):
    student = collection.find_one({"name": name})        # .find_one tested
    if student:
        student["_id"] = str(student["_id"])
        return{
        "status": "student find sucessfully",
        "error": None,
        "data": student
        }
    else:
        raise HTTPException(status_code=404, detail= "student not found")


@mdcat_router.get("/find_one_student")
def find_one_students(id: str):
    student = collection.find_one({"_id": ObjectId(id)})        # .find_one tested with object id
    if student:
        student["_id"] = str(student["_id"])
        return{
        "status": "student find sucessfully",
        "error": None,
        "data": student
        }
    else:
        raise HTTPException(status_code=404, detail= "student not found")


    
@mdcat_router.post("/update_one_student")
def update_one_student(name: str, student_information: student_info):
    updated_student = collection.update_one(          # update_one tested
    {"name": name},      # filter: which document to update
    {"$set":{            # $set: update only these fields
    "name": student_information.name,                
    "address": student_information.address,
    "age": student_information.age,
    "roll_no": student_information.roll_no
    }})
    if updated_student.matched_count == 0:
        raise HTTPException(status_code=404, detail= "student not found")
    return{
        "status": "student updated sucessfully",
        "error": None,
        "matched count": updated_student.matched_count,
        "modified count": updated_student.modified_count               
    }
    
class student_info_2(BaseModel):
    address: str

@mdcat_router.post("/update_many_students")
def update_many_students(address: str, student_information: student_info_2):
    updated_student = collection.update_many(              # update_many tested
    {"address": address},      # filter: which document to update
    {"$set":{            # $set: update only these fields                
    "address": student_information.address
    }})
    if updated_student.matched_count == 0:
        raise HTTPException(status_code=404, detail= "student not found")
    return{
        "status": "students updated sucessfully",
        "error": None,
        "matched count": updated_student.matched_count,
        "modified count": updated_student.modified_count               
    }
    
@mdcat_router.delete("/delete_one")
def delete_one(name: str):
    student= collection.delete_one({"name": name})  # delete_one tested
    if student.deleted_count == 0:
        raise HTTPException(status_code=404, detail="student not found")
    return{
         "status": "student deleted sucessfully",
        "error": None,
        "data": None
    }
    

@mdcat_router.delete("/delete_many")
def delete_many(address: str):
    student= collection.delete_many({"address": address})    # delete_many tested
    if student.deleted_count == 0:
        raise HTTPException(status_code=404, detail="students not found")
    return{
         "status": "student deleted sucessfully",
        "error": None,
        "data": None
    }