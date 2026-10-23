# Create and write to a file

file = open("employee.txt","r+")
file.write("Employee name: Mehar")

file.seek(0)
data = file.read()
print(data)
file.close()