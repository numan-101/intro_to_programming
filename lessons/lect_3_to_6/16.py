list = [1, -4, 2, -5, 0,'test', 'value', 10]

for item in list:
    val = None
    try:
        val = int(item)
        if val > 0:
            print('posetive')
        elif val < 0:
            print('negative')
        else:
            print('zero')
    except:
        print('removed')