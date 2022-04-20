import csv
import re
import sys
# Imports the modules needed for this script


def ReadFile(file):
    """Reads a .csv and returns it as a 2 dimensional list."""
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
    """Checks every input for 'cancel' and returns an error if caught."""
    IN = input(prompt).lower()  # Shifts order to lower case
    if IN == 'cancel':
        sys.exit('Canceled order')  # Returns an error message called 'Canceled Order' and exits the code
    else:
        return IN


def checkMainAmount(user):
    """Returns the amount of meals from user input for the main courses"""
    while True:
        amount = Input(f'Hi {user}, How many main meals would you like to order? Max 4 \n')
        try:
            amount = int(amount)  # converts amount to an int. error caught by except if amount is not an integer
            if 0 <= amount <= 4:
                while True:
                    yn = Input(f'You entered {amount}. Is that correct Y/N')
                    if yn == 'y':
                        return amount
                    elif yn == 'n':
                        break
                    else:
                        print(f'Please enter Y or N')
            else:
                print('Please enter a number from 0 - 4')
        except ValueError:
            print('Please enter a number from 0 - 4')


def GetOptions(menu, meal_num):
    """Outputs the options in the selected meal and asks for user response"""
    if menu[meal_num][2] != '':
        opt = menu[meal_num][2].replace(', ', ' OR ')
        opt = opt.replace('/', ' OR ')
        opt = opt.split(' OR ')
        # Splits the option section of the menu into a list.
        options = [meal_num, []]

        while True:
            if len(options[1]) == len(opt):  # If all of the available options have been chosen it breaks the loop.
                break

            for q in range(len(opt)):
                print(f'{q + 1}: {opt[q]}')  # Prints the options

            while True:
                check = Input('Would you like to add an option? Y/N')  # Checks if user wants to add an option.
                if check == 'n':
                    return options
                elif check == 'y':
                    break
                else:
                    print('please enter y or n')

            while True:
                opt_num = Input("What is the option you'd like")
                try:
                    # Checks if the inputted number is a valid integer
                    opt_num = int(opt_num)
                    if 1 <= opt_num <= len(opt):
                        if opt_num in options[1]:
                            print('You already have this option')
                            continue
                        else:
                            break

                    else:
                        print('Please enter a valid option')
                        continue
                except ValueError:
                    print('Please enter a valid integer.')

            options[1].append(opt_num)
        return options
    else:
        return meal_num


def GetDrinkOptions(menu, drink_number):
    """Does the same as GetOptions() but for drinks. """
    if menu[drink_number][2] != '':
        opt = menu[drink_number][2].replace(', ', ' OR ')
        opt = opt.replace('/', ' OR ')
        opt = opt.split(' OR ')
        options = [drink_number, []]
        # Splits the option section of the menu into a list.

        for q in range(len(opt)):
            print(f'{q + 1}: {opt[q]}')

        while True:
            opt_num = Input("What is the option you'd like")
            try:
                # Checks if the option number is a valid integer.
                opt_num = int(opt_num)
                if 1 <= opt_num <= (len(opt)):
                    break
                else:
                    print('Please enter a valid order number')
                    continue
            except ValueError:
                print('Please enter a valid integer.')
        options[1].append(opt_num)
        return options
    else:
        return drink_number


def PrintMainMenuAndOrder(menu, amount):
    """Prints the main menu and gets user input for ordering"""
    print('Here is your main menu')
    for q in range(1, len(menu)):
        if menu[q][2] != '':  # Checks if there is options to print.
            if menu[q][3] != '':
                print(f'{q}: {menu[q][0]} ({(menu[q][3].upper())}) - {menu[q][1]}: Options: {menu[q][2]}. - {menu[q][4]}')
            else:
                print(f"{q}: {menu[q][0]} - {menu[q][1]}: Options: {menu[q][2]}. - {menu[q][4]}")
        else:
            if menu[q][3] != '':
                print(f'{q}: {menu[q][0]} ({(menu[q][3]).upper()}) - {menu[q][1]} - {menu[q][4]}')
            else:
                print(f"{q}: {menu[q][0]} - {menu[q][1]}. - {menu[q][4]}")

    while True:
        order_num = Input(f'Main number {amount}: Which meal would you like to order? \n')
        try:
            order_num = int(order_num)
            if 1 <= order_num <= (len(menu) - 1):  # Checks whether the order number is one of the available meals
                return GetOptions(menu, order_num)
            else:
                print('Please enter a valid order number')
        except ValueError:
            print('Please enter a valid order number')


def checkDrinkAmount():
    """Gets the amount of drinks to order from user input"""
    while True:
        amount = Input('How many drinks would you like to order? Max 10.\n')
        try:
            amount = int(amount)
            if 0 <= amount <= 10:  # Sets a maximum amount of drinks to 10 and a min to 0
                while True:
                    # Clarifies the amount given

                    yn = Input(f'You entered {amount}. Is that correct Y/N')
                    if yn == 'y':
                        return amount
                    elif yn == 'n':
                        break
                    else:
                        print(f'Please enter Y or N')
            else:
                print('Please enter a valid integer')
        except ValueError:
            print('Please enter a positive integer')


def PrintDrinkMenuAndOrder(menu, amount):
    """Prints the drinks menu and orders from user input"""
    print('Here is your drinks menu:')
    for q in range(1, len(menu)):
        if menu[q][2] != '':
            # Checks if there are any options to the meal
            print(f"{q}: {menu[q][0]} - {menu[q][1]}: with options: {menu[q][2]}. - {menu[q][3]}")
        else:
            print(f"{q}: {menu[q][0]} - {menu[q][1]}. - {menu[q][3]}")

    while True:
        order_num = Input(f'Drink number {amount}: Which drink would you like to order? \n')
        try:
            order_num = int(order_num)
            if 1 <= order_num <= (len(menu) - 1):  # Checks whether the order is a valid drink number
                return GetDrinkOptions(menu, order_num)
            else:
                print('Please enter a valid order number')
        except ValueError:
            print('Please enter a valid order number')


def main():  # Initiates the order
    """The order process."""
    print('Welcome to Quick Food. Enter cancel at any time to cancel the order.')
    orders = [[], []]  # [[Mains], [Drinks]]
    while True:
        name = Input('What is your name? \n')
        if name == '':
            print('Please enter a name')
        else:
            break

    amn = checkMainAmount(name)
    for n in range(amn):
        # Orders the mains
        orders[0].append(PrintMainMenuAndOrder(MainMenu, n + 1))

    d_amn = checkDrinkAmount()
    for r in range(d_amn):
        # Orders the drinks
        orders[1].append(PrintDrinkMenuAndOrder(Drinks, r + 1))

    price = 0
    order_list = []  # All of the order information will be appended to this list to be outputted.

    for main_order in orders[0]:
        if type(main_order) == int:
            # If no options were selected the order type is an integer, adds price from menu
            price = price + float(MainMenu[main_order][4].replace('$', '0'))
            order_list.append([MainMenu[main_order][0], MainMenu[main_order][4]])

        elif type(main_order) == list:
            # If there are options the type of order is a list with the meal number first and the options second [num, [Options, ...]
            main_num = main_order[0]  # [Menu Number, [Main Option 1, Main Option 2, etc]]
            main_opt = main_order[1]
            # Splits the meal number from the options
            optList = MainMenu[main_num][2].replace(', ', ' OR ')
            optList = optList.replace('/', ' OR ')
            optList = optList.split(' OR ')
            # Gets the original options as a list.

            order_options = []
            for option in main_opt:
                if '$' in optList[option - 1]:
                    # Checks if option has a $ in it.
                    s = re.compile('\$([0-9.]+)')  # sets a regex compiler checking for $ + digits 0-9 and a decimal point as many as it can.
                    m = re.search(s, optList[option - 1])
                    order_price = m.group(1)  # Returns the price found by the regex
                    price = price + float(order_price)  # Adds the option price.
                order_options.append(optList[option - 1])

            price = price + float(MainMenu[main_num][4].replace('$', '0'))  # Adds the main price.
            order_list.append([MainMenu[main_order[0]][0], f"({', '.join(order_options)})", MainMenu[main_order[0]][4]])

    for drink_order in orders[1]:
        if type(drink_order) == int:
            # If no option is chosen order is type int
            price = price + float(Drinks[drink_order][3].replace('$', '0'))  # Updates the price
            order_list.append([Drinks[drink_order][0], Drinks[drink_order][3]])

        elif type(drink_order) == list:
            # If option is chosen order is type list
            drink_num = drink_order[0]
            drink_opt = int(drink_order[1][0])
            drink_option = Drinks[drink_num][2].split('/')

            order_list.append([Drinks[drink_order[0]][0], f'({drink_option[drink_opt - 1]})', Drinks[drink_order[0]][3]])

            price = price + float(Drinks[drink_num][3].replace('$', '0'))  # Currently no drink options affect price so can just use normal drink price.

    print(f'\n{name.capitalize()} here is your order.')
    for row in order_list:
        print(' '.join(row))

    if float(price).is_integer():
        print(f'\nThe price is ${int(price)}')  # Prints the total cost of the order as an integer if there is no decimal point
    else:
        print(f'\nThe price is ${price:.2f}')  # Prints the total cost of the order as a float with two decimal places for cents


if __name__ == '__main__':
    main()  # Runs the script
