import requests
url = "https://fakestoreapi.com/products"

params = {
    "limit" : 5,
    "sort" : "asc",
  
}

response = requests.get(url,params = params)
products = response.json()
# print(products)

for product in products:
    print(f" Product Id : {product["id"]} \n Title : {product["title"]} \n Price : {product["price"]}")
    print()