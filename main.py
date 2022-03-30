import csv
import re
import sys


def ReadFile(file):
    arr = []
    with open(file, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            arr.append(row)
    f.close()
    return arr


MainMenu = ReadFile('Menu for Year 12 Internal - Sheet1.csv')
Drinks = ReadFile('Drinks Menu - Sheet1.csv')


def Input(prompt):
    IN = input(prompt).lower()
    if IN == 'cancel':
        sys.exit('Canceled order')
    else:
        return IN


def checkAmount(user):
    while True:
        amount = Input(f'Hi {user}, How many main meals would you like to order? Max 4 \n')
        try:
            amount = int(amount)
            if 0 <= amount <= 4:
                while True:
                    yn = Input(f'You entered {amount}. Is that correct Y/N')
                    if not yn.isalpha():
                        print('Please enter Y or N')
                    elif yn.lower() == 'y':
                        return amount
                    elif yn.lower() == 'n':
                        break
                    else:
                        print(f'Please enter Y or N')
            else:
                print('Please enter a number from 0 - 4')
        except ValueError:
            print('Please enter a number from 0 - 4')


def GetOptions(menu, meal_num):  # TODO Make duplicate options invalid + incorrect options not being caught.
    if menu[meal_num][2] != '':
        opt = menu[meal_num][2].replace(', ', ' OR ')
        opt = opt.replace('/', ' OR ')
        opt = opt.split(' OR ')
        options = [meal_num, []]

        while True:
            for q in range(len(opt)):
                print(f'{q + 1}: {opt[q]}')

            while True:
                check = Input('Would you like to add an option').lower()
                if check == 'n':
                    return options
                elif check == 'y':
                    break
                else:
                    print('please enter y or n')

            while True:
                opt_num = Input("What is the option you'd like")
                try:
                    opt_num = int(opt_num)
                    break
                except ValueError:
                    print('Please enter a valid integer.')

            options[1].append(opt_num)
    else:
        return meal_num


def GetDrinkOptions(menu, drink_number): #TODO Incorrect numbers not being caught
    if menu[drink_number][2] != '':
        opt = menu[drink_number][2].replace(', ', ' OR ')
        opt = opt.replace('/', ' OR ')
        opt = opt.split(' OR ')
        options = [drink_number, []]

        for q in range(len(opt)):
            print(f'{q + 1}: {opt[q]}')

        while True:
            opt_num = Input("What is the option you'd like")
            try:
                opt_num = int(opt_num)
                if 0 >= opt_num >= (len(opt)):
                    print('Please enter a valid order number')
                    continue
                else:
                    break
            except ValueError:
                print('Please enter a valid integer.')
        options[1].append(opt_num)
    else:
        return drink_number


def PrintMainMenuAndOrder(menu, amount):
    print('Here is your main menu')
    for q in range(1, len(menu)):
        if menu[q][2] != '':
            print(
                f"{q}: {menu[q][0]} - {menu[q][1]}: With options: {menu[q][2]}. - {menu[q][4]}")
        else:
            print(f"{q}: {menu[q][0]} - {menu[q][1]}. - {menu[q][4]}")
    while True:
        order_num = Input(f'Main number {amount}: Which meal would you like to order? \n')
        try:
            order_num = int(order_num)
            if 1 <= order_num <= len(menu) + 1:
                return GetOptions(menu, order_num)
            else:
                print('Please enter a valid order number')
        except ValueError:
            print('Please enter a valid order number')


def checkDrinkAmount():
    while True:
        amount = Input('How many drinks would you like to order? \n')
        try:
            amount = int(amount)
            if 0 <= amount:
                while True:
                    yn = Input(f'You entered {amount}. Is that correct Y/N')
                    if not yn.isalpha():
                        print('Please enter Y or N')
                    elif yn.lower() == 'y':
                        return amount
                    elif yn.lower() == 'n':
                        break
                    else:
                        print(f'Please enter Y or N')
            else:
                print('Please enter a positive integer')
        except ValueError:
            print('Please enter a positive integer')


def PrintDrinkMenuAndOrder(menu, amount):
    print('Here is your drinks menu:')
    for q in range(1, len(menu)):
        if menu[q][2] != '':
            print(f"{q}: {menu[q][0]} - {menu[q][1]}: with options: {menu[q][2]}. - {menu[q][3]}")
        else:
            print(f"{q}: {menu[q][0]} - {menu[q][1]}. - {menu[q][3]}")

    while True:
        order_num = Input(f'Drink number {amount}: Which drink would you like to order? \n')
        try:
            order_num = int(order_num)
            if 1 <= order_num <= len(menu) + 1:
                return GetDrinkOptions(menu, order_num)
            else:
                print('Please enter a valid order number')
        except ValueError:
            print('Please enter a valid order number')


def CheckInt(num):
    while True:
        try:
            num = int(num)
            if 0 <= num:
                while True:
                    yn = Input(f'You entered {num}. Is that correct Y/N')
                    if not yn.isalpha():
                        print('Please enter Y or N')
                    elif yn.lower() == 'y':
                        return num
                    elif yn.lower() == 'n':
                        break
                    else:
                        print(f'Please enter Y or N')
            else:
                print('Please enter a positive integer')
        except ValueError:
            print('Please enter a positive integer')


while True:  # Initiates the order
    orders = [[], []]  # [[Mains], [Drinks]]
    name = Input('What is your name? \n')

    amn = checkAmount(name)
    for n in range(amn):
        orders[0].append(PrintMainMenuAndOrder(MainMenu, n + 1))

    d_amn = checkDrinkAmount()
    for r in range(d_amn):
        orders[1].append(PrintDrinkMenuAndOrder(Drinks, r + 1))

    price = 0
    for main_order in orders[0]:
        if type(main_order) == int:
            price = price + float(MainMenu[main_order][4].replace('$', '0'))

        elif type(main_order) == list:
            main_num = main_order[0]  # [Menu Number, [Main Option 1, Main Option 2, etc]]
            main_opt = main_order[1]
            optList = MainMenu[main_num][2].replace(', ', ' OR ')
            optList = optList.replace('/', ' OR ')
            optList = optList.split(' OR ')

            for option in main_opt:
                if '$' in optList[option - 1]:
                    s = re.compile('\$([0-9.]+)')
                    m = re.search(s, optList[option - 1])
                    order_price = m.group(1)
                    price = price + float(order_price)
                else:
                    pass
            price = price + float(MainMenu[main_num][4].replace('$', '0'))

    for drink_order in orders[1]:
        if type(drink_order) == int:
            price = price + float(Drinks[drink_order][3].replace('$', '0'))

        elif type(drink_order) == list:
            drink_num = drink_order[0]
            drink_opt = drink_order[1]

            price = price + float(Drinks[drink_num][3].replace('$', '0'))

    print(f'${price}')
    break
