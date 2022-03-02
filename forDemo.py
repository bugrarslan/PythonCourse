numbers = [1, 3, 5, 7, 9, 12, 19, 21]

# 1- Sayilar listesindeki hangi sayılar 3'ün katıdır ?

"""
for i in numbers:
    if (i % 3 == 0):
        print(i)
"""

# 2- Sayilar listesindeki sayıların toplamı kaçtır?

"""
sum = 0
for i in numbers:
    sum += i

print(sum)
"""

# 3- Sayılar listesindeki tek sayıların karesini alınız.

"""
for i in numbers:
    if(i % 2 != 0):
        print(i**2)
"""

cities = ["Kocaeli", "İstanbul", "Ankara", "İzmir", "Rize"]

# 4- Şehirlerden hangileri en fazla 5 karakterlidir?

"""
for i in cities:
    if (len(i) <= 5):
        print(i)
    
            
"""
products = [
    {"name": "samsung S6", "price": "3000"},
    {"name": "samsung S7", "price": "4000"},
    {"name": "samsung S8", "price": "5000"},
    {"name": "samsung S9", "price": "6000"},
    {"name": "samsung S10", "price": "7000"}
]

# 5- Ürünlerin fiyatları toplamı nedir?

"""
sum = 0
for product in products:
    price = int(product["price"])
    sum += price

print("toplam ürün fiyatı: ",sum)
"""

# 6- Ürünlerden fiyatı en fazla 5000 olan ürünleri gösteriniz.

"""
for product in products:
    if(int(product["price"]) <= 5000):
        print(product["name"])
"""

