class HotBeverage:
    def __init__(self, price = 0.30, name = "hot beverage"):
        self.price = price
        self.name = name

    def description(self):
        return "Just some hot water in a cup."

    def __str__(self):
        # info = description()
        return '''name : %s
price : %0.2f
description : %s''' % (self.name, self.price, self.description())

class Coffee(HotBeverage):
    def __init__(self):
        HotBeverage.__init__(self, 0.40, "coffee")

    def description(self):
        return "A coffee, to stay awake."

class Tea(HotBeverage):
    def __init__(self):
        HotBeverage.__init__(self, 0.30, "tea")
    
    def description(self):
        return "Just some hot water in a cup."

class Chocolate(HotBeverage):
    def __init__(self):
        HotBeverage.__init__(self, 0.50, "chocolate")
    
    def description(self):
        return "Chocolate, sweet chocolate..."

class Cappuccino(HotBeverage):
    def __init__(self):
        HotBeverage.__init__(self, 0.45, "cappuccino")
    
    def description(self):
        return "Un po’ di Italia nella sua tazza!"
