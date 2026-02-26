from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


Menu = Menu()
MenuItem =
CoffeeMaker = CoffeeMaker()
MoneyMachine = MoneyMachine()

drinks = Menu.get_items()

name = "on"
while name != "off":
    name = input(f"What would you like to drink?: {drinks}").lower()
    if name == "report":
        CoffeeMaker.report()
        MoneyMachine.report()
    if name == Menu.find_drink(name):
        if CoffeeMaker.is_resource_sufficient(name):
            MoneyMachine.process_coins()
            if MoneyMachine.make_payment()



