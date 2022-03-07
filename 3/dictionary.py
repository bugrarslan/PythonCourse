""" 
# key -  value

# 41 => Kocaeli 34 => İstanbul

sehirler = ["Kocaeli", "İstanbul"]
plakalar = [41, 34]

print(plakalar[sehirler.index("Kocaeli")])
print(plakalar[sehirler.index("İstanbul")])

# print(plakalar["Kocaeli"]) => 41
# print(plakalar["İstanbul"]) => 34

plakalar = { "Kocaeli" : 41, "İstanbul" : 34 }

print(plakalar["İstanbul"])
print(plakalar["Kocaeli"])

plakalar["Ankara"] = 6
plakalar["Kocaeli"] = "new value"
print(plakalar)
"""
users = {
    "bugraArslan": {
        "age": 19,
        "roles": ["admin","user"],
        "email": "bgra.arsln@hotmail.com",
        "address": "Nevşehir",
        "phone": "313123131321"
    },
    "berkayArslan": {
        "age": 13,
        "roles": ["user"],
        "email": "brkay.arsln@hotmail.com",
        "address": "İstanbul",
        "phone": "313123131321"
    }
}

print(users["berkayArslan"]["age"])
print(users["berkayArslan"]["roles"])
print(users["berkayArslan"]["email"])
print(users["berkayArslan"]["address"])
print(users["berkayArslan"]["phone"])

print(users["bugraArslan"]["age"])
print(users["bugraArslan"]["roles"])
print(users["bugraArslan"]["email"])
print(users["bugraArslan"]["address"])
print(users["bugraArslan"]["phone"])

