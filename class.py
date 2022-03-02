# class

class Person:
    pass
    # class attributes
    address = "no information"

    # constructor(yapıcı metod)
    def __init__(self, name, year):
        # self ==> class tan türetilen p1, p2 gibi objeleri temsil eder
        # object attributes
        self.name = name
        self.year = year
        print("init metodu calistirildi")

        # methods


# object (instance)
p1 = Person(name = "Buğra",year = 2002)
p2 = Person(name = "Berkay",year = 2009)

# updating
p1.name = "Ahmet"
p1.address = "Tokat"

# accessing object attributes
print(f"p1: name: {p1.name} year: {p1.year} address: {p1.address}")
print(f"p2: name: {p2.name} year: {p2.year} address: {p2.address}")


print(p1)
print(p2)
print(type(p1))
print(type(p2))
print(p1 == p2)

