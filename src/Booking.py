"""Создайте  модель из жизни. Это может быть бронирование комнаты в отеле,
покупка билета в транспортной компании, или простая РПГ. Создайте несколько
объектов классов, которые описывают ситуацию Объекты должны содержать как
атрибуты так и методы класса для симуляции различных действий. Программа должна
инстанцировать объекты и эмулировать какую-либо ситуацию - вызывать методы,
взаимодействие объектов и т.д. """
from datetime import date
from datetime import timedelta


class Hotel(object):
    booked = {}
    parking = "no"

    def __init__(self, name="Hilton", comfort="5", parking=False):
        self.name = name
        self.comfort = comfort + "*"
        if self.comfort != "5*":
            self.parking = self.parking
        else:
            if parking:
                self.parking = parking
            else:
                parking = "yes"
                self.parking = parking

    def roomster(self, room="sngl"):
        room = Room()
        self.room = room.type_comfort
        if self.comfort == "3*":
            if self.room == "sngl":
                return (1)
            elif self.room == "dbl":
                return (2)
            elif self.room == "lux":
                return (1)
        elif self.comfort == "4*":
            if self.room == "sngl":
                return (2)
            elif self.room == "dbl":
                return (2)
            elif self.room == "lux":
                return (2)
        elif self.comfort == "5*":
            if self.room == "sngl":
                return (3)
            elif self.room == "dbl":
                return (3)
            elif self.room == "lux":
                return (3)
        else:
            print("You need to choose class of your hotel")


class Room(object):

    def __init__(self, type_comfort="lux", food="all inclusive"):
        self.type_comfort = type_comfort
        self.food = food


class Customer(object):

    def __init__(self, name=False, surname=False, payment="cash"):
        self.name = name
        self.surname = surname
        self.payment = payment


def booking(hotel, guest, room, date1=False, date2=False):
    if not date1:
        date1 = date.today()
    else:
        date1 = tuple(int(el) for el in date1.split("-"))
        date1 = date(date1[0], date1[1], date1[2])
    if not date2:
        date2 = date1 + timedelta(days=1)
    else:
        date2 = tuple(int(el) for el in date2.split("-"))
        date2 = date(date2[0], date2[1], date2[2]) + timedelta(days=1)
    if date1 > date2:
        return ("Error in dates")

    date_for_dict_first = date1
    date_for_dict_second = date2

    date_loop_1 = date1
    date_loop_2 = date2

    for i in range(hotel.roomster(room)):
        while date1 <= date2:
            if str(date1) + " " + str(hotel.name) + " №" + str(
                    i + 1) in hotel.booked:
                i += 1
                break
            date1 += timedelta(days=1)
        else:
            while date_loop_1 <= date_loop_2:
                hotel.booked[str(date_loop_1) + " " + str(
                    hotel.name) + " №" + str(i + 1)] = str(
                    guest.name) + " " + str(guest.surname)
                date_loop_1 += timedelta(days=1)
                continue
            if hotel.parking == "yes":
                return ("Your reservation was accepted \n" + str(
                    hotel.name) + " " + str(hotel.comfort) + " " + str(
                    room.type_comfort) + "\nfrom " + str(
                    date_for_dict_first) + " to " + str(
                    date_for_dict_second) + "\nNumber of your parking place "
                    "is " + str(i + 1))
            elif hotel.parking == "no" and hotel.comfort == "5*":
                return ("Your reservation was accepted \n" + str(
                    hotel.name) + " " + str(hotel.comfort) + " " + str(
                    room.type_comfort) + "\nfrom " + str(
                    date_for_dict_first) + " to " + str(
                    date_for_dict_second) + "\nYou can get parking place "
                    "at registration desk ")
            else:
                return ("Your reservation was accepted \n" + str(
                    hotel.name) + " " + str(hotel.comfort) + " " + str(
                    room.type_comfort) + "\nfrom " + str(
                    date_for_dict_first) + " to " + str(
                    date_for_dict_second) + "\nSorry we don't have a parking")
    else:
        return ("Sorry all room of this type have already reserved")


guest = Customer("Jack", "Nicholson")
hotel = Hotel("Ritz", "3", parking="yes")
room = Room("sngl", "breakfast")
print(booking(hotel, guest, room, "2020-3-02", "2020-3-09"), "\n\n")

guest = Customer("Orlando", "Bloom")
hotel = Hotel("Hilton", "5", parking="no")
room = Room("dbl", "breakfast")
print(booking(hotel, guest, room, "2020-4-10", "2020-4-15"), "\n\n")

guest = Customer("Mila", "Jovovich")
hotel = Hotel("Hilton", "5")
room = Room("dbl")
print(booking(hotel, guest, room), "\n\n")

guest = Customer("Angelina", "Jolie")
hotel = Hotel("Hilton", "5")
room = Room("dbl")
print(booking(hotel, guest, room), "\n\n")

guest = Customer("Brad", "Pitt")
hotel = Hotel("Hilton", "5")
room = Room("dbl")
print(booking(hotel, guest, room), "\n\n")

guest = Customer("Tom", "Cruz")
hotel = Hotel("Ritz", "3")
room = Room("lux")
print(booking(hotel, guest, room), "\n\n")

guest = Customer("Tom", "Hanks")
hotel = Hotel("Hilton", "5")
room = Room("dbl")
print(booking(hotel, guest, room), "\n\n")

guest = Customer("Gal", "Gadot")
hotel = Hotel("Riz", "3")
room = Room("dbl")
print(booking(hotel, guest, room), "\n\n")

print((hotel.booked), "\n\n")
