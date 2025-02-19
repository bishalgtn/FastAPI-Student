from fastapi import FastAPI, Path, Query
from typing import Optional
from pydantic import BaseModel
# from data import student_data

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
    "102": {"id": 102, "name": "Bishal Dangol", "section": "A1", "location": "Kathmandu"},
    "104": {"id": 104, "name": "Kabisha Gautum", "section": "A2", "location": "Nagarkot"},
    "106": {"id": 106, "name": "Arjun Shahi", "section": "A1", "location": "Surkhet"},
    "108": {"id": 108, "name": "Kabina Giri", "section": "A2", "location": "Sundhupalchowk"},
    "110": {"id": 110, "name": "Ravi Thapa", "section": "A3", "location": "Pokhara"},
    "112": {"id": 112, "name": "Suman Rai", "section": "A1", "location": "Bhairahawa"},
    "114": {"id": 114, "name": "Sita Adhikari", "section": "A2", "location": "Chitwan"},
    "116": {"id": 116, "name": "Pradeep Kumar", "section": "A3", "location": "Itahari"},
    "118": {"id": 118, "name": "Rina Sharma", "section": "A2", "location": "Lalitpur"},
    "120": {"id": 120, "name": "Nirajan Joshi", "section": "A1", "location": "Bhaktapur"},
    "122": {"id": 122, "name": "Anish Baral", "section": "A3", "location": "Dang"},
    "124": {"id": 124, "name": "Shiva Tamang", "section": "A1", "location": "Nawalparasi"},
    "126": {"id": 126, "name": "Nita Shrestha", "section": "A2", "location": "Rasuwa"},
    "128": {"id": 128, "name": "Binita Gurung", "section": "A3", "location": "Gorkha"},
    "130": {"id": 130, "name": "Dinesh Joshi", "section": "A2", "location": "Sindhupalchowk"},
    "132": {"id": 132, "name": "Madhav Koirala", "section": "A1", "location": "Bardiya"},
    "134": {"id": 134, "name": "Suraj Thakur", "section": "A3", "location": "Lumbini"},
    "136": {"id": 136, "name": "Rashmi Pokhrel", "section": "A1", "location": "Bhojpur"},
    "138": {"id": 138, "name": "Gita Adhikari", "section": "A2", "location": "Kavre"},
    "140": {"id": 140, "name": "Prakash Chhetri", "section": "A3", "location": "Syangja"},
    "142": {"id": 142, "name": "Maya Sharma", "section": "A1", "location": "Makwanpur"},
    "144": {"id": 144, "name": "Ashok Rai", "section": "A2", "location": "Parsa"},
    "146": {"id": 146, "name": "Subash Thapa", "section": "A3", "location": "Kaski"},
    "148": {"id": 148, "name": "Sumitra Raut", "section": "A1", "location": "Dhanusha"},
    "150": {"id": 150, "name": "Ravi Ghimire", "section": "A2", "location": "Ramechhap"},
    "152": {"id": 152, "name": "Bikash Baral", "section": "A3", "location": "Tanahu"},
    "154": {"id": 154, "name": "Kamala Yadav", "section": "A1", "location": "Morang"},
    "156": {"id": 156, "name": "Ranjan Kunwar", "section": "A2", "location": "Sunsari"},
    "158": {"id": 158, "name": "Bishnu Shrestha", "section": "A3", "location": "Jhapa"},
    "160": {"id": 160, "name": "Sandhya Karki", "section": "A1", "location": "Illam"}
}

@app.get("/")
def read_root():
    return {"message": "Welcome to Home"}

@app.get("/students/{student_id}")
async def student(student_id: int):
    if student_id in student_data:
        return student_data[student_id]
    else:
        return {"Error":f"students with id {student_id} does not exist"}

@app.get("/students_with_path/{student_id}")
async def student_detail(student_id: int = Path):
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
