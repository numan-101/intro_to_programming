def to_float(num):
    return float(num)

def square(num):
    return num ** 2

num = input('>')
num = to_float(num)
num = square(num)

print(num)