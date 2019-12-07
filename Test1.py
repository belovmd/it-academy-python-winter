print('Hello world!')

name = input('What is your name?\n')
print('Hi, %s.' % name)

friends = ['john', 'pat', 'gary', 'frea']
for i, name in enumerate(friends):
    print("iteration {iteration} is {name}".format(iteration=i, name=name))


def greet(name):
    print('Hello', name)


greet('jack')
greet('frea')
greet('fred')

# ---------------------------------------------------------

import re

for test_string in ['555-1212', 'ILL-EGAL']:
    if re.match(r'^\d{3}-\d{4}$', test_string):
        print(test_string, 'is a valid US local phone number')
    else:
        print(test_string, 'rejected')

# ---------------------------------------------------------------

price = {'apple': 0.40, 'bananas': 0.50, 'carrot': 0.30}
my_purchase = {
    'apple': 1,
    'bananas': 6,
    'carrot': 1
}

try:
    grocery_bill = sum(price[fruit] * my_purchase[fruit]
                       for fruit in my_purchase)
    print('$%.2f' % grocery_bill)
except ValueError:
    print('Something wrong')

# ----------------------------------------------------

from time import localtime

activities = {
    8: 'sleeping',
    9: 'commuting',
    17: 'working',
    18: 'commuting',
    20: 'eating',
    22: 'reasting'
}

try:
    time_now = localtime()
    hour = time_now.tm_hour
    for activity_time in sorted(activities.keys()):
        if hour < activity_time:
            print(activities[activity_time])
            break
        else:
            print("unknown, afk or sleeping")

except Exception:
    print('Something wrong')


# -------------------------------------------------------------

class BankAccount(object):
    def __init__(self, initial_balance):
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount

    def withdrawn(self, amount):
        self.balance -= amount

    def overdrawn(self):
        return self.balance < 100


my_account = BankAccount(100)
my_account.deposit(60)
my_account.withdrawn(80)

print(my_account.balance, my_account.overdrawn())
