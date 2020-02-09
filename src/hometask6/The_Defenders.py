"""It's the solution for task #1. This is the game "The_Warriors"
that I've started before. All descriptions are taken from checkio.org.
My RPG corresponds to your requirement for the task so I decided to
continue my job. Previous parts called "The_Warriors" and
"Army_Battles" are in Hometask4 and Hometask5 respectively
"""

# In the previous mission - Army battles, you've learned
# how to make a battle between 2 armies. But we have only
# 2 types of units - the Warriors and Knights. Let's add
# another one - the Defender. It should be the subclass
# of the Warrior class and have an additional defense parameter,
# which helps him to survive longer. When another unit hits
# the defender, he loses a certain amount of his health according to
# the next formula:
# enemy attack - self defense (if enemy attack > self defense).
# Otherwise, the defender doesn't lose his health.
# The basic parameters of the Defender:
# health = 60
# attack = 3
# defense = 2

"""Version The_Vampires: new class Vampire was added.
This class is the subclass of the Warrior class and
have the additional vampirism parameter, which helps him
to heal himself. When the Vampire hits the other unit,
he restores his health by +50% of the dealt damage (enemy
defense makes the dealt damage value lower). The basic
parameters of the Vampire:
health = 40
attack = 4
vampirism = 50%"""


class Warrior(object):
    health = 50
    attack = 5
    defense = 0
    is_alive = True

    def alive(self) -> bool:
        return self.health > 0

    # New function damage_to was created
    def damage_to(self, target: 'Warrior'):
        return self.attack - target.defense

    def fight(self, target: 'Warrior'):
        if self.attack > target.defense:
            target.health = target.health - (self.attack - target.defense)


class Knight(Warrior):
    attack = 7


"""New class Defender"""


class Defender(Warrior):
    health = 60
    attack = 3
    defense = 2


"""New class Vampire"""


class Vampire(Warrior):
    health = 40
    attack = 4
    vampirism = 0.5

    def fight(self, target: 'Warrior'):
        super(Vampire, self).fight(target)

        self.health = self.health + self.damage_to(target) * self.vampirism


class Army(object):
    """Initially, the army is an empty list."""

    def __init__(self):
        self.soldiers = []

    """The battle is going on while soldiers in Army are alive.
     Because of it, we need to know how many are there."""

    def __len__(self):
        return len(self.soldiers)

    """Soldiers are appended to the list according to their
     type and count."""

    def add_units(self, kind_of_soldier, count_soldiers: int):
        for _ in range(count_soldiers):
            self.soldiers.append(kind_of_soldier())


"""The battle is going on while soldiers in Army are alive."""


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


"""Fighting of two soldiers.
is_alive is a parameter that is set for each individual
soldier according to the task"""


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
    bob = Defender()
    mike = Knight()
    rog = Warrior()
    lancelot = Defender()
    eric = Vampire()
    adam = Vampire()
    richard = Defender()
    ogre = Warrior()

    assert fight(chuck, bruce), 'True'
    assert chuck.alive(), 'True'
    assert not bruce.alive(), 'False'
    assert not fight(dave, carl), 'False'
    assert carl.alive(), 'True'
    assert not dave.alive(), 'False'
    assert not fight(carl, mark), 'False'
    assert not carl.alive(), 'False'
    assert not fight(bob, mike), 'False'
    assert fight(lancelot, rog), 'True'
    assert not fight(eric, richard), "False"
    assert fight(ogre, adam), 'True'

    # battle tests
    my_army = Army()
    my_army.add_units(Defender, 2)
    my_army.add_units(Vampire, 2)
    my_army.add_units(Warrior, 1)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)
    enemy_army.add_units(Defender, 2)
    enemy_army.add_units(Vampire, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Defender, 4)

    army_4 = Army()
    army_4.add_units(Vampire, 3)
    army_4.add_units(Warrior, 2)

    battle = Battle()

    assert not battle.fight(my_army, enemy_army), 'False'
    assert battle.fight(army_3, army_4), 'True'
