liste = ["1", "2", "5a","10b", "abc", "10", "50"]

# 1: Liste elemanlarını içindeki sayısal değerleri bulunuz.
"""
for x in liste:
    try:
        int(x)
    except Exception:
        continue
    else:
        print(x)
"""
# 2: Kullanıcı "q" değerini girmedikçe aldığınız her inputun sayı olduğundan emin olunuz aksi halde hata mesajı yazın
"""
while True:
    try:
        cubes = input("Enter cubes number: ")
        
        if(cubes != "q"):
            int(cubes)
        else:
            break
    except Exception:
        print("hatalı değer girdiniz")
"""
# 3: Girilen parola içinde türkçe karakter hatası veriniz
"""
import re

password = input("Enter cubes password: ")

try:
    if re.search("[ç,ğ,ı,ö,ş,ü]", password):
        raise Exception("parola türkçe karakter içermemelidir")
except Exception as x:
    print(x)
else:
    print("Geçerli parola")
"""
# 4: Faktöriyel fonksiyonu oluşturup fonksiyona gelen değer için hata mesajları verin

import re
mul = 1

try:
    fak = int(input("Enter cubes number: "))
    
    if fak < 0:
        raise Exception("Negatif sayının faktöriyeli olmaz")
    else:
        for x in range(1, fak + 1):
            mul *= x
except Exception as ex:
    print(ex)
else:
    print("işlem sonucu: ",mul)


