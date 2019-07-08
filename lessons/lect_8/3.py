# collections
# str, list, dict, tuple, range, set

# str: sequence of characters

print(len('test'))

print("new" + "found" + "land")

print(''.join(["1", "2", "3", "test"]))

l = ','.join(["1", "2", "3", "test"])

print(l)

print(l.split(','))

print("unforgetable".partition("forget"))

name, _, age = "anas:18".partition(":")

print(name, age)

print("The age of {0} is {1}. {0} is old".format('Anas', 18))

print("{} {} {}".format(1, 2, 3))

print("Seat is reserved by {name} for {duration}".format(name='Anas', duration='12 days'))

nums = (1, 2, 3)
print("position at {nums[0]}, {nums[1]}, {nums[2]}".format(nums=nums))

import math
print("Math constants: pi={m.pi:.3f}, e={m.e}".format(m=math))

print(help(str))