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

def make_drink(drink):
    if drink == "capuccino":
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
    if drink == "capuccino":
        if resources["milk"] > MENU["cappuccino"]["ingredients"]["milk"]:
            if resources["water"] > MENU["cappuccino"]["ingredients"]["water"]:
                if resources["coffee"] > MENU["cappuccino"]["ingredients"]["coffee"]:
                    make_drink()
                else:
                    print("There is not enough coffee in the machine to make the drink.")
            else:
                print("There is not enough water in the machine to make the drink.")
        else:
            print("There is not enough milk in the machine to make the drink.")

    elif drink == "espresso":
        if resources["milk"] > MENU["espresso"]["ingredients"]["milk"]:
            if resources["water"] > MENU["espresso"]["ingredients"]["water"]:
                if resources["coffee"] > MENU["espresso"]["ingredients"]["coffee"]:
                    make_drink()
                else:
                    print("There is not enough coffee in the machine to make the drink.")
            else:
                print("There is not enough water in the machine to make the drink.")
        else:
            print("There is not enough milk in the machine to make the drink.")
    elif drink == "latte":
        if resources["milk"] > MENU["latte"]["ingredients"]["milk"]:
            if resources["water"] > MENU["latte"]["ingredients"]["water"]:
                if resources["coffee"] > MENU["latte"]["ingredients"]["coffee"]:
                    make_drink()
                else:
                    print("There is not enough coffee in the machine to make the drink.")
            else:
                print("There is not enough water in the machine to make the drink.")
        else:
            print("There is not enough milk in the machine to make the drink.")



drink = "on"
while drink != "off":
    drink = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if drink == "report":
        report()

    if drink == "capuccino":
        check_resources()





