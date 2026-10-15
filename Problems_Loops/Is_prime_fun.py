
print("PrimeNumber check ")
N = int(input("Enter a number : "))


def is_prime(N):
    flag = True
    for i in range(2,int(N/2) + 1):
        if(N % i == 0):
            flag = False
            break

    if (flag):
        print(f"{N} is a Prime number")

    else:
        print(f"{N} Not a prime number")

is_prime(N)