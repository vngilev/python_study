dictNameSpace = dict([("global","None")])
dictVariables = dict( [ ("global", dict([("def","global")]) ) ] )

def createNameSpace(n, p):
    if n not in dictNameSpace.keys():    
        dictNameSpace[n] = p
        dictVariables[n] = dict([])

def addVar(n, v):
    #if n not in dictVariables.keys():
    #    dictVariables[n] = dict([(v, n)])
    if v not in dictVariables[n].keys():
        dictVariables[n][v] = n

def getVar(n, v):
    if n == "None":
        return "None" 
    elif v in dictVariables[n].keys():
        return n
    else:
        return getVar(dictNameSpace[n], v)
    
n = int(input())
for i in range(n):
    cmd, key, value = map(str, input().split())
    if cmd == "create":
        createNameSpace(key,value)
    if cmd == "add":
        addVar(key, value)
    if cmd == "get":
        print(getVar(key,value))  
