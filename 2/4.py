from functions import checkError

Check = True
num = 0
while Check:
    num = int(input("Введите число "))
    Check = checkError(num, 1, 9)

for i in range(num+1):
    for j in range(i):
        print(i, end="")
    print("")