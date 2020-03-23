# Игра с компьютером

# Рандом может выбирать одного игрока несколько раз подряд,
# и игра может получится как долгой, так и быстрой.

from random import choice
from random import randint
from time import sleep


class Person(object):
    antagonist = None
    hp = 30
    max_HP = hp
    simple_damage = [18, 25]
    special_damage = [10, 35]
    first_aid_kit = [15, 25]
    actions = [f"1. simple kick,"
               f" {simple_damage[0]}-{simple_damage[1]} damage",
               f"2. special kick,"
               f" {special_damage[0]}-{special_damage[1]} damage",
               f"3. first aid kit, restore"
               f" {first_aid_kit[0]}-{first_aid_kit[1]} HP"]

    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def hp_change(self, change):
        self.hp += change
        if change > 0:
            if self.hp >= self.max_HP:
                self.hp = self.max_HP
                print(f"{self.name} has {self.max_HP} HP again!")
            else:
                print(f"{self.name} restore {change} HP."
                      f" He has {self.hp} HP now.")
        else:
            if self.hp <= 0:
                print(f"\n{self.name} lost")
                input("\n<Enter>")
                exit(0)
            else:
                print(f"{self.name} lost {-change} HP!"
                      f" He has {self.hp} HP now!")

    def simple_kick(self):
        damage = randint(*self.simple_damage)
        print(f"{self.name} banging simple kick")
        self.antagonist.hp_change(-damage)

    def special_kick(self):
        damage = randint(*self.special_damage)
        print(f"{self.name} banging special kick!")
        self.antagonist.hp_change(-damage)

    def healing(self):
        recovery = randint(*self.first_aid_kit)
        print(f"{self.name} used first aid kit")
        self.hp_change(recovery)


class Player(Person):

    def move(self):
        for action in Person.actions:
            print(action)
        if self.hp <= 10 and self.hp != computer.hp:
            print("666. sector 'chance' at the drum!)")
        print("entering arbitrary characters will mean skipping a move")
        print()
        answer = input(f"Select an action, {self.name}: ", )
        if answer == "1":
            self.simple_kick()
        elif answer == "2":
            self.special_kick()
        elif answer == "3":
            self.healing()
        # Следующий ответ можно ввести на любом ходу,
        # но это может сыграть и против игрока)
        elif answer == "666":
            print("The enemy already felt the taste of victory and relaxed,"
                  "\nbut with the last of your strength you serious banged him"
                  "\n and have balanced health!"
                  "\n  May the force be with you!)")
            computer.hp = self.hp


class Computer(Person):

    def move(self):
        if self.hp == self.max_HP:
            answer = randint(1, 2)
        else:
            answer = randint(1, 3)
        if answer == 1:
            self.simple_kick()
        elif answer == 2:
            self.special_kick()
        elif answer == 3:
            if self.hp <= 30:
                self.healing()
            else:
                Person.healing(self)

    def healing(self):
        recovery = randint(*self.first_aid_kit) + 8
        print(f"{self.name} good restored")
        self.hp_change(recovery)


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
    print(f"This is move by...", end="")
    for i in range(3):
        sleep(0.7)
        print(".", end="")
    print(f"{active_person.name}!\n")
    sleep(1)
    return active_person


if __name__ == "__main__":
    your_name = input("Your name: ", )[:10]
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
