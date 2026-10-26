import datetime
import uuid
import requests



API_URL = 'https://fakestoreapi.com/products/1'


def write_to_log(info):
    with open('C:/Users/MidhTech!/Desktop/Python/File_Exception_handling/logFile.txt','a') as file:
        currentTime = datetime.datetime.now()
        uniqueId = uuid.uuid4()
        endpoint = info.url
        method = info.request.method
        status_code = info.status_code
        elapsed_time = info.elapsed
        headers = info.headers
        reason = info.reason
        file.write(f"\n[{currentTime}] - {uniqueId} \n : {method} - {status_code} - {reason} \n- {elapsed_time} -{endpoint} - \n{headers}\n ")

try:
    response = requests.get(API_URL)
except Exception as e:
    write_to_log(e)
else:
    write_to_log(response)

