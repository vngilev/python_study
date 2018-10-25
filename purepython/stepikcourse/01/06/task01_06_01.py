import pdb
import sys
sys.stdin = open("input_013_5.txt", "r")
#sys.stdout = open("1.txt", "w")
#test = ['A G', 'A Z', 'A W', 'X W', 'X QWE', 'A X', 'X X', '1 1']
#cd = dict([('W', ['V']), ('G', ['F']), ('E', ['D']), ('Y', ['X', 'A']), ('F', ['D']), ('X', []), ('V', ['Z', 'Y']), ('A', []), ('C', ['A']), ('B', ['A']), ('D', ['B', 'C']), ('Z', ['X'])])
#print(cd)

cd = dict([])
def prepare():
    quantity = int(input())
    parrentNames = ""
    for i in range(quantity):
        cur = str(input())
        if cur.count(":") == 0:
            className = cur
            parrentNames = ""
        else:
            className, parrentNames = map(str, cur.split(" : "))
        if className not in cd.keys():
           cd[className]=[]
        if len(parrentNames) > 0:
            qp = parrentNames.split(" ")
            for j in range(len(qp)):
                cd[className].append(qp[j])
                if qp[j] not in cd.keys():
                    cd[qp[j]]=[]


def findParrent(wcl, par):
    res = "No"
    if par in cd[wcl]:
        return "Yes"
    if wcl == par:
        return "Yes"
    if wcl not in cd.keys():
        return "No"
    if cd[wcl] != []:
        for i in cd[wcl]:
            res = findParrent(i, par)
            if res == "Yes":
                break
    return res;

def work():
    quantity = int(input())
    for i in range(quantity):
#    for i in test:
        cur = (str(input())).split(" ")
#        cur = i.split(" ")
#        print(cur)
        print(findParrent(cur[1], cur[0]))

#pdb.set_trace()
prepare()
print(cd)
work()
