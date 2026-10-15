Input_str = "Aoops are Fun!"
vowel_count = 0
consonant_count = 0
for i in Input_str:
    i=i.lower()
    if i.isalpha():
        if i in ['a','e','i','o','u']:
            vowel_count += 1
        else:
            consonant_count +=1 

print("Vowel count : ",vowel_count)
print("Consonant count : ",consonant_count)

