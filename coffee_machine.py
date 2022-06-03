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
}

def resources_sufficient(order_ingredients):
    for ele in order_ingredients:
        if order_ingredients[ele] >= resources[ele]:
            print(f"Sorry there is not enough {ele}.")
            return False
    return True

def process_coins():
    print("Please insert Coins:")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: " )) * 0.1
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

profit = 0

def transaction_successful(money_received, drink_cost):
    global profit
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is your ${change} change.")
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is you {drink_name}. Enjoy your coffee and have a good day.")

should_continue = True

def main():
    global should_continue
    while should_continue:
        choose = input("What would you like? (espresso, latte, cappuccino): ")
        if choose == "report":
            print(f"water: {resources['water']}ml\nmilk: {resources['milk']}ml\ncoffee: {resources['coffee']}gm\nMoney: ${profit}")
        elif choose == "off":
            should_continue = False
        else:
            drink = MENU[choose]
            if resources_sufficient(drink["ingredients"]):
                payment = process_coins()
                if transaction_successful(payment, drink["cost"]):
                    make_coffee(choose, drink["ingredients"])

main()