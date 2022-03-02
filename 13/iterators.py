# array = [1, 2, 3, 4, 5]


# iterator = iter(array)
#
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
#
# for i in array:
#     print(i)

# iterator = iter(array)
#
# while True:
#     try:
#         element = next(iterator)
#         print(element)
#     except StopIteration:
#         break

class MyNumbers:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= self.stop:
            x = self.start
            self.start += 1
            return x
        else:
            raise StopIteration


array = MyNumbers(10, 20)

myIter = iter(array)

while True:
    try:
        element = next(myIter)
        print(element)
    except StopIteration:
        break
