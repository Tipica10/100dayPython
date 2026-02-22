MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost":1.5,
    },
    "latte": {
            "ingredients": {
                "water": 200,
                "milk": 150,
                "coffee": 24,
            },
            "cost":2.5,
        },
    "cappuccino": {
            "ingredients": {
                "water": 250,
                "milk": 100,
                "coffee": 24,
            },
            "cost":3.0,
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def report():
    for item in resources:
        print(f"{item}: {resources[item]}")

def new_resources(drink):
    if drink == "cappuccino":
        resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
        resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]
        resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
    if drink == "espresso":
        resources["water"] -= MENU["espresso"]["ingredients"]["water"]
        resources["milk"] -= MENU["espresso"]["ingredients"]["milk"]
        resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
    if drink == "latte":
        resources["water"] -= MENU["latte"]["ingredients"]["water"]
        resources["milk"] -= MENU["latte"]["ingredients"]["milk"]
        resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]



def check_resources(drink):
    if resources["milk"] > MENU[drink]["ingredients"]["milk"]:
        if resources["water"] > MENU[drink]["ingredients"]["water"]:
            if resources["coffee"] > MENU[drink]["ingredients"]["coffee"]:
                print("sufficient resources")
            else:
                print("There is not enough coffee in the machine to make the drink.")
        else:
            print("There is not enough water in the machine to make the drink.")
    else:
        print("There is not enough milk in the machine to make the drink.")

def process_coins(drink):
    quarters = int(input("How many quarters do you have?: "))
    dimes = int(input("How many dimes do you have?: "))
    nickels = int(input("How many nickels do you have?: "))
    pennies = int(input("How many pennies do you have?: "))

    Total_money = (quarters *0.25) + (dimes * 0.10) * (nickels * 0.05) + (pennies * 0.01)

    if Total_money < MENU[drink]["cost"]:
        print("You do not have enough money. Money refunded.")
    else:
        change = Total_money - MENU[drink]["cost"]
        print(f"Here is your {drink} and {change}")



drink = "on"
while drink != "off":
    drink = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if drink == "report":
        report()

    if drink == "cappuccino":
        if check_resources("cappucino") == "sufficient resources":
            if process_coins("cappucino") == "Here is your {drink} and {change}":
                new_resources("cappucino")
    elif drink == "espresso":
        if check_resources("espresso") == "sufficient resources":
            if process_coins("espresso") == "Here is your {drink} and {change}":
                new_resources("espresso")
    elif drink == "latte":
        if check_resources("latte") == "sufficient resources":
            if process_coins("latte") == "Here is your {drink} and {change}":
                new_resources("latte")
    else:
        print("Invalid input!")








