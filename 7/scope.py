# global scope
x = "global x"

def function(): 
    # local scope
    # x = "local x"
    print(x)

function()
print(x)


########################################
# global
name = "Buğra"

def changeName(newName):
    # local
    global name
    name = newName
    print(name)

changeName("Berkay")
print(name)

##########################################

name = "global string"

def greeting():
    # name = "Buğra"

    def hello():
        #name = "Berkay"
        print("Hello " + name)

    hello()

greeting()

##########################################

x = 50

def test():
    global x
    print(f"x = {x}")

    x = 100

    print(f"changed x to {x}")

test()

print(x)

