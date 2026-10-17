import requests

url = "https://jsonplaceholder.typicode.com/posts"

def get_stock_data():

    payload = {"id":[1,2,3], "userId" : 1}
    
    response = requests.get(url, params = payload)
    
    if response.status_code == 200:
        data = response.json()

    return data
        
        


## POST request

# def post_stock_data():

#     data = {
         
#             "1. open": "230.6300",
#             "2. high": "231.8300",
#             "3. low": "230.6300",
#             "4. close": "231.8000",
#             "5. volume": "128"
#         }

#     response = requests.post(url,json = data)
#     print(response.json())
get_stock_data()


new_data = {
    "userId" : 10,
    "id" : 1,
    "title" : "POST request",
    "body" : "Created data"
}

post_response = requests.post(url,json = new_data)
print(post_response.json())