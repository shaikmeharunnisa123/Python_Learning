import datetime
import uuid

def division(num):
    print(f" 100 divided by {num} : {100/num}")

def printAge(age):
    print(f"Age: {age}")

def openFile():
    with open("demofil.txt","r") as file:
        data = file.read()
        print(data)

def writeToLogfile(exe):
    with open("logFile.txt","a") as LogFile:
        currentTime = datetime.datetime.now()
        uniqueId = uuid.uuid4()
        LogFile.write(f"\n[{currentTime}] - {uniqueId} : {exe}")

try:
    n=int(input("Enter number : "))
    division(n)

except ZeroDivisionError as ZDE:
    writeToLogfile(ZDE)

except ValueError as VE:
    writeToLogfile(VE)

try:
    age =int(input("Enter Age: "))
    printAge(age)

except NameError as NE:
    writeToLogfile(NE)

except ValueError as VE:
    writeToLogfile(VE)

 
try:
    openFile()

except FileNotFoundError as FNF:
            writeToLogfile(FNF)
        











    
    
