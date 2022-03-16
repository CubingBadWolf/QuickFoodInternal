import csv


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


class Mains:
    def __init__(self, Name, Description, Options, Dietary, Cost):
        self.Cost = Cost
        self.Dietary = Dietary
        self.Options = Options
        self.Description = Description
        self.Dish = Name

    def Dish(self):
        return self.Dish

    def Desc(self):
        return self.Description

    def Opt(self):
        return self.Options

    def Diet(self):
        if self.Dietary == '':
            return 'N/A'
        else:
            return self.Dietary

    def Cost(self):
        return self.Cost


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


def PrintMainMenuAndOrder(menu, amount):
    for i in range(1, len(menu)):
        print(f"{i}: {menu[i][0]} - {menu[i][1]} with options {menu[i][2]} additional dietary options {menu[i][3]}. - {menu[i][4]}")
    while True:
        order_num = input(f'Main number {amount}: Which meal would you like to order? \n')
        try:
            order_num = int(order_num)
            if 1 <= order_num <= len(menu)+1:
                return order_num
            else:
                print('Please enter a valid order number')
        except ValueError:
            print('Please enter a valid order number')


def checkDrinkAmount(user):
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
    for i in range(1, len(menu)):
        print(f"{i}: {menu[i][0]} - {menu[i][1]} with options {menu[i][2]}. - {menu[i][3]}")
    while True:
        order_num = input(f'Drink number {amount}: Which drink would you like to order? \n')
        try:
            order_num = int(order_num)
            if 1 <= order_num <= len(menu)+1:
                return order_num
            else:
                print('Please enter a valid order number')
        except ValueError:
            print('Please enter a valid order number')


while True:  # Initiates the order
    orders = [[], []] # [[Mains], [Drinks]]
    name = input('What is your name? \n')
    amn = checkAmount(name)
    d_amn = checkDrinkAmount(name)
    for n in range(amn):
        orders[0].append(PrintMainMenuAndOrder(MainMenu, amn))
    for r in range(d_amn):
        orders[1].append(PrintDrinkMenuAndOrder(Drinks, d_amn))
    print(orders)
    break