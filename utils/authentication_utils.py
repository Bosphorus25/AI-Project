from fastapi import HTTPException

def validation(student_cnic: int):
    student_cnic = str(student_cnic)
    if len(student_cnic) < 11 or len(student_cnic) > 11:
        raise HTTPException(status_code=400, detail="enter 11 digit cnic number without dashes")
    return student_cnic