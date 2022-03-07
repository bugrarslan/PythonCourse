maasAli = 5000
maasAhmet = 4000
vergi = 0.27

print(maasAli - (maasAli * vergi))
print(maasAhmet - (maasAhmet * vergi))

# Değişken tanımlama kuralları

#Rakam ile başlayamaz

number1 = 10
print(number1)
number1 = 20
print(number1)

number1 += 30
print(number1)

# Büyük küçük harf duyarlılığı

age = 20
AGE = 30

print(age)
print(AGE)

# Türkçe karakter kullanma

yas = 10
age = 20

x = 1                 #int
y = 2.3               #float
name = "Buğra"        #string
isStudent = True      #bool

x, y, name, isStudent = {2, 5.1, "Erdem", False}


a = "10"
b = "20"
print(a + b) # 30 => 1020

firstName = "Buğra"
lastName = " Arslan"

print(firstName + lastName) # Buğra Arslan