import json

person_string = '{"name": "Ali", "languages": ["Python", "C#"]}'
personDict = {"name": "Ali", "Languages": ["Python", "C#"]}

# JSON string to Dict

# result = json.loads(person_string)
# print(type(result))

# result = result["name"]
# result = result["languages"]

# with open("person.json") as f:
#     data = json.load(f)
#     print(data["name"])
#     print(data["languages"])

# print(result)

# Dict to JSON string

# result = json.dumps(personDict)
# print(result)
# print(type(result))

# with open("person.json", "w") as f:
#     json.dump(personDict, f)

personDict1 = json.loads(person_string)

result = json.dumps(personDict1, indent=4, sort_keys=True)

print(result)
print(personDict1)
