class asset:
  def __init__(self, name, amount, price):
    self.name = name
    self.amount = amount
    self.price = price

class simple_pool: 
    def __init__(self, asset1, asset2):
        self.asset1 = asset1
        self.asset2 = asset2
        total1 = asset1.amount * asset1.price
        total2 = asset2.amount * asset2.price
    
    #def remove(asset, amount):

    #def print_prices(self):
        #print("total1 is" + self.total1)
        #print("There are" + asset1.amount + "of asset" + asset1 + "at price" + asset1.price)
        #print("There are" + asset2.amount + "of asset" + asset2 + "at price" + asset2.price)




uni = asset("uni", 30, 100)
wbtc = asset("wbtc", 10, 300)

uni_wbtc = simple_pool(uni,wbtc)
print(uni_wbtc)
#print_prices()
