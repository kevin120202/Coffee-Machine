from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def main():
    coffeeMaker = CoffeeMaker()
    menu = Menu()
    money = MoneyMachine()
    while True:
        user_input = input(
            f"What would you like? ({menu.get_items()}): ").lower()
        if user_input == 'report':
            coffeeMaker.report()
            money.report()
        elif user_input == "espresso" or user_input == "latte" or user_input == "cappuccino":
            drink = menu.find_drink(user_input)
            if coffeeMaker.is_resource_sufficient(drink) and money.make_payment(drink.cost):
                coffeeMaker.make_coffee(drink)
        elif user_input == 'off':
            break
        else:
            print("Invalid input")


main()
