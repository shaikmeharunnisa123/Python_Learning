from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# defining the structure of Employee data
class Employee(BaseModel):
    name : str
    age : int
    course : str

@app.post("/employees")
def create_employee(employee: Employee): #tells FastAPI to validate the incoming JSON
                                            # using the Employee model.
    return {
        "message" : "Employee created succcessfully",
        "employee" : employee
    }
