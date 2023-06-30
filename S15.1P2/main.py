class Room:
    def __init__(self, room_number, price_per_night):
        self.room_number = room_number
        self.price_per_night = price_per_night
        self.is_reserved = False

    def reserve(self):
        if not self.is_reserved:
            self.is_reserved = True
            print(f"Camera {self.room_number} a fost rezervată.")
        else:
            print(f"Camera {self.room_number} este deja rezervată.")

    def release(self):
        if self.is_reserved:
            self.is_reserved = False
            print(f"Camera {self.room_number} a fost eliberată.")
        else:
            print(f"Camera {self.room_number} nu este rezervată.")

    def calculate_total_price(self, nights):
        return self.price_per_night * nights

    def __str__(self):
        return f"Camera {self.room_number}"


def bar_consumption_payment(func):
    def wrapper(self, nights, bar_consumption):
        total_price = func(self, nights)
        total_price += bar_consumption
        print(f"Total de plată (cu consum din bar): {total_price}")
    return wrapper


class Hostel:
    def __init__(self):
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    def get_available_rooms(self):
        return [room for room in self.rooms if not room.is_reserved]


@bar_consumption_payment
def calculate_total_price_with_bar_consumption(room, nights):
    return room.calculate_total_price(nights)


def main():
    hostel = Hostel()

    # Crearea camerelor și adăugarea lor în hostel
    room1 = Room(101, 50)
    room2 = Room(102, 60)
    room3 = Room(103, 70)
    hostel.add_room(room1)
    hostel.add_room(room2)
    hostel.add_room(room3)

    # Rezervarea unei camere și calculul totalului de plată cu consumul din bar
    room_to_reserve = hostel.get_available_rooms()[0]
    room_to_reserve.reserve()
    nights_to_stay = 3
    bar_consumption = 20
    calculate_total_price_with_bar_consumption(room_to_reserve, nights_to_stay, bar_consumption)

    # Eliberarea camerei
    room_to_reserve.release()


if __name__ == "__main__":
    main()
