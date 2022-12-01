def formStroke(x, y):
    stroke = ""
    for i in range(1, x + 1):
        for j in range(1, y + 1):
            stroke += str(i*j) + "\t"
        stroke += "\n"
    return stroke



x = int(input("Введите количество чисел по горизонтали "))
y = int(input("Введите количество чисел по вертикали "))
stroke = formStroke(x, y)
print(stroke)