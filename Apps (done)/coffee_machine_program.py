MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0
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

def report():
    for element in resources:
        element = element
        quantity = resources[element]
        if element == 'water' or element == 'milk':
            print(f'{element}: {quantity}ml')
        elif element == 'coffee':
            print(f'{element}: {quantity}g')
        elif element == 'money':
            print(f'{element}: ${quantity}')
def check_resources_sufficient(drink_ordered):
    """checks whether enough resources to do the drink or not
        returns True if sufficient
        returns False if not suffient and prints the missing"""

    water_required = MENU[drink_ordered]['ingredients']['water']
    coffee_required = MENU[drink_ordered]['ingredients']['coffee']
    milk_required = MENU[drink_ordered]['ingredients']['milk']

    water_left = resources['water']
    coffee_left = resources['coffee']
    milk_left = resources['milk']

    if water_left > water_required:
        water_sufficient = True
    else:
        water_sufficient = False
    if coffee_left > coffee_required:
        coffee_sufficient = True
    else:
        coffee_sufficient = False
    if milk_left > milk_required:
        milk_sufficient = True
    else:
        milk_sufficient = False
    #####################
    if water_sufficient and coffee_sufficient and milk_sufficient:
        print('messsage: It can be done "enough resources"')
        return True
    else:
        print('message: there are no enough resources')
        if coffee_sufficient == False:
            print("Not Engough coffee")
        if milk_sufficient == False:
            print("Not enough milk")
        if water_sufficient == False:
            print("Not enough water")
        return False
def input_coins(drink_ordered):
    quarters = int(input('quarters: '))
    dimes = int(input('dimes: '))
    nickles = int(input('nickles: '))
    pennies = int(input('pennies: '))
    total_paid = 0.25*dimes + 0.1*nickles + 0.05*pennies
    return total_paid

success = False
change = 0
cost = 0
def process_coins(drink_ordered):
    global cost
    total_paid = input_coins(drink_ordered)
    cost = MENU[drink_ordered]['cost']
    global success, change
    if total_paid >= cost:
        success = True
        change = total_paid - cost
    else:
        success = False


def transaction_successful():
    if success == True:
        return True
    else:
        return False
def prepare_order_and_adjust_resources(drink_ordered):
    print('Preparing Order')
    water_required = MENU[drink_ordered]['ingredients']['water']
    coffee_required = MENU[drink_ordered]['ingredients']['coffee']
    milk_required = MENU[drink_ordered]['ingredients']['milk']

    resources['water'] -= water_required
    resources['coffee'] -= coffee_required
    resources['milk'] -= milk_required
    resources['money'] += cost



working = True
while working:
    drink_ordered = input('“What would you like? (espresso/latte/cappuccino): ')
    if drink_ordered == 'off':
        working = False ##break the loop (NOT DONE YET)
    elif drink_ordered == 'report':
        report()
    elif drink_ordered in 'espresso/latte/cappuccino': #one of those
        if check_resources_sufficient(drink_ordered) == True:
            process_coins(drink_ordered)
            if transaction_successful() == True:
                prepare_order_and_adjust_resources(drink_ordered)
                print(f'here is your {drink_ordered}')
                print(f'your change is: {change} ')
            else:
                print("Sorry! That's not enough money")
    else:
        print('Wrong Input, Please Try Again')
    print('\n\n\n\n')