#weight conversion v2
user_weight = input('Weight: ')
weight = float(user_weight)
user_conversion_unit = input('(L)bs or (K)g: ')

if user_conversion_unit.lower() == 'l':
    print(weight * 0.45)
elif user_conversion_unit.lower() == 'k':
    print(weight / 0.45)
else:
    print("Unknown unit")