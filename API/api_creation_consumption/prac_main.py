from fastapi import FastAPI

app = FastAPI()

#Path parameter
@app.get("/employees/{employee_id}")
def get_employee(employee_id : int):
    return {
        "employee_id" : employee_id,
        "message" : "Employee deatils retrieved"
    }

# Query parameter

@app.get("/search")
def search_employee(name: str, age:int):
    return {
        "name" :name,
        "age": age
    }