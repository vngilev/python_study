import pdb
class Buffer:
    def __init__(self):
        self.position = 0
        self.tail = []
        self.sum = 0

    def reset(self):
        print(self.sum)
        self.sum = 0
        self.tail = []
        self.position = 0

    def add(self, *a):
        for i in range(len(a)):
            self.sum += a[i]
            self.position += 1
            self.tail.append(a[i])
            if self.position == 5:
                Buffer.reset(self)

    def get_current_part(self):
        print(self.tail)
        return self.tail

#pdb.set_trace()
buf = Buffer()
buf.add(1, 2, 3)
buf.get_current_part()
#pdb.set_trace()
buf.add(4, 5, 6)
buf.get_current_part()
buf.add(7, 8, 9, 10)
buf.get_current_part()
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
buf.get_current_part()