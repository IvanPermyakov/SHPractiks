def reverseNum(num, num2):
    if num > num2:
        return num2, num
    else: 
        return num, num2

def checkError(num, Diap1, Diap2):
    if num > Diap2 or num < Diap1:
        print(f"Число должно быть в диапозоне от {Diap1} до {Diap2}")
        return True
    else:
        return False

def checkErrorForTwoNum(num, num2, Diap1, Diap2):
    if num > Diap2 or num2 > Diap2 or num < Diap1 or num2 < Diap1:
        print("Числа должны быть в диапозоне от 100 до -100")
        return True
    else:
        return False