# import json
# print(json.__file__)  # shows module path

import requests
import json

result = requests.get("https://jsonplaceholder.typicode.com/todos")
result = json.loads(result.text)  # turn str var to dict var

# print(result[0]["title"])

for i in result:
    if i["userId"] == 1:
        print(i["title"])

# print(type(result))
