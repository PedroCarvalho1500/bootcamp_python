import os
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


indices = {
    "espresso": 0,
    "latte": 1,
    "cappuccino": 2
}


if __name__ == '__main__':
    print(f"+-+ +-+ +-+ +-+ +-+   +-+ +-+ +-+ +-+ +-+ +-+ +-+")
    print(f"|C| |O| |F| |E| |E|   |M| |A| |C| |H| |I| |N| |E|")
    print(f"+-+ +-+ +-+ +-+ +-+   +-+ +-+ +-+ +-+ +-+ +-+ +-+")
    
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()
    menu_drinks = Menu()
    
    option = "on"
    while(option != "off"):
        option = input("\n\n\n  What would you like? (espresso/latte/cappuccino): ")
        if(option == "report"):
            coffee_maker.report()
            money_machine.report()
        elif(option != "off"):
            drink_menu_item = menu_drinks.find_drink(option)
            try:
                if(coffee_maker.is_resource_sufficient(drink_menu_item) and money_machine.make_payment(drink_menu_item.cost)): 
                    coffee_maker.make_coffee(drink_menu_item)
            except:
                input("OPÇÃO INVÁLIDA !!! PRESS ENTER TO CONTINUE...")