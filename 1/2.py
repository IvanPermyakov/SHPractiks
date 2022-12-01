num = int(input("Введите число "))
num2 = int(input("Введите число 2 "))
if num % num2 == 0:
    print(f"{num} кратное {num2}")
else:
    print(f"{num} некратное {num2}")