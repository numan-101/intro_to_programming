# collections
# str, list, dict, tuple, range, set

# tuple: immutable sequence
t = ('kuwait', 18.0, 4)
print(t)

print(t[0])
print(t[1])

print(len(t))

for item in t:
    print(item)

print(t + ('syria', 34.0, 2))

print(t * 3)

a = ((1, 2), (3, 4), (5, 6))

print(a[0])
print(a[0][0])

h = (391)
print(type(h))

k = (240,)
print(type(k))

e = ()
print(type(e))

p = 1, 2, 3, 4, 5, 6
print(type(p))

def age_height():
    return 12, 5

#tuple unpacking
age, height = age_height()
print(age)
print(height)

# list to tuple
print(tuple([1, 2, 3, 4, 5, 6]))

# string to tuple
print(tuple('test'))

print(1 in (0, 2, 3))
