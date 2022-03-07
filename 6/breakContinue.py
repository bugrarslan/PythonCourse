# name = "Buğra Arslan"

# for letter in name:
    
#     ifletter == "u":
#         continue
#     print(letter)

# x = 0

# while x < 5:
#     if x == 2:
#         continue
#     print(x)
#     x += 1

# 1 den 100 e kadar tek sayıların toplamı

x = 0
result = 0
while x <= 100:
    x += 1
    if x % 2 == 0:
        continue
    result += x
    
print(result)