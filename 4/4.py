def print_digit(dig):
    """функция вывода образа одной цифры"""
    for line in dig:
        print(line)

def mappingIdxToDig(idx, digits):
    for i in idx:
        dig = digits[int(i)]
        print_digit(dig)

idx = input("Введите индекс ")

digits = {  # это словарь образов цифр
    0: ('XXX', 'X X', 'X X', 'X X', 'XXX'),
    1: ('  X', ' XX', '  X', '  X', '  X'),
    2: ('XXX', '  X', ' X ', 'X  ', 'XXX'),
    3: ('XXX', '  X', 'XXX', '  X', 'XXX'),
    4: ('X X', 'X X', 'XXX', '  X', '  X'),
    5: ('XXX', 'X  ', 'XXX', '  X', 'XXX'),
    6: ('XXX', 'X  ', 'XXX', 'X X', 'XXX'),
    7: ('XXX', '  X', ' XX', '  X', '  X'),
    8: ('XXX', 'X X', 'XXX', 'X X', 'XXX'),
    9: ('XXX', 'X X', 'XXX', '  X', 'XXX'),
}

mappingIdxToDig(idx, digits)