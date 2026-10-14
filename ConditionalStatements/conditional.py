

#============Conditional Statements============

# Conditional statements help a program make decisions based on whether a condition is True or False.

x = 7

if x % 2 == 0:
    print("Even")
else:                 #We use else when we want to execute another block if the if condition is false
    print("Odd")

#   NESTED IF
#we need to check another condition only after the first condition is true. An if inside another if is called a nested if.

x = 8

if x % 2 == 0:
    print("Even")

    if x > 5:
        print("Greater than 5")

# ELIF
#We could use multiple if statements, but Python would check each independent if condition.
# Instead, we can use elif to check another condition only if the previous condition was false.

x = 3

if x == 1:
    print("One")
elif x == 2:
    print("Two")
elif x == 3:
    print("Three")
elif x == 4:
    print("Four")
else:
    print("Wrong input")


#======SUMMARY======

# What?   Why do we use it?                  How does it work?

# if      To check a condition               Executes when the condition is true

# else    To handle the alternative           Executes when the if condition is false

# elif    To check multiple possibilities     Checks the next condition if previous ones are false

# Nested if   To check dependent conditions   Checks an inner condition inside an outer block




