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


class Aircraft:

    def __init__ (self, registration, model, num_rows, num_seats_per_row):
        # TODO: perofrm validation
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self.num_seats_per_row = num_seats_per_row
    
    def registration(self):
        return self._registration

    def model(self):
        return self._model

    def seating_plan(self):
        rows = range(1, self._num_rows + 1)
        cols = "ABCDEFGHIJK"[:self.num_seats_per_row]
        return (rows, cols)

## f = Flight('N600')

f = Flight('NC600')

print(f.number())

print(f.airline())

a = Aircraft('G-EUPT', 'Airbus A319', num_rows=22, num_seats_per_row=6)

print(a.registration())
print(a.model())
print(a.seating_plan())