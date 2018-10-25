def c(a, b):
    if  b == 0:
        return 1
    if b > a: 
        return 0
    return c(a-1, b) + c(a-1, b-1)
n, k = map(int, input().split())
print(c(n,k))