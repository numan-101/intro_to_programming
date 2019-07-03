# init method
# init is an initializer not a contructor
# self is semilar to this in java

class Flight:
    def __init__(self, number):
        self._number = number

    def number(self):
        return self._number

f = Flight('N600')
print(f.number())
