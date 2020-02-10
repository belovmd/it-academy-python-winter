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
        self.employee_list = []
        self.all_customers_list = []
        self.current_customers_list = []
        self.total_income = 0

    def all_rooms(self):
        print('All rooms: \t', *[el.id for el in self.rooms])

    def vacant_rooms(self):
        print('Vacant rooms: \t', *[el.id for el in self.rooms if not el.is_occupied])

    def all_employee(self):
        print('All employee: \t', *self.employee_list)

    def service_list(self):
        s_list = [el.id for el in self.rooms if el.cleaning_is_ordered]
        if s_list:
            print('Rooms need cleaning: \t', *s_list)

    def all_customers(self):
        if self.all_customers_list:
            print('Total number of customers:', len(self.all_customers_list))
            for customer in self.all_customers_list:
                if customer.room_id:
                    room_id = customer.room_id
                else:
                    room_id = 'Not in hotel'
                print(customer.id, customer.name, customer.second_name, room_id)

    def current_customers(self):
        if self.current_customers_list:
            print('Number of customers now in hotel:', len(self.current_customers_list))
            print('Id Name S.Name Room')
            for customer in self.current_customers_list:
                print(customer.id, customer.name, customer.second_name, customer.room_id)

    def hotel_status(self):
        print('-' * 50)
        print('Total income: {}'.format(self.total_income))
        self.all_rooms()
        self.vacant_rooms()
        self.all_employee()
        self.service_list()
        self.current_customers()
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
    employee_id = 1
    salary = 250

    def __init__(self, name, second_name, some_hotel):
        self.name = name
        self.second_name = second_name
        self.hotel = some_hotel
        self.hotel.employee_list.append(self)
        self.id = self.employee_id
        Employee.employee_id += 1


class Manager(Employee):
    salary = 1000
    pass


class Maid(Employee):
    def cleaning(self):
        for dirty_room in self.hotel.rooms:
            if dirty_room.cleaning_is_ordered:
                print('Cleaning room', dirty_room.id)
                dirty_room.cleaning_is_ordered = False


class Customer(object):
    customer_id = 0
    room_id = None
    room = None

    def __init__(self, name, second_name, some_hotel):
        self.name = name
        self.second_name = second_name
        self.hotel = some_hotel
        self.hotel.all_customers_list.append(self)
        self.id = self.customer_id + 1
        Customer.customer_id += 1
        print('Welcome to the {} mr {}!'.format(self.hotel.name, self.second_name))

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
                self.hotel.current_customers_list.append(self)
                self.room_id = room.id
                self.room = room
                room.is_occupied = True
                room.hotel.total_income += room.cost
                print('Room number {} is yours mr {}.'
                      .format(room.id, self.second_name))

    def check_out(self):
        self.room.is_occupied = False
        self.hotel.current_customers_list.remove(self)
        # self.room.cleaning_is_ordered = True
        self.__delattr__('room')
        self.__delattr__('room_id')
        print('Thank you mr {}. We hope to see you again.'
              .format(self.second_name))

    def order_cleaning(self):
        self.room.cleaning_is_ordered = True


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

maid_1 = Maid('Anna', 'Maria', my_hotel)

my_hotel.hotel_status()

customer_1 = Customer('Peter', 'Venkman', my_hotel)
customer_2 = Customer('Egon', 'Spengler', my_hotel)
customer_3 = Customer('Raymond', 'Stantz', my_hotel)
customer_4 = Customer('Winston', 'Zeddemore', my_hotel)

customer_1.make_reservation(room_101)
customer_1.make_reservation(room_201)
customer_1.order_cleaning()

customer_2.make_reservation(room_102)

customer_3.make_reservation(room_102)
customer_3.make_reservation(room_201)
customer_3.order_cleaning()

customer_4.make_reservation(room_301)

my_hotel.hotel_status()

maid_1.cleaning()

customer_2.check_out()
customer_3.check_out()
customer_3.make_reservation(room_102)

customer_4.check_out()

my_hotel.hotel_status()

my_hotel.all_customers()
