list1 = []

print("Enter List items : " )
for i in range(1,8):
    n=int(input(f"Item {i} : "))
    list1.append(n)

print(list1)

Target = int(input("Enter your target to search : "))

count = 0
for i in list1:
    if i==Target:
        count += 1

print(f"Count of target in list1 : {count}")
