from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Welcome to FastAPI!"}


@app.get("/hello")
def hello():
    return {"message": "Hello, Muhammad Zohaib!"}


@app.get("/square/{number}")
def square(number: int):
    return {
        "number": number,
        "square": number ** 2
    }