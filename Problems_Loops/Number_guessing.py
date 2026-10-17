import random

start = 1
end  = 100

Random_num = random.randint(start,end)


print("** NUMBER GUESSING GAME **")

print()

while True:

    N_input = int(input("Guess the number : "))

    if (N_input > 100 or N_input < 1):
        print(f"Please enter number in the range {start} - {end}")

    else:

        if N_input == Random_num:
            print(f"You won ! Guesses number is {N_input}")
            break

        elif(N_input > Random_num):
            print("Too High !!")

        elif(N_input <  Random_num):
            print("Too Low !!")

    
