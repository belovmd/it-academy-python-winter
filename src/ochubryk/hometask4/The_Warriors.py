# Let's start with the simple task - one-on-one duel. You need
# to create the class Warrior, the instances of which will have
# 2 parameters - health (equal to 50 points) and attack (equal
# to 5 points), and 1 property - is_alive, which can be True (if
# warrior's health is > 0) or False (in the other case).
# In addition you have to create the second unit type - Knight,
# which should be the subclass of the Warrior but have the
# increased attack - 7. Also you have to create a function
# fight(), which will initiate the duel between 2 warriors and
# define the strongest of them. The duel occurs according to
# the following principle:
# Every turn, the first warrior will hit the second and this
# second will lose his health in the same value as the attack
# of the first warrior. After that, if he is still alive, the
# second warrior will do the same to the first one.
# The fight ends with the death of one of them. If the first
# warrior is still alive (and thus the other one is not anymore),
# the function should return True, False otherwise.


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


def fight(unit_1: 'Warrior', unit_2: 'Warrior') -> bool:
    while True:
        unit_1.fight(unit_2)
        if not unit_2.alive():
            unit_2.is_alive = False
            return True

        unit_2.fight(unit_1)
        if not unit_1.alive():
            unit_1.is_alive = False
            return False


if __name__ == '__main__':
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
