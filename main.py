from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

use_menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

is_on = True

while is_on:
    option = use_menu.get_items()
    choose = input(f"what would you like? {option}:")
    if choose == "off":
        is_on = False
    elif choose == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = use_menu.find_drink(choose)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)


