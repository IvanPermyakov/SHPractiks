import math

def lenghtCircle(R):
    return 2 * math.pi * R

def Square(R):
    return math.pi * R * R

R = int(input("Введите радиус окружности "))
L = lenghtCircle(R)
S = Square(R)
print(f"Длина круга = {round(L)} Площадь круга = {round(S)}")
    