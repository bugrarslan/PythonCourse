# 1- Gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazın.
"""
def repeatByNumber(word, repeat):
    for i in range(0, repeat):
        print(word)
"""

# 2- Kendine gönderilen sınırsız sayıdaki parametreyi bir listeye  çeviren fonksiyonu yazınız.
"""
def toTheList(*args):
    array = []
    for i in args:
        array.append(i)

    print(array)
"""

# 3- Gönderilen 2 sayı arasındaki tüm asal sayıları bulun.
"""
def findPerfectNumbers(num1, num2):
    array = [] 
    for i in range(num1, num2+1):
        if i > 1:
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                array.append(i)
    print(array)

findPerfectNumbers(5, 56)
"""

# 4- Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndürünüz
"""
def tambolen(number):
    array = []
    for i in range(2, number):
        if number % i == 0:
            array.append(i)
        else:
            continue
    print(array)
"""
