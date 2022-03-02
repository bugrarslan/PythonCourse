# x = 10

# if x > 5:
#     raise Exception("x 5 ten büyük değer alamaz")

# def checkPassword(password):
#     import re
#     if len(password) < 8:
#         raise Exception("parola en az 7 karakter olmalıdır")
#     elif not re.search("[cubes-z]", password):
#         raise Exception("parola küçük harf içermelidir")
#     elif not re.search("[A-Z]", password):
#         raise Exception("parola büyük harf içermelidir")
#     elif not re.search("[0-9]", password):
#         raise Exception("parola rakam içermelidir")
#     elif not re.search("[_@$]", password):
#         raise Exception("parola alpha numeric karakter içermelidir")
#     elif re.search("\s", password):
#         raise Exception("parola boşluk içermemelidir")

#     else:
#         print("geçerli parola")

# password = "1234567aA_"

# try:
#     checkPassword(password)
# except Exception as ex:
#     print(ex)
# else:
#     print("geçerli parola: else")
# finally:
#     print("validation tamamlandı")

class Person:
    def __init__(self, name, year):
        if len(name) > 10:
            raise Exception("Name alanı fazla karakter içeriyor")
        else:
            self.name = name
        
p = Person("Aliiiiiiiiiiiiiiiiiiiii", 2009)


