# %%
from coffee_maker import CoffeeMaker
from money_handler import MoneyHandler

coffee_maker_session = CoffeeMaker()
money_handler_session = MoneyHandler()


def barista():
    order = input("What would like?").lower()
    if order == "off" or not order:
        print("Turning off the machine.")
        return False
    else:
        drink = coffee_maker_session.find_item(order)
        if order == "report":
            coffee_maker_session.report()
            money_handler_session.report()
            barista()
        elif not drink:
            print("Sorry we do not carry this item in our menu.")
            barista()
        elif drink:
            price = coffee_maker_session.check_resource(order)
            if price != 0:
                if sort_money(price):
                    coffee_maker_session.coffee_making(order)
                    money_handler_session.cashier(price)
                    barista()
                else:
                    print("Returning to get your order.")
                    barista()
            else:
                print("There was not enough in the machine to make your order.")
                barista()
        else:
            return False
            

def sort_money(price: float):
    money_handler_session.processing()
    if money_handler_session.price_check(price):
        return True
    else:
        option = input('''Do you have enough to pay 
                       or want to order something else?
                       Type "payment" or "order"''')
        if option == 'payment':
            sort_money(price)
        elif option == 'order':
            return False

if barista():
    barista()
    

        

        



