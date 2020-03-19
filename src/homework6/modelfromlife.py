import random

"""Создайте  модель из жизни. Это может быть бронирование комнаты в
отеле, покупка билета в транспортной компании, или простая РПГ.
Создайте несколько объектов классов, которые описывают ситуацию
Объекты должны содержать как атрибуты так и методы класса для
симуляции различных действий. Программа должна инстанцировать
объекты и эмулировать какую-либо ситуацию - вызывать методы,
взаимодействие объектов и т.д.

"""


class Casino(object):

    def __init__(self, name):
        self.list_guests = list_guests[:]
        self.name = name
        self.roulette_table = [val for val in range(37)]
        self.blackjack_deck = [1, 2, 3, 4, 5, 6, 7,
                               8, 9, 10, 10, 10, 10
                               ]
        self.one_hand_bandit_ = [1, 2, 3, 4, 5, 6, 7]
        self.start_capital = 10000
        self.capital = 10000
        self.roulette_players = []
        self.blackjack_players = []
        self.bar_visitors = []

    def roulette(self, players):
        # Here guests place bets.
        for time in range(3):
            bets = {}
            for person in players:
                if person.do_i_have_cash():
                    bets.setdefault(person.bet_roulette())
            self.all_bets_are_off(bets)
            bets.clear()

    def all_bets_are_off(self, bets):
        # It is a very simple simulation roulette. Only numbers
        # played in this simulation. Guests can't place bet for a
        # zero because a casino always win.
        roulette_round = random.choice(self.roulette_table)
        for person in bets:
            if person[1][0] == roulette_round:
                self.capital -= (person[1][1] * 35)
                self.won(person[0], person[1][1] * 36)
            else:
                self.capital += person[1][1]

    def one_hand_bandit(self, person):
        if person.do_i_have_cash():
            bet = person.bet_one_hand()
            win_ratio = 1
            random.shuffle(self.one_hand_bandit_)
            column_1 = self.one_hand_bandit_[2:5]
            random.shuffle(self.one_hand_bandit_)
            column_2 = self.one_hand_bandit_[2:5]
            random.shuffle(self.one_hand_bandit_)
            column_3 = self.one_hand_bandit_[2:5]
            if column_1[0] == column_2[0] == column_3[0]:
                win_ratio += 1
            if column_1[1] == column_2[1] == column_3[1]:
                if column_1[1] == column_2[1] == column_3[1] == 7:
                    win_ratio += 3
                else:
                    win_ratio += 1
            if column_1[2] == column_2[2] == column_3[2]:
                win_ratio += 1
            if win_ratio > 1:
                self.capital -= bet * (win_ratio - 1)
                self.won(person, bet * win_ratio)
            else:
                self.capital += bet

    def blackjack(self, persons_list):
        # It simulation does't use different ace values.
        cards = self.blackjack_deck[:] * 4
        random.shuffle(cards)
        players = []
        croupier_hand = [cards.pop(0), cards.pop(1)]
        for person in persons_list:
            if person.do_i_have_cash():
                bet = person.bet_blackjack()
                hand = [cards.pop(0), cards.pop(1)]
                one_more = person.get_hand(hand)
                players.append([person, bet, hand, one_more])
        while any(param[-1] for param in players):
            for person in players:
                if person[-1]:
                    person[2].append(cards.pop(0))
                    person[-1] = person[0].get_hand(person[2])
        while sum(croupier_hand) < 17:
            croupier_hand.append(cards.pop(0))
        for person in players:
            if 22 > sum(person[2]) > sum(croupier_hand):
                self.won(person[0], person[1] * 2)
                self.capital -= person[1]
            else:
                self.capital += person[1]

    def won(self, person, pot):
        person.current_place = 'bar'
        person.woo_hoo(pot)
        person.money += pot

    def security(self, person):
        if person in self.roulette_players:
            self.roulette_players.remove(person)
        if person in self.blackjack_players:
            self.blackjack_players.remove(person)
        if person in self.bar_visitors:
            self.bar_visitors.remove(person)
        self.list_guests.remove(person)

    def __str__(self):
        return ('Casino profit is {} dollars'
                .format(self.capital - self.start_capital))


class Bar(object):

    @classmethod
    def bar(self, guests):
        bar_visitors = guests
        drinks = {'mojito': (1, 10),
                  'bud': (1, 5),
                  'vodka': (2, 10),
                  'jimbeam': (2, 15),
                  'chivas': (2, 50)}
        for person in bar_visitors:
            the_picked_drink = random.choice(person.prefer_drink)
            print('{} is drinking a glass of {}'
                  .format(person.name, the_picked_drink))
            person.drunk += drinks[the_picked_drink][0]
            person.money -= drinks[the_picked_drink][1]
            with_blackjack.capital += drinks[the_picked_drink][1]
        with_blackjack.bar_visitors.clear()


class UsualGuest(object):

    def __init__(self, name):
        self.name = name
        list_guests.append(self)
        self.money = 2500
        self.drunk = 1
        self.start_bet = 5
        self.prefer_place = ['roulette', 'blackjack', 'one-hand bandit']
        self.current_place = ''
        self.go_to_the_bar = True
        self.prefer_drink = ['bud', 'jimbeam']

    def choice_place(self):
        if self.current_place == 'bar' and self.go_to_the_bar:
            self.go_to_the_bar = False
        else:
            self.go_to_the_bar = True
            self.current_place = random.choice(self.prefer_place)

    def do_i_have_cash(self):
        if self.money - (self.start_bet * self.drunk) <= 0:
            self.gameover()
            return False
        else:
            return True

    def woo_hoo(self, pot):
        print(f'{self.name}: WOO-HOO! I win {pot} dollars!')

    def gameover(self):
        if self.drunk > 7:
            print(str.upper('give me back my money!1!!!111'))
        with_blackjack.security(self)

    def bet_roulette(self):
        bet = random.choice(range(1, 37))
        self.money -= self.start_bet * self.drunk
        return self, (bet, self.start_bet * self.drunk)

    def bet_blackjack(self):
        self.money -= (self.start_bet * self.drunk)
        return (self.start_bet * self.drunk)

    def get_hand(self, hand):
        if sum(hand) <= 17:
            return True
        else:
            return False

    def bet_one_hand(self):
        self.money -= self.start_bet * self.drunk
        return self.start_bet * self.drunk

    def __str__(self):
        return ('{} has {} dollars and drank {} glasses some drinks.'
                .format(self.name, self.money, self.drunk))


class VipGuest(UsualGuest):

    def __init__(self, name):
        super().__init__(name)
        self.money = 10000
        self.start_bet = 100
        self.prefer_place = ['roulette', 'blackjack']
        self.prefer_drink = ['chivas']


class OldGuest(UsualGuest):

    def __init__(self, name):
        super().__init__(name)
        self.money = 1000
        self.start_bet = 1
        self.prefer_place = ['blackjack', 'one-hand bandit']
        self.prefer_drink = ['bud', 'mojito']


class ChinaTourist(UsualGuest):

    def __init__(self, name):
        super().__init__(name)
        self.money = 1500
        self.start_bet = 15
        self.prefer_place = ['roulette', 'one-hand bandit']
        self.prefer_drink = ['vodka', 'mojito']

    def gameover(self):
        if self.drunk > 5:
            print('把钱还给我！ 该死！ 狗儿子')
        with_blackjack.security(self)


def cycle(times):
    # It is a main function in this program, it start a interplay
    # after instanced all objects.
    # One cycle equal 15 minutes, 3 rounds of roulette,
    # 4 rounds of blackjack, 5 rounds of
    # one-hand bandit, 1 glass some drink in a bar.
    # Persons have parameter - а prefer_place, random.chouce() picks
    # a current place in it. Person goes to the bar after win.

    for time in range(times):
        if with_blackjack.list_guests:
            for person in with_blackjack.list_guests:
                person.choice_place()
                if person.current_place == 'roulette':
                    with_blackjack.roulette_players.append(person)
                if person.current_place == 'blackjack':
                    with_blackjack.blackjack_players.append(person)
                if person.current_place == 'one-hand bandit':
                    with_blackjack.one_hand_bandit(person)
                if person.current_place == 'bar':
                    with_blackjack.bar_visitors.append(person)
            with_blackjack.roulette(with_blackjack.roulette_players)
            with_blackjack.roulette_players.clear()
            with_blackjack.blackjack(with_blackjack.blackjack_players)
            with_blackjack.blackjack_players.clear()
            Bar.bar(with_blackjack.bar_visitors)
            with_blackjack.bar_visitors.clear()
            print(with_blackjack)
        else:
            break


if __name__ == '__main__':
    list_guests = []
    guest1 = UsualGuest('Vasya')
    guest2 = UsualGuest('Petua')
    guest3 = UsualGuest('John')
    guest4 = UsualGuest('Donny')
    guest5 = VipGuest('James Bond')
    guest6 = VipGuest('Vicar of Christ')
    guest7 = OldGuest('Grandpa')
    guest8 = OldGuest('Granny')
    guest9 = ChinaTourist('Jackie')
    guest10 = ChinaTourist('Senior Vong')
    with_blackjack = Casino('with_blackjack')

    cycle(300)

    for person in list_guests:
        print(person)
    print(with_blackjack)
