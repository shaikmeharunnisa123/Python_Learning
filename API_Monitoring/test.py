import datetime
import uuid
import requests



API_URL = 'https://fakestoreapi.com/products/1'


def write_to_log(response):
    with open('C:/Users/MidhTech!/Desktop/Python/File_Exception_handling/logFile.txt','a') as file:
        currentTime = datetime.datetime.now()
        uniqueId = uuid.uuid4()
        endpoint = response.url
        method = response.request.method
        status_code = response.status_code
        elapsed_time = response.elapsed
        
        reason = response.reason
        file.write(f"\n[{currentTime}] - {uniqueId} : {method} - {status_code} - {reason} \n- {elapsed_time} -{endpoint}")

try:
    response = requests.get(API_URL)
except Exception as e:
    write_to_log(e)
else:
    write_to_log(response)

