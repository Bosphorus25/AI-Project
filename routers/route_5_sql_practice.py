from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from utils.database import get_db
from utils.jwt_token_setup import create_jwt_token, verify_token, hash_password, verify_hash_password
from utils.postgress_sql_students_models import student, courses, authentic
from pydantic import BaseModel , Field, EmailStr
from typing import List

degree_router = APIRouter(
    prefix="/generate_result",
    tags= ["generate_result"]
)

class student_data(BaseModel):
    name: str
    corse_duration: int
    cgpa: float
    corse_compleated: bool
    address: str
    age: int 
    roll_number: int
    student_signup_id: int


@degree_router.post("/result")
def result(student_data: student_data, token_verify= Depends(verify_token), db: Session = Depends(get_db)):
    check_schema = student(
        name=student_data.name,
        corse_duration= student_data.corse_duration,
        cgpa=student_data.cgpa,
        corse_compleated=student_data.corse_compleated,   # posting one student data to db tested
        address= student_data.address, 
        age= student_data.age, 
        roll_number= student_data.roll_number,
        student_signup_id= student_data.student_signup_id)
    db.add(check_schema)
    db.commit()
    db.refresh(check_schema)
    return check_schema

# token varification checked here
@degree_router.get("/get_all_students_result")
def get_all_students_result(token_verify= Depends(verify_token), db: Session = Depends(get_db)):    # fetching all data from table tested
    return db.query(student).all()

@degree_router.get("/get_one_student/{id}")
def get_one_student(id: int, db: Session= Depends(get_db)):
    db_student = db.query(student).filter(student.id == id).first()   # fetching one student from table
    if not db_student:
        raise HTTPException(status_code=404, detail="student not found")
    return{
        db_student
    }

class updated_data(BaseModel):
    cgpa: float
    corse_compleated: bool

@degree_router.put("/update_student/{id}")
def update_student(id: int, updated_data: updated_data, db: Session= Depends(get_db)):
    db_student = db.query(student).filter(student.id == id).first()        
    if not db_student:                                                          # updating a student info
        raise HTTPException(status_code=404, detail="student not found")
    db_student.cgpa = updated_data.cgpa
    db_student.corse_compleated = updated_data.corse_compleated
    db.commit()
    db.refresh(db_student)
    return{
        db_student
    }

@degree_router.delete("/delete_student/{id}")
def delete_student(id: int, db: Session= Depends(get_db)):
    db_student = db.query(student).filter(student.id == id).first()   # deleating a student
    if not db_student:
        raise HTTPException(status_code=404, detail="student not found")
    db.delete(db_student)
    db.commit()
    return{
        "status": "sucess",
        "data": None,
        "message": "student deleted scuessfully"
    }


#  testing links between two tables

class book_name(BaseModel):
    book: str

class student_courses(BaseModel):
    id: int
    all_books: List[book_name]


@degree_router.post("/add_student_courses")
def add_student_courses(student_courses: student_courses,token_verify= Depends(verify_token), db: Session= Depends(get_db)):
    db_student = db.query(student).filter(student.id == student_courses.id).first()  
    if not db_student:
        raise HTTPException(status_code=404, detail="student not found")
    
    for b in student_courses.all_books:
        new_courses = courses(books= b.book, student_id = student_courses.id)
        db.add(new_courses)
    db.commit()
    db.refresh(new_courses)
    return{
        "message": "courses added sucessfully"
    }

# testing relationship between two tables

@degree_router.get("/get_a_student/{id}")
def get_a_student(id: int, db: Session= Depends(get_db)):
    db_student = db.query(student).filter(student.id == id).first()   # fetching one student from table
    if not db_student:
        raise HTTPException(status_code=404, detail="student not found")
    return{
         "id": db_student.id,
         "name": db_student.name,
         "courses": [b.books for b in db_student.courses_table]
    }
    

# test generate jwt token with signup login

class signup(BaseModel):
    username: str
    email: EmailStr
    password: str = Field(min_length= 6)

# signup
@degree_router.post("/signup_here")
def signup_here(signup: signup, db: Session= Depends(get_db)):
    hashed_pswd = hash_password(signup.password)
    add_db = authentic(
        username= signup.username,
        email= signup.email,
        Password= hashed_pswd
    )
    db.add(add_db)
    db.commit()
    db.refresh(add_db)
    return{
        "message": "signup sucessfully"
    }

# login
@ degree_router.post("/login_here")
def login_here(data: signup, db: Session= Depends(get_db)):
    db_user = db.query(authentic).filter(authentic.email == data.email).first()

    if not db_user:  # user not found
        raise HTTPException(status_code=401, detail="invalid email")
    if data.username != db_user.username:
        raise HTTPException(status_code=401, detail="invalid username")
    if not verify_hash_password(data.password, db_user.Password):
        raise HTTPException(status_code=401, detail="invalid credentials")
    token = create_jwt_token(data={
        "username": data.username,
        "email": data.email,
    })
    return{
        "message": "token generated sucessflly",
        "data": token
    }