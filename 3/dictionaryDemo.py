"""
students = {
    "120": {
        "name": "Ali",
        "surname": "Yılmaz",
        "phone": "532 000 00 01"
    },
    "125": {
        "name": "Can",
        "surname": "Korkmaz",
        "phone": "532 000 00 02"
    },
    "128": {
        "name": "Volkan",
        "surname": "yükselen",
        "phone": "532 000 00 03"
    }
}

1- Bilgileri verilen öğrencileri kullanıcıdan aldığınız bilgilerle dictionary içinde saklayınız.
2- Öğrenci numarasını kullanıcıdan alıp ilgili öğrenci bilgisini gösterin
"""

students = {}

studentNumber = input("Öğrenci numarasını girin: ")
name = input("Öğrencinin adını girin: ")
surname = input("Öğrencinin soyadını girin: ")
phone = input("Öğrencinin numarasını girin: ")

students.update({
    studentNumber: {
        "name" : name,
        "surname" : surname,
        "phone" : phone
    }
})

studentNumber = input("Öğrenci numarasını girin: ")
name = input("Öğrencinin adını girin: ")
surname = input("Öğrencinin soyadını girin: ")
phone = input("Öğrencinin numarasını girin: ")

students.update({
    studentNumber: {
        "name" : name,
        "surname" : surname,
        "phone" : phone
    }
})

studentNumber = input("Öğrenci numarasını girin: ")
name = input("Öğrencinin adını girin: ")
surname = input("Öğrencinin soyadını girin: ")
phone = input("Öğrencinin numarasını girin: ")

students.update({
    studentNumber: {
        "name" : name,
        "surname" : surname,
        "phone" : phone
    }
})

print(students)

search = input("Aranacak öğrenci numarasını girin: ")

print(f"aradığınız öğrencinin öğr. numarası: {students[search][studentNumber]}, adı: {students[search][name]}, soyadı: {students[search][surname]}, telefon numarası: {students[search][phone]}")
