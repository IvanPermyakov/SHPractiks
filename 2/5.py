from functions import checkError

Check = True
num = 0
while Check:
    num = int(input("Введите число "))
    Check = checkError(num, 1, 9)

for i in range(num):
    for j in range(num):
        print(num, end="")
    print("")