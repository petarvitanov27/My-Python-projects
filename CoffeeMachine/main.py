
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

def calc():
    quarters = float(input("How many quarters would you like to insert? "))
    dimes = float(input("How many dimes would you like to insert? "))
    nickles = float(input("How many nickles would you like to insert? "))
    pennies = float(input("How many pennies would you like to insert? "))
    change = 0
    total = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    if total > MENU[choice]["cost"]:
        change = total - MENU[choice]["cost"]
        print(f"Here are ${round(change, 2)} in change")
        resources["money"] += MENU[choice]["cost"]
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False

def make_coffee():
    for item in MENU[choice]["ingredients"]:
        resources[item] -= MENU[choice]["ingredients"][item]



in_use = True
while in_use:
    choice = input("What would you like? (espresso/latte/cappuccino):")
    if choice == "off":
        in_use = False
    elif choice == "report":
        print(f"Water: {resources["water"]}")
        print(f"Milk: {resources["milk"]}")
        print(f"Coffee: {resources["coffee"]}")
        print(f"Money: {resources["money"]}")
    else:
        for item in resources:
            if resources[item] > MENU[choice]["ingredients"][item]:
                if calc() == True:
                    make_coffee()
                    print(f"Here is your {choice}")
                    break
                    in_use = False
                else:
                    break
                    in_use = False
            else:
                print(f"Sorry, there is not enough {item}")
                in_use = False
                break