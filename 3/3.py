x = int(input("Введите число "))

for i in range(x):
    print(str(' ' * (x-i-1)) + str('*' * (i*2+1)))
    print()