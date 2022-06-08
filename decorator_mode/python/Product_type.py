from decorator_Interface import Beverage, CondimentDecorator

class BlackTea(Beverage):
    def __init__(self):
        super().__init__()
        self.description = "BlackTea"
    
    def cost(self):
        return 20

class GreenTea(Beverage):
    def __init__(self):
        super().__init__()
        self.description = "GreenTea"
    
    def cost(self):
        return 15

class Milk(CondimentDecorator):
    def __init__(self, bevarage):
        super().__init__()
        self.bevarage = bevarage
    
    def get_description(self):
        return f"{self.bevarage.get_description()}, Milk"
    
    def cost(self):
        return self.bevarage.cost() + 20

class Bubble(CondimentDecorator):
    def __init__(self, bevarage):
        super().__init__()
        self.bevarage = bevarage
    
    def get_description(self):
        return f"{self.bevarage.get_description()}, Bubble"
    
    def cost(self):
        return self.bevarage.cost() + 10
