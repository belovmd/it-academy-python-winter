# Создайте  модель из жизни. Это может быть бронирование комнаты в отеле,
# покупка билета в транспортной компании, или простая РПГ. Создайте
# несколько объектов классов, которые описывают ситуацию Объекты должны
# содержать как атрибуты так и методы класса для симуляции различных действий.
# Программа должна инстанцировать объекты и эмулировать какую-либо
# ситуацию - вызывать методы, взаимодействие объектов и т.д.


class Hotel(object):
    free_rooms = ['101', '102', '103', '104', '105']
    rented_rooms = []
    booked_rooms = []
    list_of_guests = {}


class Person(object):
    def __init__(self, name):
        self.name = name
        self.rentroom = []
        self.bookroom = []

    def __str__(self):
        return self.name + ' is rented ' + ','.join(self.rentroom) + \
               ' room(s), and he(she) is book ' + \
               ','.join(self.bookroom) + ' room(s).'

    def rent_room(self, *numbers_of_room):
        for n in numbers_of_room:
            if n not in Hotel.free_rooms:
                print('This room is not acces, please choose from these:')
                for i in Hotel.free_rooms:
                    print(i)
            else:
                Hotel.rented_rooms.append(
                    Hotel.free_rooms.pop(Hotel.free_rooms.index
                                         (n)))
                self.rentroom.append(n)
            Hotel.list_of_guests[self.name] = self.rentroom

    def check_out(self, *numbers_of_room):
        for n in numbers_of_room:
            if n not in self.rentroom:
                print(self.name + ' is not rent this room(s). He(she) rent :')
                for i in self.rentroom:
                    print(i)
            else:
                Hotel.free_rooms.append(Hotel.rented_rooms.pop
                                        (Hotel.rented_rooms.index(n)))
                self.rentroom.remove(n)

    def book_room(self, *numbers_of_room):
        for n in numbers_of_room:
            if n not in Hotel.free_rooms:
                print('This room is not acces, please choose another.')
                for i in Hotel.free_rooms:
                    print(i)
            else:
                Hotel.booked_rooms.append(
                    Hotel.free_rooms.pop(Hotel.free_rooms.index(n)))

                self.bookroom.append(n)

    def cancel_book_room(self, *numbers_of_room):
        for n in numbers_of_room:
            if n not in self.bookroom:
                print('This room is not booked.')
                for i in Hotel.booked_rooms:
                    print(i)
            else:
                Hotel.free_rooms.append(Hotel.booked_rooms.pop
                                        (Hotel.booked_rooms.index(n)))

                self.bookroom.remove(n)


class InfoTable(object):
    def __str__(self):
        list_of_guests = Hotel.list_of_guests
        print('|    Persons:   |   Rent Rooms: | ')
        for i in list_of_guests.items():
            return '|{:^15}|{:^15}|'.format(i[0], (' '.join(i[1])))


def __str__(self):
    return self.name + ' is rented ' + ','.join(self.rentroom) + \
           ' room(s), and he(she) is book ' + ','.join(self.bookroom) + \
           ' room(s).'


def call_to_hotel():
    name = str(input('''
    Hello, our Hotels greeting you! Please tell
    us your full name ? ''')).title()

    print('We are glade to greet you ' + name + '!')
    while True:
        answer = int(input('''\nif you want rent room enter :1
                              \nif you want book room enter :2
                              \nif you want check out room enter :3
                              \nif you want cancel book room enter :4
                              \nplease make a choice.'''))
        guest = Person(name)

        if answer == 1:
            print('We have this free rooms :')
            for i in Hotel.free_rooms:
                print(i)
            rooms = str(input('Please, choose a  number of room: '))
            if rooms not in Hotel.free_rooms:
                while rooms not in Hotel.free_rooms:
                    rooms = str(input('This room is not access,'
                                      'Please, choose another  '
                                      'number of room: '))
            guest.rent_room(rooms)
            print('You successfully rented room')

        elif answer == 2:
            print('We have this free rooms :')
            for i in Hotel.free_rooms:
                print(i)
            rooms = str(input('Please, choose a  number of room: '))
            if rooms not in Hotel.free_rooms:
                while rooms not in Hotel.free_rooms:
                    rooms = str(input('This room is not access,'
                                      'Please, choose another  '
                                      'number of room: '))
            guest.book_room(rooms)
            print('You successfully booked room')
        elif answer == 3:
            rooms = str(input('Please, choose a  number of room: '))
            if rooms not in guest.rentroom:
                while rooms not in guest.rentroom:
                    rooms = str(input('You did not rent this room, '
                                      'chose another:'))
            guest.check_out(rooms)
            print('You checked out,good by!')
        elif answer == 4:
            rooms = str(input('Please, choose a  number of room: '))
            if rooms not in guest.bookroom:
                while rooms not in guest.bookroom:
                    rooms = str(input('You did not booked this room,'
                                      ' choose another '))
            guest.cancel_book_room(rooms)
            print('You successfully cancel booked room,good by!')
        answer = str(input('Can we do something else for you?'
                           ' Yes/No ')).lower()
        if answer == 'no':
            print('Good by!')
            break
        elif answer == 'yes':
            continue


call_to_hotel()
print(InfoTable())
