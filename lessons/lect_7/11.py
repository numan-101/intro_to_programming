# inheritance
# A sub-class can derive from a base-class
# inheriting its behavior and making behavior specific 
# to the sub-class

'''Inheritance in python is most useful when sharing implementation.'''
from pprint import pprint as pp
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

    def _parse_seat(self, seat):
        '''Parse a seat designator into a valid row and letter.
        Args: 
            seat: A seat designator such as 12F
        
        Returns:
            A tuple containing an integer and a string for row and seat
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

        return row, letter

    def allocate_seat(self, seat, passenger):
        '''Allocate seats to passengers
        Args: 
            seat: A seat designator such as '12C' or '21F'.
            passenger: the passenger name.
        Raises: 
            ValueError: if seat is unavailable.
        '''
        
        row, letter = self._parse_seat(seat)

        if self._seating[row][letter] is not None:
            raise ValueError('Seat {} already occupied'.format(seat))

        self._seating[row][letter] = passenger

    def relocate_passengar(self, from_seat, to_seat):
        '''Relocate a passengar to a different seat.
        Args:
            from_seat: existing seat designator for the passengar to be moved
            to_seat: the new seat designator
        '''

        from_row, from_letter = self._parse_seat(from_seat)
        if self._seating[from_row][from_letter] is None:
            raise ValueError('No passenger to relocate in seat'.format(from_seat))

        
        to_row, to_letter = self._parse_seat(to_seat)
        if self._seating[to_row][to_letter] is not None:
            raise ValueError('Seat {} already occupied'.format(to_seat))

        self._seating[to_row][to_letter] = self._seating[from_row][from_letter]
        self._seating[from_row][from_letter] = None

    def num_available_seats(self):
        seats = 0
        for row in self._seating:
            if row is not None:
                for s in row.values():
                    if s is None:
                        seats += 1
        return seats
    

    def make_boarding_cards(self, card_printer):
        for passenger, seat in sorted(self._passenger_seats()):
            card_printer(passenger, seat, self.number(), self.aircraft_model())

    def _passenger_seats(self):
        '''An iterable series of passenger seating allocations'''
        row_numbers, seat_letters = self._aircraft.seating_plan()
        for row in row_numbers:
            for letter in seat_letters:
                passenger = self._seating[row][letter]
                if passenger is not None:
                    yield(passenger, "{}{}".format(row, letter))
        

class Aircraft:
    def __init__(self, registration):
        self._registration = registration
    
    def registration(self):
        return self._registration

    def num_seats(self):
        rows, rows_seats = self.seating_plan()
        return len(rows) * len(rows_seats)


class AirBusA319(Aircraft):    
    def model(self):
        return 'Airbus A319'

    def seating_plan(self):
        return range(1, 23), 'ABCDEF'

    # duplicate code
    # def num_seats(self):
    #     rows, rows_seats = self.seating_plan()
    #     return len(rows) * len(rows_seats)


class Boeing777(Aircraft):
    def __init__(self, registration):
        self._registration = registration
    
    def registration(self):
        return self._registration
    
    def model(self):
        return 'Boeing 777'

    def seating_plan(self):
        return range(1, 56), 'ABCDEGHJK' 

    # duplicate code
    # def num_seats(self):
    #     rows, rows_seats = self.seating_plan()
    #     return len(rows) * len(rows_seats)

def make_flights():
    # different classes work with Flight class because both quack like ducks
    f = Flight('BA758', AirBusA319('G-EUPT'))
    f.allocate_seat('12A', 'Anas')
    f.allocate_seat('15F', 'Zaher')
    f.allocate_seat('15E', 'Fahed')
    f.allocate_seat('1C', 'Rami')
    f.allocate_seat('1D', 'Asad')

    g = Flight('AF72', Boeing777('F-GSPS'))
    g.allocate_seat('55K', 'Hani')
    g.allocate_seat('33G', 'Sami')
    g.allocate_seat('4B', 'Khaled')
    g.allocate_seat('4A', 'Yaser')

    return f, g


# Polymorphism
# Using objects of different types through a common interface
def console_card_printer(passenger, seat, flight_number, aircraft):
    output =    "| Name: {0}" \
                "  Flight: {1}" \
                "  Seat: {2}" \
                "  Aircraft: {3}" \
                " |".format(passenger, flight_number, seat, aircraft)
    banner = '+' + '-' * (len(output) - 2) + '+'
    border = '|' + ' ' * (len(output) - 2) + '|'
    lines = [banner, border, output, border, banner]
    card = '\n'.join(lines)
    print(card)
    print()

f = AirBusA319('G-EZBT')
print(f.num_seats())

g = Boeing777('N717AN')
print(g.num_seats())

