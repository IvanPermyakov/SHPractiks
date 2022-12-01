import random

k = int(input("Введите число "))
spisok = []
for i in range(k):
    num = round(random.random() * 100)
    spisok.append(num)

print(spisok)