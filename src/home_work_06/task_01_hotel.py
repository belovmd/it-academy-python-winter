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


class Hotel(object):
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.customers_list = []
        self.service_orders = []
        self.total_income = 0

    def all_rooms(self):
        all_rooms_nums = [el.id for el in self.rooms]
        print('All rooms: \t', *all_rooms_nums)

    def vacant_rooms(self):
        vacant_rooms_nums = [el.id for el in self.rooms if not el.is_occupied]
        print('Vacant rooms: \t', *vacant_rooms_nums)

    def all_customers(self):
        if self.customers_list:
            print('Total number of customers:', len(self.customers_list))
            for customer in self.customers_list:
                print(customer.id, customer.name, customer.second_name, customer.room_id)

    def hotel_status(self):
        print('-' * 50)
        print('Total income: {}'.format(self.total_income))
        self.all_rooms()
        self.vacant_rooms()
        self.all_customers()
        print('-' * 50)


class Room(object):
    type_id = 100
    cost = 50
    is_occupied = False
    cleaning_is_ordered = False

    def __init__(self, some_hotel):
        self.id = self.type_id + 1
        Room.type_id += 1
        self.hotel = some_hotel
        self.hotel.rooms.append(self)


class Lux(Room):
    type_id = 200
    cost = 100

    def __init__(self, some_hotel):
        super().__init__(some_hotel)
        self.id = self.type_id + 1
        Lux.type_id += 1


class Penthouse(Room):
    type_id = 300
    cost = 200

    def __init__(self, some_hotel):
        super().__init__(some_hotel)
        self.id = self.type_id + 1
        Penthouse.type_id += 1


class Employee(object):
    pass


class Customer(object):
    customer_id = 0
    room_id = None
    room = None

    def __init__(self, name, second_name, some_hotel):
        self.name = name
        self.second_name = second_name
        self.hotel = some_hotel
        self.hotel.customers_list.append(self)
        self.id = self.customer_id + 1
        Customer.customer_id += 1

    def make_reservation(self, room):
        if self.room:
            print("Mr {} you can't reserve another room. "
                  "You need to checkout first."
                  .format(self.second_name))
        else:
            if room.is_occupied:
                print('Sorry mr {}, room {} is already occupied.'
                      .format(self.second_name, room.id))
            else:
                self.room_id = room.id
                self.room = room
                room.is_occupied = True
                room.hotel.total_income += room.cost
                print('Room number {} is yours mr {}.'
                      .format(room.id, self.second_name))

    def check_out(self):
        self.room.is_occupied = False
        self.__delattr__('room')
        self.__delattr__('room_id')
        print('Thank you mr {}. We hope to see you again.'
              .format(self.second_name))


my_hotel = Hotel('Ghost Hotel')

print('Welcome to the {}!'.format(my_hotel.name))

room_101 = Room(my_hotel)
room_102 = Room(my_hotel)
room_103 = Room(my_hotel)
room_104 = Room(my_hotel)
room_105 = Room(my_hotel)
room_201 = Lux(my_hotel)
room_202 = Lux(my_hotel)
room_301 = Penthouse(my_hotel)

my_hotel.hotel_status()

customer_1 = Customer('Peter', 'Venkman', my_hotel)
customer_2 = Customer('Egon', 'Spengler', my_hotel)
customer_3 = Customer('Raymond', 'Stantz', my_hotel)
customer_4 = Customer('Winston', 'Zeddemore', my_hotel)

customer_1.make_reservation(room_101)
customer_1.make_reservation(room_201)
customer_2.make_reservation(room_102)
customer_3.make_reservation(room_102)
customer_3.make_reservation(room_201)
customer_4.make_reservation(room_301)

my_hotel.hotel_status()

customer_2.check_out()
customer_3.check_out()
customer_3.make_reservation(room_102)
customer_4.check_out()

my_hotel.hotel_status()
