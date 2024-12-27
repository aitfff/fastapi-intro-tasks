from fastapi import FastAPI, Body
from pydantic import BaseModel, EmailStr
from typing import Optional

app = FastAPI()

# BEGIN (write your solution here)
class User(BaseModel):
    username: str
    email: EmailStr
    age: Optional[int] = None

@app.post("/users")
def create_user(user: User):
    response = {
        "username": user.username,
        "email": user.email,
        "age": user.age,
        "status": "User created"
    }
    
    return response
# END
