data = {
    "name": "Lahari",
     "age" : 21,
     "department" : "development"
}

print(data)
print(data.items())
print(data.keys())
print(data.values())

data.update({"Emp_type":"full time"})
print(data)

print(data.pop("name"))
print(data.popitem())
print(data)