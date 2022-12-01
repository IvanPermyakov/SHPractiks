import random

spisok = {}
for i in range(4):
    Check = True
    num = round(random.random() * 10)
    while num in spisok:
        num = round(random.random() * 10)
    spisok[i] = num
    


print(spisok)