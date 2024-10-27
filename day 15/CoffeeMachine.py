from platform import machine
from tabnanny import check

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

# resources = {
#     "water": 300,
#     "milk": 200,
#     "coffee": 100,
# }


# TODO: 1. Print report of all coffee machine resource
def print_report(current_resource, current_money):
    print(f"Water: {current_resource['water']}ml")
    print(f"Milk: {current_resource['milk']}ml")
    print(f"Coffee: {current_resource['coffee']}g")
    print(f"Money: ${current_money}")

# print_report()

# TODO: 3. Check resources sufficient to make drink order
def check_resources(current_resource, drink_order):
    """this function take drink_order as input and return resource sufficient is True or False"""
    not_enough_resource = []
    for key in current_resource:
        try:
            required_resource = MENU[drink_order]["ingredients"][key]
        except KeyError:
            required_resource = 0
        if current_resource[key] < required_resource:
            not_enough_resource.append(key)

    if len(not_enough_resource) == 0:
        return True
    else:
        print(f"Sorry there is not enough {', '.join(not_enough_resource)}.")
        return False


# TODO: 4. Process coins
def process_coin():
    print("Please insert coins.")
    quarter = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    amount = quarter * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    return amount


# TODO: 5. Check transaction successful
def check_transaction(drink_order, paid):
    "This function take drink order and paid amount as input and return True/False if paid more than cost"
    cost = MENU[drink_order]['cost']
    if paid >= cost:
        change = paid - cost
        print(f"Here is ${change} in change.")
        return True
    else:
        print(f"Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(current_resource, drink_order, current_money):
    for key in current_resource:
        try:
            required_resource = MENU[drink_order]["ingredients"][key]
        except KeyError:
            required_resource = 0
        current_resource[key] = current_resource[key] - required_resource

    current_money += MENU[drink_order]["cost"]

    print(f"Here is your {drink_order}☕ Enjoy!")
    return current_resource, current_money


# TODO: 2. Prompt user by asking "What would you like" (espresso/latte/cappuccino):"
def order():

    resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
    }

    money = 0
    machine_status = "on"

    while machine_status != "off":
        user_order = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if user_order == "report":
            print_report(resources, money)
        elif user_order == "off":
            machine_status = "off"
        elif user_order in MENU.keys():
            enough_resource = check_resources(resources, user_order)
            if enough_resource:
                paid_amount = process_coin()
                enough_coin = check_transaction(user_order, paid_amount)
                if enough_coin:
                    resources, money = make_coffee(resources, user_order, money)



order()
