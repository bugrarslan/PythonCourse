"""
Soru: Girilen bir sayının asal olup olmadığını bulun.
** Asal Sayı 1 ve kendisi hariç tam böleni olmayan sayılara denir.
"""

number = int(input("Sayıyı girin: "))

for i in range(2, number):
    if number % i == 0:
        result = True
        break
    else:
        result = False

if result == True:
    print(f"{number} bir asal sayı değildir")

else:
    print(f"{number} bir asal sayıdır")

