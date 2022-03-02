# # class

# class Person:
#     pass
#     # class attributes
#     address = "no information"
#     # constructor(yapıcı metod)
#     def __init__(self, name, year): # self ==> class tan türetilen p1, p2 gibi objeleri temsil eder
#         # object attributes
#         self.name = name
#         self.year = year

#     # instance methods
#     def intro(self):
#         print("Hello there. I am " + self.name)
    
#     # instance methods
#     def calculateAge(self):
#         return 2021 - self.year

# # object (instance)
# p1 = Person(name = "Buğra",year = 2002)
# p2 = Person(name = "Berkay",year = 2009)


# p1.intro()
# p2.intro()

# print(f"adım {p1.name} ve yaşım {p1.calculateAge()}")
# print(f"adım {p2.name} ve yaşım {p2.calculateAge()}")

class Circle:
    # Class object attribute
    pi = 3.14

    def __init__(self, yaricap = 1):
        self.yaricap = yaricap

    # Methods
    def CevreHesapla(self):
        return 2*self.pi*self.yaricap

    # Methods
    def AlanHEsapla(self):
        return self.pi*(self.yaricap**2)

c1 = Circle() # yaricap = 1
c2 = Circle(5)

print(f"c1 : alan = {c1.AlanHEsapla()} çevre : {c1.CevreHesapla()}")
print(f"c2 : alan = {c2.AlanHEsapla()} çevre : {c2.CevreHesapla()}")


