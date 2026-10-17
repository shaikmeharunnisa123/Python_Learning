# Constraints 

# -->Must be below 12 characters
# -->Must be without spaces
# -->Should not contain integers


userName = input("Enter user name: ")
flag = True

if (len(userName) > 12):
    print("Usename should not exceed 12 characters")
elif(not userName.isalpha()):
    print("Username should not contain numbers and spaces")
else:
    print(f"Username {userName} is valid.")
    
