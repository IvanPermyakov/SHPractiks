k = int(input("Введите число "))
if (k%10==0 or (k>=11 and k<20) or k%10 >=5):
    p = "ей"
elif (k%10==1):
    p = "ь"
else:
    p = "я"
print(f"{k} рубл{p}")

