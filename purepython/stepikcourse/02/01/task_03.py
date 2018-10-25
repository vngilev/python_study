class NonPositiveError(Exception):
    pass


class PositiveList(list):
    def __init__(self, seq=()):
        super().__init__(self)

    def append(self, x):
        if x > 0:
            super().append(x)
        else:
            raise NonPositiveError("NonPositiveError")


test = PositiveList()
test.append(5)
#test.append(0)
#test.append(-5)
print(test)
