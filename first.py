from fastapi import FastAPI
from pydantic import BaseModel


class College(BaseModel):
    name: str


app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}


@app.get("/students/student_data")
def student():
    student_data = {
        {"id": 102,
        "name":"Bishal Dangol",
        "section": "A1",
        "location": "kathmandu"
        },
        {"id": 104,
        "name":"kabisha Gautum",
        "section": "A2",
        "location": "Nagarkot"
        }
    }

    return student_data
 

@app.get("/section/{section_id}")
def read_section(section_id : int, section: str | None = None):
    student_data = {
        {"id": 102,
        "name":"Bishal Dangol",
        "section": "A1",
        "location": "kathmandu"
        },
        {"id": 104,
        "name":"kabisha Dangol",
        "section": "A2",
        "location": "Kathmandu"
        }
    }
    if section_id == 104:
        return student_data()
    
    return {"id":section_id, "section":section} 