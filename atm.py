#bankamatik uygulaması

BugraHesap = {
    "ad": "Buğra Arslan",
    "hesapNo": "12345678",
    "bakiye": 3000,
    "ekHesap": 2000
}

BerkayHesap = {
    "ad": "Berkay Arslan",
    "hesapNo": "12345678",
    "bakiye": 2000,
    "ekHesap": 1000
}

def paraCek(hesap, miktar):
    print(f"Merhaba {hesap['ad']}")

    if hesap["bakiye"] >= miktar:
        hesap["bakiye"] -= miktar 
        print("paranızı alabilirsiniz")
        bakiyeSorgula(BugraHesap)
    else:
        toplam = hesap["bakiye"] + hesap["ekHesap"]

        if toplam >= miktar:
            ekHesapKullanimi = input("ek hesap kullnılsın mı? (e/h)")

            if ekHesapKullanimi == "e":

                ekHesapKullanılacakMiktar = miktar - hesap["bakiye"]
                hesap["bakiye"] = 0
                hesap["ekHesap"] -= ekHesapKullanılacakMiktar

                print("paranızı alabilirsiniz")
                bakiyeSorgula(BugraHesap)
            else:
                print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} bakiye bulunmaktadır")
        else:
            print("Üzgünüz bakiyeniz yetersiz")
            bakiyeSorgula(BugraHesap)


def bakiyeSorgula(hesap):
    print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} TL ve ek hesap limitiniz ise {hesap['ekHesap']}")

paraCek(BugraHesap, 3000)
paraCek(BugraHesap, 2000)




