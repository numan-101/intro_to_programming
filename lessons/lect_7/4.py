# init method with validation

class Flight:
    def __init__(self, number):
        if not number[:2].isalpha():
            raise ValueError(f'Airline code must be Alpha, found: {number}')

        if not number[:2].isupper():
            raise ValueError(f'Airline code must be upper case, found: {number}')

        if not number[2:].isdigit():
            raise ValueError(f'Route number must be digits, found: {number}')

        self._number = number

    def number(self):
        return self._number

    def airline(self):
        return self._number[:2]

## f = Flight('N600')

f = Flight('NC600')

print(f.number())

print(f.airline())