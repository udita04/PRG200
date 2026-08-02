class Bus:

    def __init__(self, route, total_seats):
        self.route = route
        self.total_seats = total_seats
        self.booked = {}

    def book_seat(self, seat_number, passenger_name):

        if seat_number in self.booked:
            print("Seat already booked")
        elif seat_number > self.total_seats or seat_number < 1:
            print("Invalid seat number")
        else:
            self.booked[seat_number] = passenger_name
            print(passenger_name, "booked Seat", seat_number)

    def available_seats(self):
        return self.total_seats - len(self.booked)

    def passenger_list(self):

        print("\nPassenger List")
        print("")

        for seat in sorted(self.booked):
            print("Seat", seat, "-", self.booked[seat])


bus = Bus("Kathmandu - Pokhara", 10)

bookings = [
    (3, "Ramila Shrestha"),
    (7, "Deepak Gurung"),
    (3, "Anita Rai"),
    (1, "Prakash Magar"),
    (7, "Suman Tamang")
]

for seat, name in bookings:
    bus.book_seat(seat, name)

print("\nAvailable Seats:", bus.available_seats())

bus.passenger_list()