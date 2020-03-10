"""
покупка билетов на маршрутное такси
"""


class Client(object):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        print(f"Клиент \033[35m{first_name} "
              f"{last_name}\033[0m желает воспользоваться "
              f"услугами перевозки")


class Bus(object):
    def __init__(self, number, name_driver, seats):
        self.number = number
        self.name_driver = name_driver
        self.seats = seats

        print(f"Зарегистрирован автобус {number} на {seats} мест")


class Route(object):
    key_route = 1

    def __init__(self, starting_point, finish_point, bus):
        self.passengers = []
        self.starting_point = starting_point
        self.finish_point = finish_point
        self.bus_number = bus.number
        self.number_route = Route.key_route
        self.seats = bus.seats
        print(f"Маршруту \"{starting_point}"
              f" - {finish_point}\" "
              f"назначен автобус {self.bus_number} "
              f"- маршрут № {self.key_route} "
              f"свободных мест {self.seats}")
        self.key_route += 1

    """
    покупка билета на маршрут
    """
    def get_seats(self, client):

        if self.seats > 0:
            self.passengers.append((
                self.seats,
                client.first_name,
                client.last_name
            ))
            self.seats -= 1
            print(f"Пассажир \033[35m {client.first_name} "
                  f"{client.last_name}\033[0m "
                  f"купил билет на {self.starting_point} "
                  f"- {self.finish_point}. Осталось {self.seats} мест")
        else:
            print("---------------------")
            print(f"\033[31mМест на маршруте {self.starting_point} "
                  f"- {self.finish_point} нет. \033[0m"
                  f"Предложите клиету\033[35m "
                  f"{client.first_name} {client.last_name}\033[0m "
                  f"другой маршрут")

    """
    список пассажиров на маршруте
    """
    def get_list_passengers(self):
        print("---------------------")
        print(f"Список пассажиров маршрута "
              f"\033[32m{self.starting_point} "
              f"- {self.finish_point}\033[0m:")

        for passenger in self.passengers[::-1]:
            print(f"место № {passenger[0]}: {passenger[1]} {passenger[2]}")
        if self.seats == 0:
            print(f"\033[32mМаршрут готов к отправке\033[0m")
            print("---------------------")
        else:
            print(f"Осталось свободных мест - \033[35m{self.seats}\033[0m")
            print("---------------------")


if __name__ == '__main__':
    """
    регистрация автобусов в парке
    """
    bus01 = Bus('9034kc-7', 'Василий', 8)
    bus02 = Bus('3045ca-4', 'Николай', 4)
    """
    назначение автобусов на маршрут
    """
    route01 = Route('Минск', 'Вильнюс', bus01)
    route02 = Route('Минск', 'Киев', bus02)
    """
    регистрация клиентов
    """
    client01 = Client('Николай', 'Гуцаленко')
    client02 = Client('Валентин', 'Колко')
    client03 = Client('Константин', 'Шило')
    client04 = Client('Валерий', 'Мыло')
    client05 = Client('Александр', 'Иванов')
    client06 = Client('Дмитрий', 'Петров')
    client07 = Client('Михаил', 'Сидоров')
    client08 = Client('Андрей', 'Широов')
    client09 = Client('Сергей', 'Мотало')
    """
    покупка билета на маршрут
    """
    route01.get_seats(client01)
    route01.get_seats(client02)
    route01.get_seats(client03)
    route01.get_seats(client04)
    route01.get_seats(client05)
    route01.get_seats(client06)
    route01.get_seats(client07)
    route01.get_seats(client08)
    route01.get_seats(client09)
    route02.get_seats(client09)
    """
    список пассажиров на маршруте
    """
    route01.get_list_passengers()
    route02.get_list_passengers()
