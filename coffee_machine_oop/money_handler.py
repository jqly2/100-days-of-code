import constants

class MoneyHandler:
    
    
    def __init__(self):
        self.bank = {
            "profit": 0.00,
            "receive": 0.00
        }
        self.coinage = constants.COINS
        
        
    def report(self):
        profit = self.bank["profit"]
        return print(f"Money: {constants.CURRENCY}{profit}")
        
        
    def processing(self):
        for coin in self.coinage.keys():
            amount = input(f"How many {coin} inserted?")
            if not amount or not amount.isdigit():
                amount = 0
            self.bank["receive"] += self.coinage[coin] * float(amount)
        return self.bank   
         

    def price_check(self, price: float):
        if self.bank["receive"] - price < 0:
            need = "{:.2f}".format(price - self.bank["receive"])
            print(f'''It cost ${price} and you only gave ${self.bank["receive"]}.
                  You need to give ${need} more or request a different drink.''')
            self.bank["receive"] = 0
            return False
        elif self.bank["receive"] - price >= 0:
            return True
        else:
            return


    def cashier(self, price):
        change = self.bank["receive"] - price 
        rounded_change = "{:.2f}".format(change) 
        if change == 0:
            self.bank["profit"] += price
            print("You have paid enough. Thank you!")
            self.bank["receive"] = 0
            return self.bank
        elif change > 0:
            self.bank["profit"] += price
            self.bank["receive"] = 0
            if change >= 1.00:
                dollars = "dollars"
            else:
                dollars = ""
            print(f"Here is {constants.CURRENCY}{rounded_change} {dollars} in change.")
            return self.bank["profit"]
        else:
            print("There was an error in the payout.")
            return 