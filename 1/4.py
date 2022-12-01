a = int(input("Введите сторону a "))
b = int(input("Введите сторону b "))
c = int(input("Введите сторону c "))
 
if a + b > c and a + c > b and b + c > a:
    print("Треугольник существует")
else:
    print("Треугольник не существует")