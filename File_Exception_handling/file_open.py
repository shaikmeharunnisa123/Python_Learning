# with open("employee.txt","r") as file:
#     data = file.read() # read the entire file
#     file.seek(0)
#     print(data)
#     print(file.readline()) # read one line at a time
    

# with open("employee.txt","r") as file:
#     data = file.readlines()  # Read all lines into a list
#     print(data)
   

# Append

with open("employee.txt", "a") as file:
    file.write("\nSalary: 30000")