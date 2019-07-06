# list
# loop
numbers = [1, 4, 50, 100, 200, 44, 230]
largest = numbers[0]

for x in numbers:
    if x > largest:
        largest = x

print(largest)