# An exception is an error that occurs 
# while a program is running and interrupts its normal execution.

try:
    num = int(input("Enter a number: "))
    print(100/num)

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Enter valid input")

print("Execution completed")