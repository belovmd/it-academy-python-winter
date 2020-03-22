"""Создайте  модель из жизни. Это может быть бронирование комнаты
 в отеле, покупка билета в транспортной компании, или простая РПГ.
  Создайте несколько объектов классов, которые описывают ситуацию
  Объекты должны содержать как атрибуты так и методы класса для
  симуляции различных действий. Программа должна инстанцировать
  объекты и эмулировать какую-либо ситуацию - вызывать методы,
   взаимодействие объектов и т.д."""


# This is a game with 2 character classes.
# Enemies - regular mobs to damage you.
# When you kill enemies you get experience, level, gold and lose health.
# When you die you lose gold and experience
class Hero(object):
    def __init__(self, nickname, class_hero):
        self.gold = 0
        self.nickname = nickname
        self.class_hero = class_hero
        self.level = 1
        self.health = 100
        self.my_exp = 0
        self.max_health = 100

    def __str__(self):
        return 'Nickname: {}; Class: {}; Level: {}; Health : {}: Exp : {}' \
            .format(self.nickname,
                    self.class_hero,
                    self.level,
                    self.health,
                    self.my_exp)


class Paladin(Hero):

    def __init__(self, nickname, class_hero):
        super().__init__(nickname, class_hero)
        self.health = 150
        self.max_health = 150


class Wizard(Hero):
    def __init__(self, nickname, class_hero):
        super().__init__(nickname, class_hero)


class Bag(object):
    def __init__(self):
        self.gold = 20
        self.my_cure = {'big_cure': 1, 'mid_cure': 1, 'small_cure': 1}

    def my_money(self):
        return 'You have {} gold'.format(self.gold)

    def my_aids_kits(self):
        return 'You have {} aid kits'.format(self.my_cure)


class Shop(object):
    # It is a price of aid kit and count health that it regenerates
    shop_cure = {'big_cure': 20, 'mid_cure': 15, 'small_cure': 10}

    def buy(self, my_buy, buyer):
        if my_buy in self.shop_cure and \
                buyer[1].gold >= self.shop_cure[my_buy]:
            buyer[1].my_cure[my_buy] += 1
            buyer[1].gold -= self.shop_cure[my_buy]
        elif my_buy not in self.shop_cure:
            print("{} don't exist".format(my_buy))
        else:
            print("Not enough gold!")


class Enemy(object):
    damage = 3


def regeneration(cure, hero):
    if cure in hero[1].my_cure and hero[1].my_cure[cure] != 0:
        hero[1].my_cure[cure] -= 1
        hero[0].health += shop.shop_cure[cure]
        if hero[0].health >= hero[0].max_health:
            hero[0].health = hero[0].max_health
    elif cure not in hero[1].my_cure:
        print("{} don't exist".format(cure))
    else:
        print("You don't have {}".format(cure))


def fight(enemies, hero):
    # If you die, you appear on another place with full health,
    # without enemies
    # you lose gold and exp
    exp_for_fight = 4
    for en in range(enemies):
        hero[0].health -= enemy.damage
        hero[0].my_exp += 1
        hero[1].gold += 1
        if hero[0].my_exp >= 30:
            hero[0].level += 1
            exp_for_fight -= 0.4
            enemy.damage -= 0.2
            hero[0].my_exp = 0
        elif hero[0].health <= 0:
            hero[0].health = hero[0].max_health
            hero[0].my_exp = 0
            hero[0].gold -= 10
            print('You died!')
            break


# instance[0] == it is a specifications of character
# instance[1] == it is a Bag with gold and aid kits of character
alex = Wizard('alex', 'Wizard'), Bag()
amour = Paladin('amour', 'Paladin'), Bag()
shop = Shop()
enemy = Enemy()
print(alex[0])
fight(20, alex)
print(alex[0])
fight(33, amour)
print(amour[0])
regeneration('big_cure', amour)
print(amour[0])
fight(20, amour)
print(amour[0])
regeneration('mid_cure', amour)
print(amour[0])
shop.buy('big_cure', amour)
regeneration('big_cure', amour)
fight(20, amour)
print(amour[0])
print(amour[1].my_aids_kits())
print(amour[1].my_money())
print(alex[1].my_money())
shop.buy('big_cure', amour)
fight(20, amour)
print(amour[1].my_money())
print(amour[0])
