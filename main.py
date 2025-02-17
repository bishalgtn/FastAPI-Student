from enum import Enum

from fastapi import FastAPI, Path


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


app = FastAPI()

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
def student(student_id: int = Path):
    return student_data[student_id]




@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}