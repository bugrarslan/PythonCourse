numbers = [1,3,5,7,9,12,19,21]

# 1- sayılar listesini while ile ekrana yazdırın

"""
i = 0
while (1 < len(numbers)):

    print(numbers[i])
    i += 1
"""

# 2- Başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm tek sayıları ekrana yazdırın

"""
start = int(input("Başlangıç: "))
finish = int(input("Bitiş: "))

i = start
while start < finish:
    i += 1
    if(i%2 == 0):
        print(i)
"""

# 3- 1-100 arasındaki sayıları azalan şekilde yazdırın.

"""
i = 100

while i >= 0:
    print(i)
    i -= 1
"""

# 4- Kullanıcıdan alacağınız 5 sayıyı ekrana sıralı bir şekilde yazdırın.

"""
numbers = []

i = 0

while i < 5:
    number = int(input("sayı: "))
    numbers.append(number)
    i += 1

print(numbers.sort())
"""

# 5- Kullanıcıdan alacağınız sınırsız ürün bilgisini ürünler listesi içinde saklayın.
#    ** ürün sayısını kullanıcıya sorun
#    ** dictionary listesi yapısı (name, price) şeklinde olsun
#    ** ürün ekleme işi bittiğinde ürünleri ekrana while ile listeleyin.

"""
products = []

count = int(input("kaç adet ürün eklemek istiyorsunuz: "))
i = 0

while(i<count):
    name = input("ürün ismi: ")
    price = input("ürün fiyatı: ")
    products.append({
        "name": name,
        "price": price
    })
    i += 1

for product in products:
    print(f"ürün adı: {product['name']} ürün fiyatı: {product['price']}")
"""