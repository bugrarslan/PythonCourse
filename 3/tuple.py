list = [1, 2, 3]

tuple = (1, "iki", 3)

print(type(list))
print(type(tuple))

print(list[2])
print(tuple[2])

print(len(list))
print(len(tuple))

list = ["Ali", "Veli"]
tuple = ("Damla", "Ayşe", "Ayşe")
names = ("Emel", "Demet", "Ayşe") + tuple

list[0] = "Ahmet"
# tuple[0] = "Deniz"
print(names)