from fastapi import FastAPI, Path, Query
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class Student(BaseModel):
    name: str
    section: str
    location: str
    exam_status :bool
    phone_number: int

class UpdateStudent(BaseModel):
    name: Optional[str] = None
    section: Optional[str] = None
    location: Optional[str] = None
    exam_status: Optional[bool] = None
    phone_number: Optional[int] = None


student_data = {
    102:{"id": 102,
    "name":"Bishal Dangol",
    "section": "A1",
    "location": "kathmandu"
    },
    104:{"id": 104,
    "name":"kabisha Gautum",
    "section": "A2",
    "location": "Nagarkot"
    },
    106:{"id": 106,
    "name":"Arjun Shahi",
    "section": "A1",
    "location": "Surkhet"
    },
    108:{"id": 108,
    "name":"kabina Giri",
    "section": "A2",
    "location": "Sundhupalchowk"
    },
}

@app.get("/")
def read_root():
    return {"message": "Welcome to Home"}

@app.get("/students/{student_id}")
def student(student_id: int):
    if student_id in student_data:
        return student_data[student_id]
    else:
        return {"Error":f"students with id {student_id} does not exist"}

@app.get("/students_with_path/{student_id}")
def student_detail(student_id: int = Path):
    return student_data[student_id]

@app.post("/create_student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in student_data:
        return {"Error": "student already exist with the student id"}
    student_data[student_id] = student
    return student_data[student_id]

@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in student_data:
        return {"Error": f" Student with studentId {student_id}, doesn't exist"}
    
    if student.section != None:
        student_data[student_id].section= student.section

    if student.location != None:
        student_data[student_id].location = student.location

    if student.name != None:
        student_data[student_id].phone_number = student.phone_number

    if student.exam_status != None:
        student_data[student_id].exam_status = student.exam_status

    return student_data[student_id]

@app.delete("/delete-item")
def delete_item(student_id: int = Query(..., description= "Provide Id of the student to delete student data")):
    if student_id not in student_data:
        return {"error": "Id doesnot exist"}
    del student_data[student_id]

    return {"Sucess":f"student with {student_id} has deleted"}
