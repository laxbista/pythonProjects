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

moneyBox = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def resource_sufficiency(ingredients):
    """Returns true when order can be made, False if ingredients are insufficient"""
    for item in ingredients:
        if ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True


def process_coins():
    """Returns calculated total number of coins inserted"""
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Returns True when payment is accepted or False if money is insufficient"""
    if money_received >= drink_cost:
        global moneyBox
        change = round(money_received - drink_cost, 2)
        print(f"Here is your change ${change}")
        moneyBox += drink_cost
        return True
    else:
        print("Sorry not enough Money. Money refunded")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct required ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕")


is_on = True
while is_on:
    userChoice = input("What would you like? (espresso/latte/cappuccino): ")

    if userChoice == "off":
        is_on = False

    elif userChoice == "report":
        print("Current Resources Report:")
        print(f"Water: {resources['water']}mL")
        print(f"Milk: {resources['milk']}mL")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${moneyBox}")

    else:
        drink = MENU[userChoice]
        if resource_sufficiency(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(userChoice, drink["ingredients"])
