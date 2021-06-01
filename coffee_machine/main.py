'''App that imitates a coffee machine'''

'''main menus'''

from os import system
from time import sleep

def make_espresso(water, coffee):
    system('cls')
    ten = int(input("Enter the number of 10p's: "))
    twenty = int(input("Enter the number of 20p's: "))
    fifty = int(input("Enter the number of 50p's: "))
    pounds = int(input('Enter the number of pound coins: '))
    sum = (ten * 0.10) + (twenty * 0.20) + (fifty * 0.50) + (pounds * 1.00)
    if sum < 1.50:
        system('cls')
        print('insufficient funds')
        sleep(5)
        system('cls')
    elif sum >= 1.50:
        system('cls')
        print('your drink is being made')
        sleep(5)
        system('cls')
        print(f'your change is £{sum - 1.50}')
        sleep(5)
        system('cls')
        water -= 50
        coffee -= 30
    return water, coffee

def make_latte(water, coffee, milk):
    system('cls')
    ten = int(input("Enter the number of 10p's: "))
    twenty = int(input("Enter the number of 20p's: "))
    fifty = int(input("Enter the number of 50p's: "))
    pounds = int(input('Enter the number of pound coins: '))
    sum = (ten * 0.10) + (twenty * 0.20) + (fifty * 0.50) + (pounds * 1.00)
    if sum < 2.50:
        system('cls')
        print('insufficient funds')
        sleep(5)
        system('cls')
    elif sum >= 2.50:
        system('cls')
        print('your drink is being made')
        sleep(5)
        system('cls')
        print(f'your change is £{sum - 2.50}')
        sleep(5)
        system('cls')
        water -= 150
        coffee -= 30
        milk -= 200
    return water, coffee, milk

def make_cappucino(water, coffee, milk):
    system('cls')
    ten = int(input("Enter the number of 10p's: "))
    twenty = int(input("Enter the number of 20p's: "))
    fifty = int(input("Enter the number of 50p's: "))
    pounds = int(input('Enter the number of pound coins: '))
    sum = (ten * 0.10) + (twenty * 0.20) + (fifty * 0.50) + (pounds * 1.00)
    if sum < 2.50:
        system('cls')
        print('insufficient funds')
        sleep(5)
        system('cls')
    elif sum >= 2.50:
        system('cls')
        print('your drink is being made')
        sleep(5)
        system('cls')
        print(f'your change is £{sum - 2.50}')
        sleep(5)
        system('cls')
        water -= 200
        coffee -= 30
        milk -= 150
    return water, coffee, milk
        

def check_espresso_resource(water, coffee):
    check = True
    if water < 50:
        system('cls')
        print('not enough water')
        sleep(5)
        system('cls')
        check = False
    if coffee < 30:
        system('cls')
        print('not enough coffee')
        sleep(5)
        system('cls')
        check = False
    return check

def check_latte_resource(water, coffee, milk):
    check = True
    if water < 150:
        system('cls')
        print('not enough water')
        sleep(5)
        system('cls')
        check = False
    if coffee < 30:
        system('cls')
        print('not enough coffee')
        sleep(5)
        system('cls')
        check = False
    if milk < 200:
        system('cls')
        print('not enough milk')
        sleep(5)
        system('cls')
        check = False
    return check

def check_cappucino_resource(water, coffee, milk):
    check = True
    if water < 200:
        system('cls')
        print('not enough water')
        sleep(5)
        system('cls')
        check = False
    if coffee < 30:
        system('cls')
        print('not enough coffee')
        sleep(5)
        system('cls')
        check = False
    if milk < 150:
        system('cls')
        print('not enough milk')
        sleep(5)
        system('cls')
        check = False
    return check
    

#main menu
def main_menu():
    water = 1000
    coffee = 500
    milk = 1000
    while True:
        system('cls')
        print('Enter the option you would like to select (1/2/3/4/5)')
        print()
        print('1)espresso\n2)latte\n3)cappucino\n4)report\n5)turn on/off')
        user = int(input('Enter your option here: '))
        if user == 1:
            check = check_espresso_resource(water, coffee)
            if check == True:
                water, coffee = make_espresso(water, coffee)
        elif user == 2:
            check = check_latte_resource(water, coffee, milk)
            if check == True:
                water, coffee, milk = make_latte(water, coffee, milk)
        elif user == 3:
            check = check_cappucino_resource(water, coffee, milk)
            if check == True:
                water, coffee, milk = make_cappucino(water, coffee, milk)
        elif user == 4:
            system('cls')
            print('Resources')
            print()
            print(f'Water: {water}\nCoffee: {coffee}\nMilk: {milk}')
            sleep(5)
        elif user == 5:
            break
        else:
            continue
        
    
    

#on off switch
def on_off():
    while True:
        system('cls')
        user = input('Turn on/off (enter on or off): ')
        if user == 'on':
            main_menu()
        elif user == 'off':
            system('cls')
            print('Thank you, goodbye')
            sleep(5)
            system('cls')
            break
        else:
            continue

on_off()
