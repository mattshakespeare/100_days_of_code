from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

while True:
    user = input(f"Select one of the following options {menu.get_items()}: ")
    if user == 'resource':
        coffee_maker.report()
        money_machine.report()
    elif user == 'off':
        break
    else:
        drink = menu.find_drink(user)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
                
        
        
        

