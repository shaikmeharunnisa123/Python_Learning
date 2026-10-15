P = int(input("Enter principle value : "))
R = int(input("Enter Interest rate : "))
T = int(input("Enter Time : "))

Total = P * pow((1+R/100),T)

print(f" Compound Interest {Total-P}")