names = ["Ali", "Yağmur", "Hakan", "Deniz"]
years = [1998, 2000, 1998, 1987]

# 1 "Cenk" ismini listenin sonuna ekleyiniz.

names.append("Cenk")

# 2 "Sena" değerini listenin başına ekleyiniz.

names.insert(0, "Sena")

# 3 "Deniz" ismini listeden siliniz.

names.pop(-2)

# 4 "Deniz" isminin indeksi nedir?

print(names.count("Deniz"))

# 5 "Ali" listenin bir elemanı mıdır?

result = "Ali" in names
print(result)

# 6 Liste elemanlarını ters çevirin

names.reverse()

# 7 Liste elemanlarını alfabetik olarak sıralayınız.

names.sort()

# 8 years listesini rakamsal büyüklüğe göre sıralayınız.

years.sort()

# 9 str = "Chevrolet,Dacia" karakter dizisini listeye çeviriniz.

str = "Chevrolet,Dacia"
str.split(",")

# 10 years dizisinin en büyük ve en küçük elemanı nedir?

print(max(years))
print(min(years))

# 11 years dizisinde kaç tane 1998 değeri vardır?

years.count(1998)

# 12 years dizisinin tüm elemanlarını siliniz.

years.clear()

# 13 Kullanıcıdan alacağınız 3 tane marka bilgisini bir listede bir listede saklayınız.

a = input("Marka girin: ")
b = input("Marka girin: ")
c = input("Marka girin: ")

brands = [a, b, c]

print(str)

print(names)
