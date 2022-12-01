def checkParindrom(stroke):
    lenghtStr = round((len(stroke)-1)/2)
    for i in range(0, lenghtStr):
        if stroke[i] != stroke[len(stroke)-i-1]:
            return False
        else:
            return True

stroke = input("Введите строку ")
les=('.','?','!',':',';','-','—',' ')
backStroke = stroke.lower()
backStroke = "".join(symbol for symbol in backStroke if symbol not in les)

if checkParindrom(backStroke):
    print(stroke)
else:
    print("Строка не является палиндромом")

