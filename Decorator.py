# Let you add extra behaviour to a function, without changing the function code.

def decorator(func):
    def wrapper():
        print("Before calling the function.")
        func()
        print("After calling the function")

    return wrapper

@decorator
def greet():
    print("Hello, World!")
greet()