# def myDecorator(func):
#     def wrapper(name):
#         print("fonksiyondan onceki islemler")
#         func(name)
#         print("fonksiyondan sonraki islemler")
#     return wrapper

# @myDecorator
# def sayHello(name):
#     print("Hello ", name)

# sayHello("Ali")

import math
import time


def calculateTime(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        time.sleep(1)
        func(*args, **kwargs)
        finish = time.time()
        print("fonksiyon " + func.__name__ + " " +
              str(finish - start) + " saniye sürdü")

    return wrapper


@calculateTime
def usAlma(a, b):
    print(math.pow(a, b))


@calculateTime
def faktoriyel(num):
    print(math.factorial(num))


usAlma(2, 3)
faktoriyel(4)
