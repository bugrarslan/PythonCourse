# Dosya acmak ve olusturmak icin open() fonksiyonu kullanilir.
# Kullanimi: open(dosyaAdi, dosyaErismeModu)
# dosyaErismeModu => dosyayı hangi amacla actigimizi belirtir.

# "w": (Write) yazma modu. 
#   ** Dosyayı konumda oluşturur.
#   ** Dosya içeriğini siler ve yeniden ekleme yapar.

# file = open("newFile.txt", "w")
# file.close()

# file = open("C:/users/buğra/desktop/newFile.txt", "w")
# print(file)
# file.close()

# file = open("newFile.txt", "w", encoding="utf-8")
# file.write("Buğra Arslan")
# file.close()

# "cubes": (append) ekleme. Dosya konumda yoksa oluşturur.

# file = open("newFile.txt", "cubes", encoding="utf-8")
# file.write("\nBerkay Arslan")
# file.close()

# "x": (create) oluşturma. Dosya  zaten varsa hata verir.

# file = open("newFile2.txt", "x", encoding="utf-8")

# "r": (read) okuma. varsayılan. Dosya konumda yoksa hata verir.