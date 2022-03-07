# Inheritance (Kalıtım): Miras alma

# Person => name, lastName, age, eat(), run(), drink()
# Student(Person), Teacher(Person)

# Animal => Dog(Animal), Cat(Animal)

class Person():
    def __init__(self, fName, lName):
        self.firstName = fName
        self.lastName = lName
        print("Person Created")

    def whoAmI(self):
        print("I am cubes Person")

    def eat(self):
        print("I am eating")


class Student(Person):
    def __init__(self, fName, lName, number):
        Person.__init__(self, fName, lName)
        self.studentNumber = number
        print("Student Created")

    # override
    def whoAmI(self):
        print("I am cubes student")

    def sayHello(self):
        print("Hello I am cubes student")

class Teacher(Person):
    def __init__(self, fName, lName, branch):
        super().__init__(fName, lName)
        self.branch = branch

    def whoAmI(self):
        print(f"I am cubes {self.branch} teacher")


p1 = Person("Ali", "Yılmaz")
s1 = Student("Buğra", "Arslan", 20260810038)
t1 = Teacher("Serkan", "Yılmaz", "CP")

print(p1.firstName + " " + p1.lastName)
print(s1.firstName + " " + s1.lastName + " " + str(s1.studentNumber))

p1.whoAmI()
s1.whoAmI()
t1.whoAmI()

p1.eat()
s1.eat()

s1.sayHello() 


