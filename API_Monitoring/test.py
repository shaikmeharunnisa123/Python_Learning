import datetime
import uuid
import requests



API_URL = 'https://fakestoreapi.com/products/1'
log_file = ('C:/Users/MidhTech!/Desktop/Python/File_Exception_handling/logFile.txt')

def write_to_log(response=None, error=None):
    with open(log_file,'a') as file:
        currentTime = datetime.datetime.now()
        uniqueId = uuid.uuid4()
        file.write("\n"+"="*60)
        file.write(f"\nTime : {currentTime}\n")
        file.write(f"Unique ID : {uniqueId}\n")

        if response is not None:
            endpoint = response.url
            method = response.request.method
        elif error is not None and error.request is not None:
            endpoint = error.request.url
            method = error.request.method

        else:
            endpoint = API_URL

        file.write(f"Endpoint : {endpoint}\n")
        file.write(f"Method : {method}\n")
        
        if error is not None:
            file.write(f"Error details : {error}\n")
            if error.response is not None:
                file.write(f"Status code : {error.response.status_code}")

        elif response is not None:
            file.write(f"Status code: {response.status_code}\n")
            file.write(f"Reason : {response.reason}\n")
            file.write(f"Elapsed Time : {response.elapsed}\n")

        
        
        
try:
    response = requests.get(API_URL)
    response.raise_for_status()
  
except requests.RequestException as e:
    write_to_log(error = e)
   
else:
    write_to_log(response =response)

