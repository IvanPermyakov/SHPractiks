from functions import checkError

def CheckPerfect(num):
    count = 0
    for i in range(1, num):
        if num % i == 0:
            count += i
    if count == num:
        print(f"Число {num} совершенное")
    elif count != num:
        print(f"Число {num} не совершенное")

Check = True
num = 0
while Check:
    num = int(input("Введите число "))
    Check = checkError(num, 1, 1000)

CheckPerfect(num)
