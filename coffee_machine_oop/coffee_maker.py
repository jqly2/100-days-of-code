import constants

class CoffeeMaker:
    
    
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100
        }
        self.menu = constants.COFFEE
    
    
    def find_item(self, request: str):
        for item in self.menu:
            if request.lower() == item:
                return item
        return ''
 
        
    def report(self):
        print(f"Here is the current resources in the machine:")
        for item, amount in self.resources.items():
            if item == "milk" or item == "water":
                metric = constants.LOWEST_FLUID_METRIC
            elif item == "coffee":
                metric = constants.LOWEST_SOLID_METRIC
            print(f"{item.capitalize()}: {amount}{metric}")


    def coffee_making(self, request: str):
        self.update_ingredients(request)
        return print(f"Here is your {request}. Enjoy!")

        
    
    def check_resource(self, query:str):
        res = self.resources
        drink = self.menu[query]
        if query:
            for ingredient in drink:
                if ingredient in res and res[ingredient] > drink[ingredient]:
                    return drink["price"]
            return 0
        else:
            return 0
        
    
    def update_ingredients(self, drink: str):
        recipe = self.menu[drink]["recipe"]
        for ingredient in recipe:
            if ingredient in self.resources:
                self.resources[ingredient] -= recipe[ingredient]
        return self.resources
        