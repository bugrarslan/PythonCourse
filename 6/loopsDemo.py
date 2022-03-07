# 1-100 arasında rastgele üretilecek bir sayıyı aşağı yukarı ifadeleri ile buldurmaya çalışın.
# ** "random modülü" için "python random" şeklinde arama yapın.
# ** 100 üzerinden puanlama yapın. her soru 20 puan.
# ** hak bilgisini kullanıcıdan alın ve her soru belirtilen can sayısı üzerinden hesaplansın.

import random

number = int(random.uniform(1, 10))
health = int(input("Hak sayısını giriniz: "))
enteredNumber = 1
sayac = 0

while health > 0:
    health -= 1
    sayac += 1
    
    enteredNumber = int(input("sayıyı giriniz: "))

    if (number > enteredNumber):
        print("yukarı!!!")
        print(f"Kalan Hak sayınız: {health}")
    elif(number < enteredNumber):
        print("aşağı!!!")
        print(f"Kalan Hak sayınız: {health}")
    else:
        print(f"Tebrikler!!! {sayac}. defada doğru sayıyı girdiniz. Toplam puanınız: {100 - ((100 / health) * (sayac - 1))}")
        break
    
    if health == 0:
        print(f"Hakkınız bitti. Tutulan sayı: {number}")
    
