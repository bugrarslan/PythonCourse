website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

length2 = len(website)
length = len(course)

print(length)

print(website[7:10])

print(website[22:25])

print(course[:15],"\n", course[51:])

print(course[::-1])

name, surname, age, job = "Buğra", "Arslan", 19, "Mühendis"

print(f"Benim adım {name} {surname}, yaşım {age} ve mesleğim {job}.")

greeting = "Hello world"

greeting = greeting[:6] + "W" + greeting[7:] # greeting.replace("w", "W")

print(greeting)

variable = "abc"

print(variable * 3)
