
# 1- Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.

"""
number = float(input("Enter cubes number: "))

result = number > 0 and number < 100
"""

# 2- Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.

"""
result = number >= 0 and number % 2 == 0
"""

# 3- Email ve parola bilgileri ile giriş kontrolü yapınız.

"""
email = "asdasasdasasds"
password = "asdsasaasdsa"

isEmail = input("Enter email: ")
isPassword = input("Enter password: ")

result = isEmail == email and isPassword == password
"""

# 4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız.
"""
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
number3 = int(input("Enter third number: "))

result = (cubes > b) and (cubes > c)
print(f"cubes en büyük sayıdır: {result}")

result = (b > cubes) and (b > c)
print(f"b en büyük sayıdır: {result}")

result = (c > cubes) and (c > b)
print(f"c en büyük sayıdır: {result}")
"""


# 5- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
#    Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
#    cubes-) Ortalama 50 olsa bile final notu en az 50 olmalıdır.
#    b-) Finalden 70 alındığında ortalamanın önemi olmasın.
"""
visa1 = float(input("visa 1: "))
visa2 = float(input("visa 2: "))
final = float(input("final 3: "))

ort = (((visa1 + visa2) / 2 ) * 0.6) + (final * 0.4)

result = (ort > 50) and (final > 50)
result = (ort >= 50) or (final>=70)
print(f"Öğrencinin ortalaması: {ort} ve geçme durumu: {result}")
"""

# 6- Kişinin ad, kilo ve boy bilgilerini alıp indexlerini hesaplayınız.
#    Formül: (Kilo / boy uznkuğunun karesi)
#    Aşağıdaki tabloya göre kişi hangi gruba girmektedir?
#    0-18.4     => Zayıf
#    18.5-24.9  => Normal
#    25.0-29.9  => Fazla Kilolu
#    30.0-34.9  => Şişman (Obez)

"""
name = input("Adınız:")
kg = float(input("Kilonuz:"))
hg = float(input("boyunuz: "))

index = (kg) / (hg ** 2)
zayıf = (index >= 0 ) and (index <= 18.4)
normal = (index > 18.4) and (index <= 24.9)
kilolu = (index > 24.9) and (index <= 29.9)
obez = (index > 29.9) and (index <= 34.9)

print(f"{name} kilo indeksin: {index} ve kilo değerlendirmen zayıf: {zayıf}")
print(f"{name} kilo indeksin: {index} ve kilo değerlendirmen normal: {normal}")
print(f"{name} kilo indeksin: {index} ve kilo değerlendirmen kilolu: {kilolu}")
print(f"{name} kilo indeksin: {index} ve kilo değerlendirmen obez: {obez}")
"""

