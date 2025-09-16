from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean, Float
from sqlalchemy.orm import declarative_base, Relationship
import datetime

Base = declarative_base()

class student(Base):
    __tablename__ = "students_degree_certificate"

    id = Column(Integer, primary_key= True, index= True )

    name = Column(String, nullable= False, index= True)

    corse_duration = Column(Integer, nullable= False)

    cgpa = Column(Float, nullable= False)

    corse_compleated = Column(Boolean, nullable= False)

    address = Column(String, nullable= True)

    age = Column(String, nullable= False, default= 0)

    roll_number = Column(Integer, unique= True, nullable= False)

    created_at = Column(DateTime, default= datetime.datetime.now() )

    courses_table = Relationship("courses", back_populates="student_table")


class courses(Base):
    __tablename__ = "student_courses"

    id = Column(Integer, primary_key= True, index= True)
    books = Column(String, nullable= False)
    student_id = Column(Integer, ForeignKey(student.id))        # making a link with student.id student_courses
    student_table = Relationship("student", back_populates="courses_table")