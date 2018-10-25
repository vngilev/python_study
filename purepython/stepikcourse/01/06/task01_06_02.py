class ExtendedStack(list):

    def sum(self):
        # операция сложения
        res = self.pop()+self.pop()
        self.append(res)

    def sub(self):
        # операция вычитания
        res = self.pop()-self.pop()
        self.append(res)

    def mul(self):
        # операция умножения
        res = self.pop()*self.pop()
        self.append(res)

    def div(self):
        # операция целочисленного деления
        res = self.pop()//self.pop()
        self.append(res)

exst = ExtendedStack([])
exst.append(5)
exst.append(6)
