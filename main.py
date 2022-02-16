from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffeeMaker = CoffeeMaker()
menu = Menu()
moneyMachine = MoneyMachine()

while True:
    selection = input("What would you like? " + menu.get_items()).lower()

    if selection == "off":
        quit()
    elif selection == "report":
        coffeeMaker.report()
        moneyMachine.report()
        continue

    drink = menu.find_drink(selection)
    if drink and drink.name in menu.get_items() and coffeeMaker.is_resource_sufficient(drink) and \
            moneyMachine.make_payment(drink.cost):
        coffeeMaker.make_coffee(drink)
