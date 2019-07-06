# nested comparison operators
temperature = -1

if temperature > 30:
    print("it's a hot day")
elif temperature >= 20:
    print("it's a warm day")
elif temperature >= 10:
    print("it's a cold day")
elif temperature > 0:
    print("it's freezing")
elif temperature == 0:
    print("temp is 0")
else:
    print("It's below zero")