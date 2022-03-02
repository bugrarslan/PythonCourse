# 1- Kulanıcıdan isim, yaş ve eğitim bilgilerini isteyip ehliyet alabilme
#    durumunu kontrol ediniz. Ehliyet alma koşulu en az 18 ve eğitim durumu
#    lise yada üniversite olmalıdır.

"""
name = input("isim: ")
age = int(input("yaş"))
educationalStatus = input("eğitim durumu: ")

if age < 18:
    print("yaş en az 18 olmalıdır")
else:
    if (educationalStatus == "lise" or educationalStatus == "üniversite"):
        print("ehliyet alınabilir")
    else:
        print("eğitim durumu lise yada üniversite olmalıdır")
"""

# 2- Bir öğencinin 2 yazılı bir sözlü notunu alıp hesaplanan ortalamaya göre
#    not aralığına karşılık gelen not bilgisini yazdırınız.

"""
exam1 = int(input("ilk sınav: "))
exam2 = int(input("2. sınav: "))
oExam = int(input("Sözlü sınav: "))

avr = (exam1 + exam2 + oExam) / 3

if 0 <= avr <= 24:
    print("0")
if 25 <= avr <= 44:
    print("1")
if 45 <= avr <= 54:
    print("2")
if 55 <= avr <= 69:
    print("3")
if 70 <= avr <= 84:
    print("4")
if 85 <= avr <= 100:
    print("5")
"""

# 3- Trafiğe çıkış tarihi alınan bir aracın servis zamanını aşağıdaki
#    bilgilere göre hesaplayınız.
#    1. Bakım => 1. yıl
#    2. Bakım => 2. yıl
#    3. Bakım => 3. yıl
#    ** Süre hesabını alınan gün, ay, yıl bilgisine göre gün bazlı hesaplayınız.
#    *** datetime modülünü kullanmanız gerekiyor.

"""
import datetime

date = input("aracınız hangi tarihte trafiğe çıktı (2021/11/23): ")
date.split("/")

firstDate = datetime.datetime(int(date[0], date[1], date[2]))
now = datetime.datetime.now()
division = now - firstDate
days = division.days




if days <= 365:
    print("1. Servis aralığı")
elif days > 365 and days<= 365*2:
    print("2. servis aralığı")
elif days > 365*2 and days <= 365*3:
    print("3. servis aralığı")
else:
    print("hatalı süre")
"""