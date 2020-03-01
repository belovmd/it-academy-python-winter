"""Создайте  модель из жизни. Это может быть бронирование комнаты в отеле,
покупка билета в транспортной компании, или простая РПГ. Создайте несколько
объектов классов, которые описывают ситуацию Объекты должны содержать как
атрибуты так и методы класса для симуляции различных действий. Программа должна
инстанцировать объекты и эмулировать какую-либо ситуацию - вызывать методы,
взаимодействие объектов и т.д. """
from datetime import date
from datetime import timedelta

booked = {}


class Hotel(object):

    def __init__(self, name="Hilton", comfort="5"):
        self.name = name
        self.comfort = comfort + "*"

    def qof(self, qof=False):
        qof_sngl = 0
        qof_dbl = 0
        qof_lux = 0
        k = Hotel()
        if not qof:
            if k.comfort == "3*":
                qof_sngl = 3
                qof_dbl = 5
                qof_lux = 2
            elif k.comfort == "4*":
                qof_sngl = 4
                qof_dbl = 6
                qof_lux = 3
            elif k.comfort == "5*":
                qof_sngl = 5
                qof_dbl = 7
                qof_lux = 3
            else:
                print("You need to choose class of your hotel")
            self.qof = qof_sngl + qof_dbl + qof_lux
            return (self.qof)


class Room(Hotel):

    def room(self, typ=False):
        self.typ = typ
        if not typ:
            print("Enter type of room: sngl, dbl, lux")
            typ = str(input())
        while typ not in ["sngl", "dbl", "lux"]:
            print("Enter coorect type of room: sngl, dbl, lux")
            typ = str(input())
        return (typ)

    def roomster(self, room="sngl"):
        self.room = room
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


class Customer(object):

    def __init__(self, name=False, surname=False):
        self.name = name
        self.surname = surname


class Booking(Room, Customer):

    def booker(self, room="sngl", date1=False, date2=False):
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
        i = 1
        date_for_dict_first = date1
        date_for_dict_second = date2
        date_loop_1 = date1
        date_loop_2 = date2
        for i in range(self.roomster(room)):
            while date1 <= date2:
                if str(date1) + " " + str(self.name) + " №" + str(
                        i + 1) in booked:
                    i += 1
                    break
                date1 += timedelta(days=1)
            else:
                while date_loop_1 <= date_loop_2:
                    booked[str(date_loop_1) + " " + str(
                        self.name) + " №" + str(i + 1)] = str(
                        guest.name) + " " + str(guest.surname)
                    date_loop_1 += timedelta(days=1)
                    continue

                return ("Your reservation was accepted \n" + str(
                    self.name) + " " + str(self.comfort) + " " + str(
                    self.room) + "\nfrom " + str(
                    date_for_dict_first) + " to " + str(date_for_dict_second))
        else:
            return ("Sorry all room of this type have already reserved")


guest = Customer("Jack", "Nicholson")
w = Booking("Ritz", "3")
print(w.booker("sngl", "2020-3-02", "2020-3-09"), "\n\n")

guest = Customer("Orlando", "Bloom")
w = Booking("Hilton", "5")
print(w.booker("dbl", "2020-4-10", "2020-4-15"), "\n\n")

guest = Customer("Mila", "Jovovich")
w = Booking("Hilton", "5")
print(w.booker("dbl"), "\n\n")

guest = Customer("Angelina", "Jolie")
w = Booking("Hilton", "5")
print(w.booker("dbl"), "\n\n")

guest = Customer("Brad", "Pitt")
w = Booking("Hilton", "5")
print(w.booker("dbl"), "\n\n")

guest = Customer("Tom", "Cruz")
w = Booking("Ritz", "3")
print(w.booker("lux"), "\n\n")

guest = Customer("Tom", "Hanks")
w = Booking("Hilton", "3")
print(w.booker("dbl"), "\n\n")

guest = Customer("Gal", "Gadot")
w = Booking("Riz", "3")
print(w.booker("dbl"), "\n\n")

print(booked)
