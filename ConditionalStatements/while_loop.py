
#====WHILE LOOP=====
#We use loops to execute a block of code repeatedly.
# A while loop repeats a block of code as long as its condition is True.

# i = 1

# while i <= 5:
#     print("Hello")
#     i = i + 1

#Execution flow:

# i = 1 — initialize the counter.

# i <= 5 — check the condition.

# print("Hello") — execute the statement.

# i = i + 1 — increase the counter by 1. We can increment or decrement the "i" value

# Repeat until the condition becomes false.

#==INFINITE LOOP==
# Without incrementing i, the condition remains true forever, and the loop may run indefinitely. This is called an infinite loop.

i = 1

while i <= 3:
    print(i,end = "")
    j = 1
    while j <= 4:
        print(j, end = "") # The argument end=" " adds a space instead of starting a new line after each print.
        j = j + 1

    i = i + 1   
    print()  #When we want to repeat one task inside another repeated task, we use nested loops. 
                 