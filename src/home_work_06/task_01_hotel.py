"""
Создайте  модель из жизни. Это может быть бронирование комнаты в отеле,
покупка билета в транспортной компании, или простая РПГ.
Создайте несколько объектов классов, которые описывают ситуацию.
Объекты должны содержать как атрибуты так и методы класса
для симуляции различных действий.
Программа должна инстанцировать объекты
и эмулировать какую-либо ситуацию - вызывать методы,
взаимодействие объектов и т.д.
"""


class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.service_orders = []
        self.customers_list = []

    def add_room(self, new_room):
        self.rooms.append(new_room)

    def all_rooms(self):
        all_rooms_nums = []
        for room in self.rooms:
            all_rooms_nums.append(room.id)
        print('All rooms: \t', *all_rooms_nums)

    def vacant_rooms(self):
        vacant_rooms_nums = []
        for room in self.rooms:
            if not room.is_occupied:
                vacant_rooms_nums.append(room.id)
        print('Vacant rooms: \t', *vacant_rooms_nums)

    def add_costumer(self, new_customer):
        self.customers_list.append(new_customer)

    def all_customers(self):
        if self.customers_list:
            print('Total number of customers:', len(self.customers_list))
            for customer in self.customers_list:
                print(customer.__dict__)

    def hotel_status(self):
        self.all_rooms()
        self.vacant_rooms()
        self.all_customers()


class Room(object):
    room_id = 100
    cost = 50
    is_occupied = False
    cleaning_is_ordered = False

    def __init__(self):
        self.id = self.room_id + 1
        Room.room_id += 1

    def book(self, customer):
        if not self.is_occupied:
            self.is_occupied = True
            customer.room_id = self.id
            print('Room number {} is yours mr {}'
                  .format(self.id, customer.second_name))
        else:
            print('Sorry mr {} room {} is already occupied'
                  .format(customer.second_name, self.id))

    def leave_room(self, customer):
        self.is_occupied = False
        delattr(customer, 'room_id')

    def order_cleaning(self):
        self.cleaning_is_ordered = True
        print('Order confirmed. Thank you!')


class Lux(Room):
    room_id = 200
    cost = 100

    def __init__(self):
        super().__init__()
        self.id = self.room_id + 1
        Lux.room_id += 1


class Penthouse(Room):
    room_id = 300
    cost = 200

    def __init__(self):
        super().__init__()
        self.id = self.room_id + 1
        Penthouse.room_id += 1


class Employee:
    pass


class Customer:
    customer_id = 0
    room_id = None

    def __init__(self, name=None, second_name=None):
        if not name:
            self.name = input('Enter your name\n')
        else:
            self.name = name
        if not second_name:
            self.second_name = input('Enter your second name\n')
        else:
            self.second_name = second_name

        self.id = self.customer_id + 1
        Customer.customer_id += 1

    def make_reservation(self, room):
        room.book(self)

    def check_out(self, room):
        room.leave_room(self)


my_hotel = Hotel('Ghost Hotel')

print('Welcome to the', my_hotel.name)

room_101 = Room()
room_102 = Room()
room_103 = Room()
room_201 = Lux()
room_301 = Penthouse()

my_hotel.add_room(room_101)
my_hotel.add_room(room_102)
my_hotel.add_room(room_103)
my_hotel.add_room(room_201)
my_hotel.add_room(room_301)

my_hotel.hotel_status()

customer_1 = Customer('Peter', 'Venkman')
my_hotel.add_costumer(customer_1)
customer_2 = Customer('Egon', 'Spengler')
my_hotel.add_costumer(customer_2)
customer_3 = Customer('Raymond', 'Stantz')
my_hotel.add_costumer(customer_3)

customer_1.make_reservation(room_101)
customer_2.make_reservation(room_102)
customer_3.make_reservation(room_102)

my_hotel.hotel_status()

customer_2.check_out(room_102)
customer_3.make_reservation(room_102)

my_hotel.hotel_status()
