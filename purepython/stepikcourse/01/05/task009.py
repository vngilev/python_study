class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity
        self.quantity = 0
    
    def can_add(self, v):
        if self.quantity + v <= self.capacity:
            return True
        return False
    
    def add(self, v):
        if MoneyBox.can_add(self, v) == True: 
            self.quantity += v

x = MoneyBox(5)
x.add(2)
x.add(3)
x.add(1)
 