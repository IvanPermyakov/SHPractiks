num = int(input("Введите число "))
num2 = int(input("Введите число 2 "))
num3 = int(input("Введите число 3 "))
if num < num2 and num < num3:
    print(num)
elif num2 < num and num2 < num3:
    print(num2)
else: 
    print(num3)