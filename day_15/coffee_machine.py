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
    "money": 0,
}





def intro():
    a = input('What would you like to have? (espresso/latte/cappuccino): ')
    if a == 'espresso':
        resource_check('espresso')
        currency_check('espresso')
        resource_update('espresso')
    elif a == 'latte':
        resource_check('latte')
        currency_check('latte')
        resource_update('latte')
    elif a == 'cappuccino':
        resource_check('cappuccino')
        currency_check('cappuccino')
        resource_update('cappuccino')
    elif a == 'report':
        report()



def resource_check(option):
    if option == 'cappuccino' or option == 'latte':
        if MENU[(option)]['ingredients']['water'] > resources['water']:
            print("sorry there is not enough water")
            exit()
        elif MENU[(option)]['ingredients']['milk'] > resources['milk']:
            print("sorry there is not enough milk")
            exit()
        elif MENU[(option)]['ingredients']['coffee'] > resources['coffee']:
            print("sorry there is not enough coffee")
            exit()
    elif option == 'espresso':
        if MENU[(option)]['ingredients']['water'] > resources['water']:
            print("sorry there is not enough water")
            exit()
        elif MENU[(option)]['ingredients']['coffee'] > resources['coffee']:
            print("sorry there is not enough coffee")
            exit()



def currency_check(choice):
    print("Please insert coins.")
    q = int(input("How many quarters? "))
    d = int(input("How many dimes? "))
    n = int(input("How many nickels? "))
    p = int(input("How many pennies? "))

    quarters = q*(0.25)
    dimes =  d *(0.10)
    nickels = n * (0.05)
    pennies = p * (0.01)
    total = quarters + dimes + pennies + nickels
    if total > MENU[(choice)]['cost']:
        change =  int(total - MENU[(choice)]['cost'])
        rounded_change = round(change, 2)
        resources['money'] = resources['money'] + total - change

        print(f"Here is your {rounded_change} in change")
        print(f"Here is your {choice}. Enjoy!")
    else:
        print("Sorry that is not enough money.Money refunded")


def resource_update(resource):
    if resource == 'espresso':
     resources['water'] = resources['water'] - 50
     resources['coffee'] =  resources['coffee'] - 18

    elif resource == 'latte':
        resources['water'] = resources['water'] - 200
        resources['milk'] = resources['milk'] - 150
        resources['coffee'] = resources['coffee'] - 24
    elif resource == 'cappuccino':
        resources['water'] = resources['water'] - 250
        resources['milk'] = resources['milk'] - 100
        resources['coffee'] = resources['coffee'] -24




def report():
    print(f"water: {resources['water']}")
    print(f"milk: {resources['milk']}")
    print(f"coffee: {resources['coffee']}")
    print(f"money: {resources['money']}")


while resources['water'] > 0:
    intro()



