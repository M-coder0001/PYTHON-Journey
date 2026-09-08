class Computer:
    def __init__(self):
        self.__MaxPrice = 900
    
    def sell(self):
        print("Selling Price: {}".format(self.__MaxPrice))
    
    def setMaxPrice(self, price):
        self.__MaxPrice = price
        
c = Computer()
c.sell()

c.__MaxPrice = 1000
c.sell()

c.setMaxPrice(1001)
c.sell()