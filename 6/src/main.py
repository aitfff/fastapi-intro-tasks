from fastapi import FastAPI, Form
from fastapi.responses import JSONResponse

app = FastAPI()

# BEGIN (write your solution here)
@app.post("/login")
async def login(username: str = Form(...), password: str = Form(...)):
    return JSONResponse(content={
        "username": username,
        "password": password,
        "status": "Login successful"
    })
# END
