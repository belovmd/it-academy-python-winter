# Игра с компьютером

from random import randint, choice
from time import sleep


class Person:
    antagonist = None
    hp = 100
    max_HP = hp
    simple_damage = [18, 25]
    special_damage = [10, 35]
    first_aid_kit = [15, 25]
    actions = [f"1. обычный удар,"
               f" наносит {simple_damage[0]}-{simple_damage[1]} урона",
               f"2. спецприём,"
               f" наносит {special_damage[0]}-{special_damage[1]} урона",
               f"3. аптечка,"
               f" восстановит {first_aid_kit[0]}-{first_aid_kit[1]} HP",
               "ввод произвольных символов будет означать пропуск хода"]

    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def hp_change(self, change):
        self.hp += change
        if change > 0:
            if self.hp >= self.max_HP:
                self.hp = self.max_HP
                print(f"У {self.name} снова {self.max_HP} HP!")
            else:
                print(f"{self.name} восстановил {change} HP."
                      f" Теперь у него {self.hp} HP")
        else:
            if self.hp <= 0:
                print(f"\n{self.name} проиграл")
                input("\n<Enter>")
                exit(0)
            else:
                print(f"{self.name} потерял {-change} HP!"
                      f" Теперь у него {self.hp} HP!")

    def simple_kick(self):
        damage = randint(*self.simple_damage)
        print(f"{self.name} наносит обычный удар")
        self.antagonist.hp_change(-damage)

    def special_kick(self):
        damage = randint(*self.special_damage)
        print(f"{self.name} выполняет спецприём!")
        self.antagonist.hp_change(-damage)

    def healing(self):
        recovery = randint(*self.first_aid_kit)
        print(f"{self.name} использовал аптечку")
        self.hp_change(recovery)


class Player(Person):

    def move(self):
        for action in Person.actions:
            print(action)
        print()
        answer = input(f"Выберите действие, {self.name}: ", )
        if answer == "1":
            self.simple_kick()
        elif answer == "2":
            self.special_kick()
        elif answer == "3":
            self.healing()


class Computer(Person):

    def move(self):
        if self.hp == self.max_HP:
            answer = str(randint(1, 2))
        else:
            answer = str(randint(1, len(self.actions)))
        if answer == "1":
            self.simple_kick()
        elif answer == "2":
            self.special_kick()
        elif answer == "3":
            self.healing()

    def healing(self):
        if self.hp <= 35:
            recovery = randint(*self.first_aid_kit) + 5
            print(f"{self.name} хорошо подлечился")
            self.hp_change(recovery)
        else:
            Person.healing(self)


def print_parameters():
    print("_" * 30)
    for parameter in ["name", "hp"]:
        print("|%4s" % parameter + "| ", end="")
        for person in players:
            print("%10s" % person.__dict__[parameter], end="|")
        print()
    print("_" * 30)


def choosing():
    active_person = choice(players)
    print(f"Ходииит...", end="")
    for i in range(3):
        sleep(0.7)
        print(".", end="")
    print(f"{active_person.name}!\n")
    sleep(1)
    return active_person


if __name__ == "__main__":
    
    your_name = input("Ваше имя: ", )
    computer_name = "Computer"
    player = Player(your_name, Person.hp)
    computer = Computer(computer_name, Person.hp)
    # Перекрёстные ссылки для использования методов:
    player.antagonist, computer.antagonist = computer, player
    players = [player, computer]
    while True:
        print_parameters()
        whose_move = choosing()
        whose_move.move()
        input("\n<Enter>")
