import math
def Disc(a, b, c):
    D = b**2 - 4 * a * c
    if D > 0:
        x1 = -b + math.sqrt(D) / 2*a
        x2 = -b - math.sqrt(D) / 2*a
        print(f"x1 = {x1}")
        print(f"x2 = {x2}")
    elif D < 0:
        print("Корней нет")
    else:
        x1 = -b / 2*a
        print(f"x1 = {x1}")


a = int(input("Введите первый коэффициент "))
b = int(input("Введите второй коэффициент "))
c = int(input("Введите третий коэффициент "))
Disc(a, b, c)



