import requests

base_url = "http://127.0.0.1:8000"

response = requests.get(f"{base_url}/employees/101")
print(response.json())

response = requests.get(f"{base_url}/search", params = {"name": "Mehar","age":21})

print(response.json())

