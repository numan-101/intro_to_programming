def factorial1(num):
    if num > 0:
        return num * factorial1(num - 1)
    else:
        return num

print('Factorial1:', factorial1(5))

def factorial2(num):
    if num == 1:
        return num
    else:
        return num * factorial2(num - 1)

print('Factorial2:', factorial2(5))