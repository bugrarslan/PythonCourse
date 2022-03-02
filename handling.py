# Error handling => hata yönetimi

# try:
#     x = int(input("x: "))
#     y = int(input("y: "))
#     print(x/y)
# except (ZeroDivisionError, ValueError) as e:
#     print("yanlış bilgi girdiniz")
#     print(e)

# try:
#     x = int(input("x: "))
#     y = int(input("y: "))
#     print(x/y)
# except:
#     print("yanlış bilgi girdiniz")

while True:
    try:
        x = int(input("x: "))
        y = int(input("y: "))
        print(x/y)
    except Exception as ex:
        print("yanlış bilgi girdiniz", ex)

    else: # except çalışmazsa çalışır
        break
    finally: # her hâlukarda çalışır
        print("try except sonlandı")