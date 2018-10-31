from random import random


class RandomIterator:
    def __next__(self):
        return random()


x = RandomIterator()
print(next(x))

