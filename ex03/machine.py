import random
from beverages import HotBeverage, Coffee, Tea, Chocolate, Cappuccino

class  CoffeeMachine:
    def __init__(self):
        self.machine = 0
    
    class EmptyCup(HotBeverage):
        name = "empty cup"
        price = 0.90

        def description(self):
            return "An empty cup?! Gimme my money back!"
    
    class BrokenMachineException(Exception):
        def __init__(self):
              Exception.__init__(self, "This coffee machine has to be repaired.")

    def repair(self):
        self.machine = 0

    def serve(self, parameter_from_HotBeverage):
        if self.machine >= 10:
            # print(self.machine)
            raise self.BrokenMachineException()
        val = random.choice(['full_cup', 'empty_cup'])
        if val == 'full_cup':
            self.machine += 1
            # print(self.machine)
            return parameter_from_HotBeverage.description()
        else:
            return self.EmptyCup().description()


if __name__ == "__main__":
    h_b = HotBeverage()
    c_m = CoffeeMachine()
    coffee = Coffee()
    tea = Tea()
    cappuccino = Cappuccino()
    chocolate = Chocolate()
    beverage_list = [h_b, coffee, tea, cappuccino, chocolate]
    for x in range(0, 25):
        try:
            bv = random.choice(beverage_list)
            print(c_m.serve(bv))
        except Exception as e:
            print(e)
    c_m.repair()
    print('''
    Just repaired !
    ''')
    for x in range(0, 25):
        try:
            bv = random.choice(beverage_list)
            print(c_m.serve(bv))
        except Exception as e:
            print(e)