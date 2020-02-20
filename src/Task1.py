"""
Создайте  модель из жизни. Это может быть бронирование комнаты в отеле,
покупка билета в транспортной компании, или простая РПГ.
Создайте несколько объектов классов, которые описывают ситуацию
Объекты должны содержать как атрибуты так и методы класса для симуляции
различных действий. Программа должна инстанцировать объекты и эмулировать
какую-либо ситуацию - вызывать методы, взаимодействие объектов и т.д.
"""
import datetime
import pickle
import random
import string


class RentRoom(object):
    """Model for rent room"""

    def __init__(self,
                 bill=0,
                 days=0,
                 num_room=0,
                 name='',
                 address='',
                 in_date='',
                 out_date=''
                 ):
        self.bill = bill
        self.days = days
        self.num_room = num_room
        self.name = name
        self.address = address
        self.in_date = in_date
        self.out_date = out_date

    def person_data(self):
        self.name = input("\nEnter your name:")
        self.address = input("\nEnter your address:")
        self.in_date = input("\nEnter your check in date(yyyy/mm/dd):")
        self.out_date = input("\nEnter your checkout date(yyyy/mm/dd):")
        """
        Calculating days in hotel
        """
        in_date_days = self.in_date.split('/')
        out_date_days = self.out_date.split('/')
        in_date = datetime.date(int(in_date_days[0]),
                                int(in_date_days[1]),
                                int(in_date_days[2])
                                )
        out_date = datetime.date(int(out_date_days[0]),
                                 int(out_date_days[1]),
                                 int(out_date_days[2])
                                 )
        day_t = out_date - in_date
        self.days = str(day_t).split()[0]
        self.days = int(self.days)

    def room(self):
        print("We have the following rooms for you:-")
        print("1.  type A---->rs 6000\n")
        print("2.  type B---->rs 5000\n")
        print("3.  type C---->rs 4000\n")
        print("4.  type D---->rs 3000\n")

        person_choice = int(input("Enter Your Choice Please->"))

        """Get all free rooms from the file rooms.txt"""
        try:
            list_rooms = ()
            rooms = []
            file = open('rooms.txt', 'r')
            for data in file:
                list_rooms = data
            for room in list_rooms.split():
                room = room.strip(string.punctuation)
                rooms.append(room)
            file.close()
        except FileNotFoundError:
            print('File with a free rooms not found!')

        """Room selected and then deleted it from the file rooms
        start and end - it's a range of rooms"""

        def room_gen(start, end):
            while self.num_room == 0:
                num_room = random.randint(start, end)
                for el in rooms:
                    if el == str(num_room):
                        self.num_room = num_room
                        print("Your Room number is:", self.num_room)
                        rooms.remove(str(num_room))
                        with open('rooms.txt', 'w') as f:
                            f.write(str(rooms))

        """Calculate room price,
        days we auto-calculating in person_data"""
        if person_choice == 1:
            print("you have opted room type A")
            self.bill = 6000 * self.days
            room_gen(1, 20)

        elif person_choice == 2:
            print("you have opted room type B")
            self.bill = 5000 * self.days
            room_gen(21, 50)

        elif person_choice == 3:
            print("you have opted room type C")
            self.bill = 4000 * self.days
            room_gen(51, 70)

        elif person_choice == 4:
            print("you have opted room type D")
            self.bill = 3000 * self.days
            room_gen(71, 101)

        else:
            print("please choose a room")

        print("your room rent is =", self.bill, "\n")

    def display(self):
        print("Customer details:")
        print("Customer name:", self.name)
        print("Customer address:", self.address)
        print("Check in date:", self.in_date)
        print("Check out date:", self.out_date)
        print("Your Room rent is:", self.bill)
        print("Your Room number is:", self.num_room)

    def save_customer(self):
        data = {self.num_room: [
            self.name,
            self.address,
            self.bill,
            self.in_date,
            self.out_date
        ]}
        """Creating a dict with customers data
        before the save make sure that the fields
        aren't empty!(running prog - Info Customer)"""

        """Save a serialized dict to a file"""
        try:
            with open('customers.txt', 'ab') as file:
                pickle.dump(data, file)
        except pickle.PicklingError:
            print('Something was wrong :(')

        """Cleaning customer data"""
        self.num_room = 0
        self.days = 0
        self.bill = 0
        self.address = None
        self.name = None
        self.in_date = None
        self.out_date = None

        print("Customer saved!")

    def check_rooms(self):
        list_data_customers = []
        with open('customers.txt', 'rb') as file:
            while True:  # load all customers
                """Loads serialized dict from a file"""
                try:
                    data_customers = pickle.load(file)
                except EOFError:
                    break

                """Calculating days until today
                and if they have minus of zero,
                adding room of this customer to file
                with free rooms"""
                for key, value in data_customers.items():
                    out_date_cus = value[4]
                    out_date_cus = out_date_cus.split('/')
                    out_date = datetime.date(int(out_date_cus[0]),
                                             int(out_date_cus[1]),
                                             int(out_date_cus[2])
                                             )
                    now_date = datetime.date.today()
                    day_t = out_date - now_date
                    days = str(day_t).split()[0]
                    if int(days) <= 0:
                        with open('rooms.txt', 'a') as f:
                            f.write(' ' + str(key))
                    else:  # still live in hotel
                        list_data_customers.append(data_customers)
        """Rewrite customers"""
        with open('customers.txt', 'wb') as f:
            for data_customer in list_data_customers:
                pickle.dump(data_customer, f)


def main():
    inst = RentRoom()
    while True:
        print("1.Enter Customer Data")
        print("2.Calculate room rent")
        print("3.Info Customer")
        print("4.Save Customer data")
        print("5.Check free rooms")
        print("6.Exit")
        inf = int(input("\nEnter your choice:"))

        if inf == 1:
            inst.person_data()
        if inf == 2:
            inst.room()
        if inf == 3:
            inst.display()
        if inf == 4:
            inst.save_customer()
        if inf == 5:
            inst.check_rooms()
        if inf == 6:
            quit()


main()
