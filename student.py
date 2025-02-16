from fastapi import FastAPI, Path
from pydantic import BaseModel

app = FastAPI()

class Student(BaseModel):
    name: str
    section: str
    location: str
    exam_status :bool
    phone_number: int


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
    }
}

@app.get("/")
def read_root():
    return {"message": "Welcome to Home"}

@app.get("/students/{student_id}")
def student(student_id: int):
    return student_data[student_id]

@app.get("/students_with_path/{student_id}")
def student_detail(student_id: int = Path):
    return student_data[student_id]

@app.post("/create_student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in student_data:
        return {"Error": "student already exist with the student id"}
    student_data[student_id] = student
    return student_data[student_id]