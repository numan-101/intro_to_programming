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

        # seats init, list of dict
        rows, seats = self._aircraft.seating_plan()
        self._seating = [None]

        for _ in rows:
            temp_dict = {}
            for seat in seats:
                temp_dict[seat] = None # empty seat
            self._seating += [temp_dict]
        

    def number(self):
        return self._number

    def airline(self):
        return self._number[:2]

    # law of demeter
    def aircraft_model(self):
        return self._aircraft.model()

    def allocate_seat(self, seat, passenger):
        '''Allocate seats to passengers
        Args: 
            seat: A seat designator such as '12C' or '21F'.
            passenger: the passenger name.
        Raises: 
            ValueError: if seat is unavailable.
        '''
        rows, seat_letters = self._aircraft.seating_plan()
        letter = seat[-1]
        if letter not in seat_letters:
            raise ValueError('Invalid seat letter {}'.format(letter))
        
        row_text = seat[:-1]

        try:
            row = int(row_text)
        except ValueError:
            raise ValueError('Invalid seat row {}'.format(row_text))

        if row not in rows:
            raise ValueError('Invalid row number {}'.format(row))

        if self._seating[row][letter] is not None:
            raise ValueError('Seat {} already occupied'.format(seat))

        self._seating[row][letter] = passenger



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

from pprint import pprint as pp
pp(f._seating)

f.allocate_seat('12A', 'Anas Najaa')

pp(f._seating)

# f.allocate_seat('12A', 'Ahmed')

f.allocate_seat('15F', 'Zaher')
f.allocate_seat('15E', 'Fahed')

# f.allocate_seat('E27', 'Ammar')

f.allocate_seat('1C', 'Rami')
f.allocate_seat('1D', 'Asad')

# f.allocate_seat('DD', 'Eyad')

pp(f._seating)