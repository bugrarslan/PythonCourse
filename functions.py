def sayHello(name = "user"): # define
    return "Hello " + name

message = sayHello("Buğra")
print(message)

def total(num1, num2):
    return num1 + num2

result = total(10,20)
print(result)

def yasHesapla(bornYear):
    return 2021 - bornYear

ageBugra = yasHesapla(2002)
ageBerkay = yasHesapla(2009)
ageSevgi = yasHesapla(1978)

print(ageBugra, ageBerkay, ageSevgi)

def howMuchToRetirement(bornYear, name):
    """
    DOCSTRING: Dogum yiliniza gore emekliliginize kac yil kaldi
    INPUT: Dogum Yili
    OUTPUT: Hesaplanan yil bilgisi
    """
    age = yasHesapla(bornYear)
    retirement = 65 - age

    if retirement > 0:
        print(f"emekliliğinize {retirement} yıl kaldı")
    else:
        print(f"zaten emekli oldunuz")

howMuchToRetirement(2002, "Buğra")
howMuchToRetirement(2009, "Berkay")
howMuchToRetirement(1976, "Sevgi")
        
print(help(howMuchToRetirement))

list = [1,2,3]

print(help(list.append))



