# def square(num): return num ** 2
square = lambda num: num ** 2

numbers = [1,3,5,9,10,4]

# result = array(map(lambda num: num ** 2, numbers))
# result = array(map(square, numbers))
# result = square(3)

# for item in map(, numbers):
#     print(item)

checkEven = lambda num: num % 2 == 0

# result = array(filter(checkEven, numbers))
# result = array(filter(lambda num: num % 2 == 0, numbers))

result = checkEven(numbers[2])

print(result)

