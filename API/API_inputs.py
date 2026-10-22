## How does an API receive input?

#  Query parameters : Values passed in the URL after ?

# http://127.0.0.1:8000/add?a=10&b=20
# ? starts the query parameters.
# & separates multiple parameters.
# a and b are the parameter names that match your function arguments.

from fastapi import FastAPI

app = FastAPI()

@app.get("/add")

def add_numbers(a:int,b:int):
    return a+b

# Path parameters 
@app.get("/square/{number}")

def square_number(number: int):
    return {"result" : number **2} 


# Request Body

# When you need to send data from a client (let's say, a browser)
# to your API, you send it as a request body.

# 2. FastAPI + Pydantic

# Checks required fields and validates types

from pydantic import BaseModel

class Employee(BaseModel):
    name: str
    age: int
    course: str

@app.post("/employees")
def create_employee(employee : Employee):
    return {
        "name": employee.name, 
        "age" : employee.age,
        "course" : employee.course
    
    }