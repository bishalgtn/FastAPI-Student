from fastapi import FastAPI, Form
from pydantic import BaseModel, EmailStr, validator
from typing import Optional
from datetime import date, time
import phonenumbers
from fastapi.responses import HTMLResponse

# Decleraction of app
app = FastAPI()

# Pydentic model for Blog post 
class Blog_Post(BaseModel):
    title : str
    discription: str
    author: str
    tag: list[str] = []
    add_blog_date : date
    add_blog_time : time


class Feedback(BaseModel):
    name: str
    middle_name: Optional[str] = None
    last_name: str
    email: EmailStr
    discription: str
    phonenumbers: Optional [str] = None
    
    @validator('phonenumbers')
    def validate_phone_number(cls, v):
        try:
            validate_phoneNumber = phonenumbers.parse(v)
            if not phonenumbers.is_valid_number(parsed_number):
                raise ValueError('Invalid phone number')
        except phonenumbers.phonenumberutil.NumberParseException:
            raise ValueError('Invalid phone number format')
        return v
    


@app.get('/')
async def root():
    return "welcome to API"

@app.get('/blog')
async def vew_blog():
    return "post"

@app.get('/feedback', response_class=HTMLResponse)
async def user_feedback():
    return """
    <form action="/submit" method="POST">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required><br>
        <label for="middle_name">Middle name:</label>
        <input type="text" id="middle_name" name="middle_name"><br>
        <label for="last_name">last name:</label>
        <input type="text" id="last_name" name="last_name" required><br>
        <label for="email">email:</label>
        <input type="text" id="email" name="email" required><br>
        <label for="phone_number">Phone Number:</label>
        <input type="text" id="phone_number" name="phone_number"><br>
        <label for="discription">Discription:</label>
        <input type="text" id="discription" name="discription"><br>
        <button type="submit">Submit</button>
    </form>
    """


@app.post("/submit")
async def submit(
    name: str = Form(...),
    middle_name: Optional[str] = Form(None),
    last_name: str = Form(...),
    email: str = Form(...),
    phone_number: Optional[str] = Form(None),
    discription: str = Form(...)
):
    try:
        # Manually create the Feedback object with form data
        feedback = Feedback(
            name=name,
            middle_name=middle_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
            discription = discription
        )
        # Log the feedback data for debugging
        print(f"User Data: {feedback.dict()}")
        
        # Return a success message
        return {"message": "Form submitted successfully!"}
    
    except Exception as e:
        # Log the exception
        print(f"Error: {str(e)}")
        
        # Return an error response with a message and the exception details
        return {"error": f"Internal Server Error: {str(e)}"}


@app.post('/blog_create')
async def post_blog(Title, Body):
    
    return {"Title": Title, "Discription": Body}

@app.post('/blog_create')
async def post_blog(Title, Body):

    return {"Title": Title, "Discription": Body}