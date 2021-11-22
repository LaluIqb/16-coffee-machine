from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

is_stop = False
while not is_stop:

    option = menu.get_items()
    user_order = input(f'\tWhat would you like? ({option}): ')

    if user_order == "report":
        coffee_maker.report()
        money_machine.report()

    elif user_order == "off":
        is_stop = True

    elif user_order == "espresso" or user_order == "latte" or user_order == "cappuccino":
        drink = menu.find_drink(user_order)

        # Check resources first before jump into payment access
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
    else:
        continue
