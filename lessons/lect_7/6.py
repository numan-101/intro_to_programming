# law of demeter
# the principle of least knowledge
# only talk to your friends

class Flight:
    ''' A Flight with a particular passenger aircraft '''
    def __init__(self, number, aircraft):
        if not number[:2].isalpha():
            raise ValueError(f'Airline code must be Alpha, found: {number}')

        if not number[:2].isupper():
            raise ValueError(f'Airline code must be upper case, found: {number}')

        if not number[2:].isdigit():
            raise ValueError(f'Route number must be digits, found: {number}')

        self._number = number
        self._aircraft = aircraft

    def number(self):
        return self._number

    def airline(self):
        return self._number[:2]

    # law of demeter
    def aircraft_model(self):
        return self._aircraft.model()


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

f = Flight('BA758', Aircraft('G-EUPT', 'Airbus A319', num_rows=22, num_seats_per_row=6))


print(f.aircraft_model())

# complex is better than complicated
# many moving parts
# combined in a clever box
# are now one good tool
# f.aircraft_model()
# no need to know about the aircraft class
# which means it doesn't matter if the inner mechanisim changes
# the mthod call will stay the same