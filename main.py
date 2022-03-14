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


for i in range(1, len(MainMenu)):
    Menu = Mains(MainMenu[i][0], MainMenu[i][1], MainMenu[i][2], MainMenu[i][3], MainMenu[i][4])
    dish = Mains.Dish(Menu)
    desc = Mains.Desc(Menu)
    opt = Mains.Opt(Menu)
    diet = Mains.Diet(Menu)
    cost = Mains.Cost(Menu)

    print(f"{dish} - {desc}, with options {opt}, additional dietary options {diet}. - {cost}")
