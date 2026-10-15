N = int(input("Enter Number :"))

for i in range(1,N+1):
    print(f" Cube of {i} = {i**3}")



List_num = [12,75,150,180,145,525,50]

for i in List_num:
    if(i > 500):
        break
    elif(i > 150):
        continue
    elif(i % 5 == 0):
        print(i)
    
    