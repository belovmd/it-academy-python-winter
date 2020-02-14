"""Создайте  модель из жизни. Это может быть бронирование комнаты
 в отеле, покупка билета в транспортной компании, или простая РПГ.
  Создайте несколько объектов классов, которые описывают ситуацию
  Объекты должны содержать как атрибуты так и методы класса для
  симуляции различных действий. Программа должна инстанцировать
  объекты и эмулировать какую-либо ситуацию - вызывать методы,
   взаимодействие объектов и т.д."""


class Wizard(object):
    def __init__(self, nickname, race='Wizard'):
        self.gold = 0
        self.nickname = nickname
        self.race = race
        self.level = 0
        self.health = 100
        self.my_exp = 0
        self.max_health = 100
        self.big_aid_kit = 1
        self.mid_aid_kit = 1
        self.small_aid_kit = 1

    def __str__(self):
        # Выводит статус нашего персонажа.
        return 'Nickname: {}; Race: {}; Level: {}; Health : {}' \
            .format(self.nickname, self.race, self.level, self.health)

    def my_gold(self):
        # Выводит все золото
        return 'У игрока {} осталось {} золота.' \
            .format(self.nickname, self.gold)

    def my_aids_kit(self):
        # Выводит все наши аптечки
        return 'У игрока {} осталось аптечек: Big: {}, Mid: {}, Small: {}' \
            .format(self.nickname,
                    self.big_aid_kit, self.mid_aid_kit, self.small_aid_kit)

    def enemies(self, count_enemy, damage=3.0, increase_exp_lvl=5):
        # за каждого врага мы получаем 1 exp;
        # с каждым уровнем надо больше получить exp;
        # с каждым уровнем уменьшается damage
        for i in range(count_enemy):
            self.gold += 2  # за одного врага
            self.health -= damage
            self.my_exp += 1.1
            if self.my_exp >= increase_exp_lvl:
                self.level += 1
                damage -= 0.1
                increase_exp_lvl += 2
                self.my_exp = 0
                # смерть персонажа: теряем 1 level,
                # восстанавливается health на 100 %, теряем 10% gold,
                # врагов рядом нет - enemy = 0
            elif self.health <= 0:
                self.health = self.max_health
                self.level -= 1
                self.gold *= 0.9
                break

    def regeneration(self, aid_kit):
        # Мои аптечки. При использовании увеличевается health
        # и из my_aids_kit исчезает использованная аптечка
        if aid_kit == 'big':
            if self.big_aid_kit - 1 >= 0:
                self.big_aid_kit -= 1
                self.health += 20
            else:
                print('Большая аптечка отсутствует')
        elif aid_kit == 'mid':
            if self.mid_aid_kit - 1 >= 0:
                self.mid_aid_kit -= 1
                self.health += 10
            else:
                print('Средняя аптечка отсутствует')
        elif aid_kit == 'small':
            if self.small_aid_kit - 1 >= 0:
                self.small_aid_kit -= 1
                self.health += 5
            else:
                print('Малая аптечка отсутствует')
        if self.health > self.max_health:
            self.health = self.max_health

    def my_shop(self, **kwargs):
        # Магазин аптечек. В shop_aid_kit указанна какая аптека и цена аптечки.
        # На ввод получаем словарь с названием аптечки и количество которое нам надо
        shop_aid_kit = {'big': 20, 'mid': 15, 'small': 10}
        for i in kwargs:
            if i in shop_aid_kit:
                if self.gold - (shop_aid_kit[i] * kwargs[i]) < 0:
                    print('Вам не хватает {} золота на покупку'.
                          format(abs(self.gold - (shop_aid_kit[i] * kwargs[i]))))
                    break
                else:
                    self.gold -= shop_aid_kit[i] * kwargs[i]
                if i == 'big':
                    self.big_aid_kit += kwargs[i]
                elif i == 'mid':
                    self.mid_aid_kit += kwargs[i]
                elif i == 'small':
                    self.small_aid_kit += kwargs[i]
                else:
                    print('Такой аптечки нет, попробуйте еще раз.')


class Troll(Wizard):
    # Расса Troll у которой health больше на 50
    #  и получаемый урон меньше чем у Wizard. При этом Troll
    #  получает менше exp чем Wizard
    def __init__(self, nickname, race='Troll'):
        super().__init__(nickname, race)
        self.health = 150
        self.max_health = 150

    def enemies(self, count_enemy, damage=2.6, increase_exp_lvl=8):
        super().enemies(count_enemy, damage, increase_exp_lvl)


blackmamba = Wizard('blackmamba')
blackmamba.enemies(34)
blackmamba.my_shop(big=1)
print(blackmamba)
blackmamba.regeneration('big')
blackmamba.my_shop(big=1, mid=1)
blackmamba.my_shop(mid=1)
blackmamba.regeneration('small')
print(blackmamba.my_aids_kit())
print(blackmamba.my_gold())
print(blackmamba)
amour = Troll('amour')
amour.enemies(35)
print(amour.my_aids_kit())
print(amour.my_gold())
print(amour)
amour.regeneration('big')
amour.my_shop(mid=1)
print(amour)
print(amour.my_aids_kit())
print(amour.my_gold())
