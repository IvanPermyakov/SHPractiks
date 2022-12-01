stroke = input("Введите строку ")
les=('а','у','е','ы','о','э','я','и','ю')
numGlas=0
for i in stroke:
    if i in les:
        numGlas += 1

if len(stroke)- numGlas > numGlas:
    print("Строка согласная")
else: 
    print("Строка гласная")