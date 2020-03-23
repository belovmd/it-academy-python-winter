"""Создайте  модель из жизни. Это может быть бронирование комнаты в отеле,
 покупка билета в транспортной компании, или простая РПГ.
 Создайте несколько объектов классов,
 которые описывают ситуацию
 Объекты должны содержать как атрибуты так и методы класса
 для симуляции различных действий.
 Программа должна инстанцировать объекты и эмулировать
 какую-либо ситуацию - вызывать методы, взаимодействие объектов и т.д."""

from random import random


class Zybitskaya(object):
    def __init__(self, health=100, alcohol=0, cash=300, mood=50):
        self.health = health
        self.alcohol = alcohol
        self.cash = cash
        self.mood = mood

    def drink(self, shoots):
        for _ in range(shoots):
            if self.alcohol >= 100:
                print("You are drunk, comrade!")
            elif self.cash <= 0:
                print("Cash is empty! Go home!")
            else:
                self.alcohol += 10
                self.cash -= 15
                self.mood += 10
                self.health -= 5

    def dancing(self):
        if self.health <= 0:
            print("You haven't energy, not today!")
        else:
            self.alcohol -= 5
            self.health -= 15
            self.mood += 10
            self.cash -= 10

    def food(self):
        if self.cash <= 10:
            print("Sorry, comrade, you stay hungry!")
        elif self.health >= 50:
            print("You are not hungry! Go back to bar!")
        else:
            print("menu: kebab\n burger\n hotdog\n")
            food = input("What you will to eat? ").split()
            if 'kebeb' in food:
                self.health += 15
                self.cash -= 10
            if 'burger' in food:
                self.health += 12
                self.cash -= 15
            if 'hotdog' in food:
                self.health += 10
                self.cash -= 8

    def casino(self):
        if self.cash <= 10:
            print("Call taxi and go home!")
        else:
            self.cash -= 10
            result = random()
            if result > 0.5:
                print("Now you lucky!")
                self.cash += 15
            else:
                print("Loser!")

    def wayhome(self):
        print("Health = ", self.health, "Cash = ", self.cash, "Alcohol = ",
              self.alcohol, "Mood = ", self.mood)


evening = Zybitskaya()
evening.food()
evening.drink(5)
evening.dancing()
evening.food()
evening.casino()
evening.drink(10)
evening.food()
evening.wayhome()
