
print("======Calculator=========")

operator = input("Select the operation : + , - , * , / --->")
num1 = int(input("Enter number : "))
num2 = int(input("Enter number : "))

match operator:
    case "+":
        result = num1 + num2

    case "-":
        result = num1 - num2

    case "*":
        result = num1 * num2

    case "/":
        result = num1 / num2

print(result)