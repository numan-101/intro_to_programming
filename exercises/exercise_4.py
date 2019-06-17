#name validation
name = input("Enter name: ")
name_length = len(name)

if name_length > 50:
    print('name too long')
elif name_length < 3:
    print('name must be at least 3 characters')
else:
    print('name passes')