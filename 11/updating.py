# with open("newFile.txt", "r+", encoding="utf-8") as file: # r+ hem okuma hem de yazma modunu temsil eder
#     content = file.read()
#     print(content)


# with open("newFile.txt", "r+", encoding="utf-8") as file:
#     file.seek(20)
#     file.write("deneme")

# with open("newFile.txt", "r+", encoding="utf-8") as file:
#     print(file.read())

# ********** sayfa sonunda güncelleme **************

# with open("newFile.txt", "cubes", encoding="utf-8") as file:
#     file.write("\nArda Ocak")

# *********** sayfa başında güncelleme ************


# with open("newFile.txt", "r+", encoding="utf-8") as file:
#     content = file.read()
#     content = "Efe Arslan\n" + content
#     file.seek(0)
#     file.write(content)

# with open("newFile.txt", "r", encoding="utf-8") as file:
#     print(file.read())

# ********** sayfa ortasında güncelleme ************

with open("newFile.txt", "r+", encoding="utf-8") as file:
    list = file.readlines()
    list.insert(1, "Zeliha Arslan\n")
    file.seek(0)
    # for i in array:
    #     file.write(i)
    file.writelines(list)

with open("newFile.txt", "r", encoding="utf-8") as file:
    print(file.read())
