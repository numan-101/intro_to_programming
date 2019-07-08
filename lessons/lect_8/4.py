# collections
# str, list, dict, tuple, range, set

# range: arithmetic progression of integers

# 1 arg = stop val
print(range(5))

for i in range(5):
    print(i)

# 2 arg = start, stop
print(range(5, 10))

l1 = list(range(5, 10))

print(l1)

l2 = list(range(10, 15))

print(l2)

print(l1 + l2)

# 3 arg = start, stop, step
print(list(range(0, 10, 2)))

# Don't:
s = [0, 1, 4, 6, 10]
for i in range(len(s)):
    print(s[i])

# Do:
for v in s:
    print(v)

t = [20, 300, 432, 334, 545, 767]

for pair in enumerate(t):
    print(pair)

for index, value in enumerate(t):
    print('index = {}, value = {}'.format(index, value))


