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

account = 0
profit = 0
resources = {   
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def make_coffee(type_coffee):
    global account
    global profit
    ingredients = MENU[type_coffee]["ingredients"]
    enough_resources = True
    for ingredient, amount in ingredients.items():
        if resources[ingredient] < amount:
            enough_resources = False
            print(f"Sorry there is not enough {ingredient}")
            break
    if account >= MENU[type_coffee]["cost"]:
        if enough_resources:
            for ingredient, amount in ingredients.items():
                resources[ingredient] -= amount
            price = MENU[type_coffee]["cost"]
            change = account - price
            print(f"Here is ${change:.2f} in change.")
            print(f"Here is your {type_coffee} ☕️. Enjoy!")
            profit = profit + price
            account = account - price
            home()
    else:
        print(f"Sorry that's not enough money. Money refunded.")
        change_account()



def change_account(type_coffee):
    global account
    if account < 1.5:
        print("Please insert coins.")
        account += int(input("How many quarters?: ")) * 0.25
        account += int(input("How many dimes?: ")) * 0.1
        account += int(input("How many nickles?: ")) * 0.05
        account += int(input("How many pennies?: ")) * 0.01
        make_coffee(type_coffee)
    else:
        make_coffee(type_coffee)

def home():
    global account
    option_coffee = input("What would you like? (espresso/latte/cappuccino): ").lower().strip()
    if option_coffee in ["espresso","latte","cappuccino"]:
        change_account(option_coffee)

    elif option_coffee == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}ml")
        print(f"Money: ${profit}")
        print("\n")
        home()
    elif option_coffee == "ingredients":
        type_coffee = input("Which one would you like to know the ingredients of? (espresso/latte/cappuccino): ").lower().strip()
        if type_coffee == "espresso":
            print(f"Water: {MENU['espresso']["ingredients"]["water"]}ml")
            print(f"Coffee: {MENU['espresso']["ingredients"]["coffee"]}ml")
        elif type_coffee == "latte":
            print(f"Water: {MENU['latte']["ingredients"]["water"]}ml")
            print(f"Milk: {MENU['latte']["ingredients"]["milk"]}ml")
            print(f"Coffee: {MENU['latte']["ingredients"]["coffee"]}ml")
        elif type_coffee == "cappuccino":
            print(f"Water: {MENU['cappuccino']["ingredients"]["water"]}ml")
            print(f"Milk: {MENU['cappuccino']["ingredients"]["milk"]}ml")
            print(f"Coffee: {MENU['cappuccino']["ingredients"]["coffee"]}ml")
        else:
            print("Product Not Found!")
            home()
    elif option_coffee == "off":
        exit()
    else:
        print("Option Not Found!")
        print("Please try again!")
        print("="*20)
        home()
home()
