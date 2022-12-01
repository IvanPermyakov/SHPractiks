from functions import checkError

def CheckNature(num):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    if count == 2:
        print(f"Число {num} натуральное")
    elif count > 2:
        print(f"Число {num} не натуральное")

Check = True
num = 0
while Check:
    num = int(input("Введите число "))
    Check = checkError(num, 1, 1000)

CheckNature(num)
