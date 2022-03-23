import csv
import re


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


def checkAmount(user):
    while True:
        amount = input(f'Hi {user}, How many main meals would you like to order? Max 4 \n')
        try:
            amount = int(amount)
            if 0 <= amount <= 4:
                while True:
                    yn = input(f'You entered {amount}. Is that correct Y/N')
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


def GetOptions(menu, meal_num):
    if menu[meal_num][2] != '':
        opt = menu[meal_num][2].replace(', ', ' OR ')
        opt = opt.replace('/', ' OR ')
        opt = opt.split(' OR ')
        opt.insert(0, 'No additional item')

        for q in range(len(opt)):
            print(f'{q + 1}: {opt[q]}')
        while True:
            opt_num = input("What is the option you'd like")
            try:
                opt_num = int(opt_num)
                break
            except ValueError:
                print('Please enter a valid integer.')
        return [meal_num, opt_num]
    else:
        return meal_num


def PrintMainMenuAndOrder(menu, amount):
    print('Here is your main menu')
    for q in range(1, len(menu)):
        if menu[q][2] != '':
            print(
                f"{q}: {menu[q][0]} - {menu[q][1]}: With options: {menu[q][2]}. - {menu[q][4]}")  # TODO AddDietaryOptions
        else:
            print(f"{q}: {menu[q][0]} - {menu[q][1]}. - {menu[q][4]}")
    while True:
        order_num = input(f'Main number {amount}: Which meal would you like to order? \n')
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
        amount = input('How many drinks would you like to order? \n')
        try:
            amount = int(amount)
            if 0 <= amount:
                while True:
                    yn = input(f'You entered {amount}. Is that correct Y/N')
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
        order_num = input(f'Drink number {amount}: Which drink would you like to order? \n')
        try:
            order_num = int(order_num)
            if 1 <= order_num <= len(menu) + 1:
                return GetOptions(menu, order_num)
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
                    yn = input(f'You entered {num}. Is that correct Y/N')
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
    name = input('What is your name? \n')

    amn = checkAmount(name)
    for n in range(amn):
        orders[0].append(PrintMainMenuAndOrder(MainMenu, n + 1))

    d_amn = checkDrinkAmount()
    for r in range(d_amn):
        orders[1].append(PrintDrinkMenuAndOrder(Drinks, r + 1))
    print(orders)

    price = 0
    for main_order in orders[0]:
        try:
            main_order = int(main_order)
            price = price + float(MainMenu[main_order-1][4].replace('$','0'))
        except TypeError:
            main_order = main_order[0]
            main_opt = main_order[1]
            optList = MainMenu[main_order][2].replace(', ', ' OR ')
            optList = optList.replace('/', ' OR ')
            optList = optList.split(' OR ')
            if '$' in optList[main_opt]:
                m = re.search('\$\d+(?:\.\d+)?', optList[main_opt])
                order_price = m.group(1)
                price

    break
