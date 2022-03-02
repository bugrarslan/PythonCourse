import os
import datetime

result = dir(os)
# result = os.name
#
# Dizin degistirme
# os.chdir("C:\\")
# os.chdir("../..")

# Klasor OLusturma
# os.mkdir("newDirectory")
# os.makedirs("C:\\newDirectory/yeniKlasor")
# os.rename("newDirectory","YeniKlasör")
# os.rmdir("YeniKlasör")
# os.removedirs("YeniKlasör/YeniKlasör")

# Listeleme
# result = os.listdir()
# result = os.listdir("C:\\")
# for file in os.listdir():
#     if file.endswith(".py"):
#         print(file)

# Etkin dizin ogrenme
# result = os.getcwd()


# result = os.stat("date.py")
# result = result.st_size/1024
# result = datetime.datetime.fromtimestamp(result.st_ctime)  # Olusturulma tarihi
# result = datetime.datetime.fromtimestamp(result.st_atime)  # Son erisilme tarihi
# result = datetime.datetime.fromtimestamp(result.st_mtime)  # Degistirilme tarihi

# os.system("notepad.exe")

# path

# result = os.path.abspath("_os.py")
# result = os.path.dirname("D:/Python_Course/15/_os.py")
# result = os.path.abspath(os.path.dirname("_os.py"))

# result = os.path.exists("_os.py")
# result = os.path.exists("D:/Python_Course/15/_os.py")
# result = os.path.exists("D:/Python_Course/15")

# result = os.path.isdir("D:/Python_Course/15")
# result = os.path.isdir("D:/Python_Course/15/_os.py")
# result = os.path.isfile("D:/Python_Course/15/_os.py")

# result = os.path.join("C:\\", "deneme", "deneme1")
# result = os.path.split("C:\\deneme")
# result = os.path.splitext("_os.py")
# result = result[0]

print(result)
