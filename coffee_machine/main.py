# %%
import constants


resource = {
    "coffee": 100,
    "milk": 200,
    "money": 0.00,
    "water": 300
}


def update_ingredients(recipe: dict):
    for ingredient in recipe:
        if ingredient in recipe:
            resource[ingredient] -= recipe[ingredient]
    return resource


def resource_check(recipe: dict):
    for ingredient in recipe:
        if not ingredient in recipe or resource[ingredient] - recipe[ingredient] < 0:
            print(f"Sorry there is not enough {ingredient}.")
            return False
        else:
            continue
    update_ingredients(recipe)
    return True


def price_check(price: float):
    total = 0
    for coin in constants.COINS.keys():
        amount = float(input(f"How many {coin} inserted?"))
        total += constants.COINS[coin] * amount
    if total - price < 0:
        need = "{:.2f}".format(price - total)
        print(f"It cost ${price} and you only gave ${total}. You need to give ${need} more or request a different drink.")
        return False
    else:
        change = "{:.2f}".format(total - price) 
        cashier(float(change))
        return True


def cashier(total: float):
    if total == 0:
        print("You have paid enough. Thank you!")
        return
    elif total > 0:
        resource["money"] += total
        if total >= 1.00:
            dollars = "dollars"
        else:
            dollars = ""
        print(f"Here is ${total} {dollars} in change.")
        return resource
    else:
        print("There was an error in the payout.")
        return
        
            
def coffee_making():
    request = input("What would you like?")
    if request == "espresso" or request == "latte" or request == "cappuccino":
        DRINK = constants.COFFEE[request]
        if resource_check(DRINK["recipe"]) and price_check(DRINK["price"]):
            print(f"Here is your {request}. Enjoy!")
            return True
        else:
            print(f"Please try to order again if you wish. Otherwise, have a nice day.") 
            return True
    elif request == "off":
        print("Processing to turn off the machine.")
        return False
    elif request == "report":
        print(f"Here is the current resources in the machine:")
        for item, amount in resource.items():
            if item == "milk" or item == "water":
                metric = "ml"
                dollar = ""
            elif item == "coffee":
                metric = "g"
                dollar = ""
            else:
                metric = ""
                dollar = "$"
                amount = "{:.2f}".format(amount)
            print(f"{item.capitalize()}: {dollar}{amount}{metric}")
        return True
    else:
        print("That request is invalid")
        return True
        
while coffee_making():
    coffee_making()


