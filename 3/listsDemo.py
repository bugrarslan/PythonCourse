# 1 "BMW, Mercedes, Opel, Mazda" elemanlarına sahip bir liste oluşturunuz.

cars = ["BMW", "Mercedes", "Opel", "Mazda"]

# 2 Liste kaç elemanlıdır?

print(len(cars))

# 3 Listenin ilk ve son elemanı nedir?

print(cars[0])
print(cars[-1])

# 4 Mazda Değerini Toyota ile değiştirin.

cars[-1] = "Toyota"

# 5 Mercedes listenin bir elemanı mıdır?

print("Mercedes" in cars)

# 6 Listenin -2 indeksindeki değer nedir?

print(cars[-2])

# 7 Listenin ilk 3 elemanını alın.

print(cars[:3])

# 8 Listenin son 2 elemanı yerine "Toyota" ve "Renault" Değerlerini ekleyin.

cars[-2:] = ["Toyota", "Renault"] 

# 9 Listenin üzerine "Audi" ve "Nissan" değerlerini ekleyin.

cars.append("Audi")
cars.append("Nissan")

# 10 Listenin son elemanı silin.

cars.pop(-1)

# 11 Liste elemanlarını tersten yazdırınız.

print(cars[::-1])

# 12 Aşağıdaki verileri bir liste içinde saklayınız.

        # studentA: Yiğit Bilgi 2010, (70,60,70)
        # studentB: Sena Turan 1999, (80,80,70)
        # studentC: Ahmet Turan 1998, (80,70,90)

studentA = ["Yiğit Bilgi", 2010, [70,60,70]]
studentB = ["Sena Turan", 1999, [80,80,70]]
studentC = ["Ahmet Turan", 1998, [80,70,90]]

students = [studentA, studentB, studentC]

# 13 Liste elemanlarını ekrana yazıdırınız.

print(students)
print(studentA[0])
print(studentB[1])
print(studentC[3][1])

