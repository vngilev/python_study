import sys
sys.stdin = open("task_02_03.txt", "r")


class mylist(list):
    def __init__(self, seq=()):
        super().__init__(self)
        self.marked = False

    def __setMark__(self, marked = True):
        self.marked = marked

    def __isMarked__(self):
        return True if self.marked else False

cd = {}

def init():
    q = int(getRealData())
    for i in range(q):
        curstr = str(getRealData())
        if (curstr.count(":") == 0):
            cd[curstr] = mylist()
        else:
            ch, par = map(str, curstr.split(" : "))
            if ch not in cd.keys():
                cd[ch] = mylist()
            pa = par.split()
            for p in pa:
                if p not in cd.keys():
                    cd[p] = mylist()
                cd[p].append(ch)

def markTheException(ex):
    cd[ex].__setMark__()
    for ch in cd[ex]:
        markTheException(ch)

def work():
    mem = set()
    q = int(getRealData())
    for i in range(q):
        ex = str(getRealData())
        if ex in cd.keys():
            if cd[ex].__isMarked__():
                if ex not in mem:
                    print(ex)
                mem.add(ex)
            else:
                markTheException(ex)
        else:
            print(ex)
            mem.add(ex)

def getRealData():
    while True:
        inp = input()
        if inp: return inp

init()
work()
