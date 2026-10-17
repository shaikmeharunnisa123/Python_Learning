# Logical Operators -- and , or , not

# Predicting Weather

temperature = int(input("Enter the present temperature: "))
is_raining = input("Is it raining ? (Y/N) : ")

if (temperature > 35 or temperature < 0 or is_raining == 'y' ):
    print("Don't go out")
elif is_raining == 'n':
    print("Clear weather")

else:
    print("invalid Inputs")