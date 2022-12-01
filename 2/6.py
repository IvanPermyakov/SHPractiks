from functions import reverseNum, checkErrorForTwoNum

def printNum(num, num2):
    for i in range(num, num2):
        for j in range(1, i):
            if i % j == 0 and j != 1 and j != i:
                list.append(j)
        if len(list) == 2:
            print(i, list)
            list.clear()
        else:
            list.clear()



Check = True
num = 0
list = []
while Check:
    num = int(input("Введите число "))
    num2 = int(input("Введите число "))
    Check = checkErrorForTwoNum(num, num2, 1, 2000)

num, num2 = reverseNum(num, num2)
printNum(num,num2)