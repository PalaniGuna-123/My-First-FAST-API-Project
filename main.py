from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "This is my first FastAPI application!"}

@app.get("/name")
def read_name():
    return {"message": "My name is FastAPI!"}