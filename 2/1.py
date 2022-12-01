from functions import reverseNum, checkErrorForTwoNum

num = int(input("Введите первое число "))
num2 = int(input("Введите второе число "))

checkErrorForTwoNum(num, num2, -100, 100)

num, num2 = reverseNum(num, num2)

for i in range(num, num2 + 1):
    print(i)