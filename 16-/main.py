from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


Menu = Menu()
# MenuItem =
CoffeeMaker = CoffeeMaker()
MoneyMachine = MoneyMachine()

drinks = Menu.get_items()

cost = 0

for item in Menu.menu:
    cost = item.cost


name = "on"
while name != "off":
    name = input(f"What would you like to drink?: {drinks}").lower()
    if name == "report":
        CoffeeMaker.report()
        MoneyMachine.report()
    if Menu.find_drink(name) and CoffeeMaker.is_resource_sufficient(Menu.find_drink(name)):
        if MoneyMachine.make_payment(cost):
            CoffeeMaker.make_coffee(Menu.find_drink(name))

# key learning points:
# - read the documentation of all the classes
#   - it clearly says things like: certain methods return the MenuItem instance.
#   - therefore, it would have been easier to say: drink = Menu.find_drink(name) and then all the other code would be more concise
#   - an instance of a class is normally always lowercase

