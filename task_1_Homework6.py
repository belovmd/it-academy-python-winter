""" Создайте  модель из жизни.
    Это может быть бронирование комнаты в отеле,
    покупка билета в транспортной компании, или простая РПГ.
    Создайте несколько объектов классов, которые описывают ситуацию
    Объекты должны содержать как атрибуты так и методы класса
    для симуляции различных действий.
    Программа должна инстанцировать объекты и эмулировать
    какую-либо ситуацию - вызывать методы, взаимодействие объектов и т.д.
"""


class AddressBookEntry:
    version = 1.0

    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def __repr__(self):
        return ' [Address Book Entry: %s, %s ] ' % (self.name, self.phone)

    def updatePhone(self, phone):
        self.phone = phone


class EmployeeAddressBookEntry(AddressBookEntry):
    def __init__(self, name, phone, id, social):
        AddressBookEntry.__init__(self, name, phone)
        self.empid = id
        self.ssn = social


class CustomerAddressBookEntry(AddressBookEntry):
    def __init__(self, name, phone, order, date):  # Переопределить конструктор
        self.order = order
        self.date = date
        AddressBookEntry.__init__(self, name, phone)  # Выполнить исходный c ’mgr1

    def updateOrder(self, order):
        self.order = []
        self.order = self.order.extend(order)

    def updateDate(self, date):
        self.date = []
        self.date = self.date.extend(date)

    def __repr__(self):
        return ' [Customer Address Book Entry: %s, %s, %s, %s ] ' % (self.name,
                                                                     self.phone,
                                                                     self.order,
                                                                     self.date)


robert = AddressBookEntry('Staf', '55-789-54645-55')

print(robert.name, robert.phone)

mitchel = CustomerAddressBookEntry('Makl Mitchel',
                                   +375447496999,
                                   'Order № 25',
                                   '25.01.2020')

print(mitchel)
# "Магический" метод __repr__ в данном случае иллюстрирует
# проявление полиморфизма.
print(robert)
