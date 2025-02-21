from fastapi import FastAPI
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
    tag: List[str] = []
    add_blog_date : date
    add_blog_time : time


class Feedback(BaseModel):
    name: str
    middle_name: Optional[str] = Null
    last_name: str
    email: EmailStr
    phonenumbers: Optional [str] = Null
    
    @validator('phonenumbers')
    def validate_phone_number(cls, v):
        try:
            validate_phoneNumber = phonenumbers.parse(v)
            if not phonenumbers.is_valid_number(parsed_number):
                raise ValueError('Invalid phone number')
        except phonenumbers.phonenumberutil.NumberParseException:
            raise ValueError('Invalid phone number format')
        return v
    
    discription: str


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
        <label for="phone_number">Phone Number:</label>
        <input type="text" id="phone_number" name="phone_number" required><br>
        <button type="submit">Submit</button>
    </form>
    """

@app.post("/submit")
async def submit(name: str = Form(...), phone_number: str = Form(...)):
    try:
        user = User(name=name, phone_number=phone_number)
        # Save data to a database or file (for illustration, print it)
        print(f"User Data: {user.dict()}")
        return {"message": "Form submitted successfully!"}
    except Exception as e:
        return {"error": str(e)}

@app.post('/blog_create')
async def post_blog(Title, Body):
    
    return {"Title": Title, "Discription": Body}

@app.post('/blog_create')
async def post_blog(Title, Body):

    return {"Title": Title, "Discription": Body}