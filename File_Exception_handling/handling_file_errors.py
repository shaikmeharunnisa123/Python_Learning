

# The try block lets you test a block of code for errors.

# The except block lets you handle the error.

# The else block lets you execute code when there is no error.

# The finally block lets you execute code, regardless of the result of the try- and except blocks.




try:
    with open("employee.txt","r") as file:
        data = file.read()
        print(data)
        print()

except FileNotFoundError:
    print("File doesn't exists")


try:
    x=10
    print(x)  # The try block will generate an exception, because x is not defined

except NameError:
    print("Variable is not defined")

else:           # This is a block of code to be executed if no errors were raised
    print("Nothing went wrong")


# Trying to open and write to a file that is not writable:
try:
    f = open("demofile.txt")
    try:
        f.write("Exception handling")
    except:
        print("Cannot write to file")
    finally:
        f.close()
except:
    print("Cannot open file")

else:
    print("open file operation completed withot any error")