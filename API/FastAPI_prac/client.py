import requests
url = "http://127.0.0.1:8000/employees"
payload = {
    "name" : "Mehar",
    "age" : 21,
    "course" : "Python"
}

response = requests.post(url,json = payload)
print(response.status_code)
print(response.json())