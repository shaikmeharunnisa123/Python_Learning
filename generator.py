# Generators are functions that can pause and resume their execution.

# yield --> When yield is encountered, the function's state is saved,and the value is returned.


def generate_num(n):
    for i in range(n):
        yield i

gen = generate_num(100)

print(next(gen))
print(next(gen))
print(next(gen))