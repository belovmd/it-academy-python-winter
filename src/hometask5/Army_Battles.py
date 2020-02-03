# In this mission your task is to add new classes
# and functions to the existing ones. The new class
# should be the Army and have the method add_units() -
# for adding the chosen amount of units to the army.
# The first unit added will be the first to go to fight,
# the second will be the second, ...
# Also you need to create a Battle() class with a fight() function,
# which will determine the strongest army.
# The battles occur according to the following principles:
# at first, there is a duel between the first warrior of the first
# army and the first warrior of the second army.
# As soon as one of them dies - the next warrior from the army
# that lost the fighter enters the duel, and the surviving warrior
# continues to fight with his current health.
# This continues until all the soldiers of one of the armies die.
# In this case, the battle() function should return True,
# if the first army won, or False, if the second one was stronger.
# Note that army 1 have the advantage to start every fight!


class Warrior(object):
    health = 50
    attack = 5
    is_alive = True

    def alive(self) -> bool:
        return self.health > 0

    def fight(self, target: 'Warrior'):
        target.health -= self.attack


class Knight(Warrior):
    attack = 7


class Army(object):
    """Изначально армия - пустой список"""

    def __init__(self):
        self.soldiers = []

    """Поскольку сражение происходит, пока не умрут все
     воины одной армии, необходимо знать их количество"""

    def __len__(self):
        return len(self.soldiers)

    """В список добавляются солдаты по принципу:
    тип солдата, количество солдат данного типа"""

    def add_units(self, kind_of_soldier, count_soldiers: int):
        for _ in range(count_soldiers):
            self.soldiers.append(kind_of_soldier())


"""Сражение происходит до тех пор, пока все солдаты одной
из армий не погибнут"""


class Battle(object):
    def fight(self, first_army: 'Army', second_army: 'Army') -> bool:
        while len(first_army) > 0 and len(second_army) > 0:
            first_soldier_won = fight(first_army.soldiers[0],
                                      second_army.soldiers[0])
            if first_soldier_won:
                second_army.soldiers.pop(0)
            else:
                first_army.soldiers.pop(0)

        return len(first_army) > 0


"""Сражение двух солдат.
is_alive устанавливается для каждого отдельного солдата,
т.к. это требуется по условию задачи"""


def fight(soldier1: 'Warrior', soldier2: 'Warrior') -> bool:
    fighter_counter = 0

    while True:
        fighter_counter += 1
        soldier1.fight(soldier2)
        if not soldier2.alive():
            soldier2.is_alive = False
            return True

        soldier2.fight(soldier1)
        if not soldier1.alive():
            soldier1.is_alive = False
            return False


if __name__ == '__main__':

    # fight tests
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    assert fight(chuck, bruce), 'True'
    assert chuck.alive(), 'True'
    assert not bruce.alive(), 'False'
    assert not fight(dave, carl), 'False'
    assert carl.alive(), 'True'
    assert not dave.alive(), 'False'
    assert not fight(carl, mark), 'False'
    assert not carl.alive(), 'False'

    # battle tests
    my_army = Army()
    my_army.add_units(Knight, 3)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 20)
    army_3.add_units(Knight, 5)

    army_4 = Army()
    army_4.add_units(Warrior, 30)

    battle = Battle()

    assert battle.fight(my_army, enemy_army), 'True'
    assert not battle.fight(army_3, army_4), 'False'
