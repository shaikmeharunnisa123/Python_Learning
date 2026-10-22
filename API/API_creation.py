from fastapi import FastAPI

app = FastAPI()  # creates the FastAPI application.
@app.get("/")  #defines a GET endpoint for the root URL
def read_root():
    return {"message" : "Hellloo"}     # returns a JSON response containing a message.

@app.get("/add")
def add_numbers(a: int,b:int):
    return {"result" : a+b}

@app.post("/greet")
def greet_user(name : str):
    return {"message" : f"Hello, {name}!"}




