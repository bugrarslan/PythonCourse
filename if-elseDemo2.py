# 1- Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.

"""
number = float(input("sayı: "))
if (number > 0) and (number <= 100):
    print(f"{number} 0-100 arasındadır")
else:
    print(f"{number} 0-100 arasında değildir")

"""

# 2- Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.

"""
number = int(input("sayı: "))
if (number > 0) and (number % 2 == 0):
    print(f"{number} pozitif çift sayıdır")
else:
    print(f"{number} pozitif çift sayı değildir")

"""

# 3- Email ve parola bilgileri ile giriş kontrolü yapınız.

"""
email = "bgra.arsln@hotmail.com"
password = "12345"

enteredEmail = input("email: ")
enteredPassword = input("şifre: ")

if (enteredEmail == email) and (enteredPassword == password):
    print("Hoş geldiniz")
else:
    print("Giriş bilgileriniz yanlış. Lütfen tekrar deneyiniz.")
"""

# 4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız.

"""
number1 = int(input("1. sayı: "))
number2 = int(input("2. sayı: "))
number3 = int(input("3. sayı: "))

max = number1

if (number2 > max):
    number2 = max
elif (number3 > max):
    number3 = max

print(f"en büyük sayı: {max}")
"""

# 5- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
#    Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
#    cubes-) Ortalama 50 olsa bile final notu en az 50 olmalıdır.
#    b-) Finalden 70 alındığında ortalamanın önemi olmasın.

"""
visa1 = float(input("visa 1: "))
visa2 = float(input("visa 2: "))
final = float(input("final 3: "))

avg = (((visa1 + visa2) / 2 ) * 0.6) + (final * 0.4)

if (avg >= 50 and final >= 50):
    print("Geçti")
elif (final >= 70):
    print("Geçti")
else:
    print("Kaldı")
"""

# 6- Kişinin ad, kilo ve boy bilgilerini alıp indexlerini hesaplayınız.
#    Formül: (Kilo / boy uznkuğunun karesi)
#    Aşağıdaki tabloya göre kişi hangi gruba girmektedir?
#    0-18.4     => Zayıf
#    18.5-24.9  => Normal
#    25.0-29.9  => Fazla Kilolu
#    30.0-45.9  => Şişman (Obez)

""""""
name = input("Adınız:")
kg = float(input("Kilonuz:"))
hg = float(input("boyunuz: "))

index = (kg) / (hg ** 2)
if (index >= 0 ) and (index <= 18.4):
    print(f"{name} isimli kişinin bki sonucu: zayıf")
elif (index > 18.4) and (index <= 24.9):
    print(f"{name} isimli kişinin bki sonucu: normal")
elif (index > 24.9) and (index <= 29.9):
    print(f"{name} isimli kişinin bki sonucu: fazla kilolu")
elif (index > 29.9) and (index <= 45.9):
    print(f"{name} isimli kişinin bki sonucu: Obez")
else:
    print("Bilgileriniz yanlış")
