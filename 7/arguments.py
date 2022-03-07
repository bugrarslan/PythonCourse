# def changeName(n):
#     n = "Berkay"

# name = "Buğra"

# changeName(name)
# print(name)

# def change(n):
#     n[0] = "Istanbul"

# cities = ["Ankara", "İzmir"]
# n = cities[:] # Slicing

# change(cities[:])

# n[0] = "İstanbul"

# print(cities)

def add(*params):
    print(type(params))
    sum = 0

    for i in params:
        sum += i
    return sum

print(add(10, 20, 50))
print(add(10, 20, 30))
print(add(10, 20, 30, 40, 50))

def displayUser(**args):
    print(type(args))
    for key, value in args.items():
        print("{} is {}".format(key, value))

displayUser(name = "Bugra", age = 19, city = "Nevşehir")
displayUser(name = "Berkay", age = 12, city = "İstanbul", phone = "12312313")
displayUser(name = "Sevgi", age = 43, city = "Tokat", phone = "12312131231", email = "asdasaadsa@mail")

def myFunc(a, b, c, *args, **kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)

myFunc(10, 20, 30, 40, 50, 50, 70, key1 = "value 1", key2 = "value 2")

