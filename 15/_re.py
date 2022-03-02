import re

result = dir(re)

# re module

str = "Python Course: Your Python Programming Guide | 40 hours"

# re.findall()

# result = re.findall("python", str)
# result = len(result)

# re.split()

# result = re.split(" ", str)

# re.sub()

# result = re.sub(" ", "-", str) #  Karakterleri degistirir
# result = re.sub("\s", "-", str)  #  Usttekinin aynisi

# re.search()

# result = re.search("Python", str)  # sadece ilk degerle ilgilenir
# result = result.span()
# result = result.start()
# result = result.end()
# result = result.group()
# result = result.string

print(result)
