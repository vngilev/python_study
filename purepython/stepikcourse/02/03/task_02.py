from math import factorial

def takewhile(predicate, iterable):
    # takewhile(lambda x: x<5, [1,4,6,4,1]) --> 1 4
    for x in iterable:
        if predicate(x):
            yield x
        else:
            break

def primes():
    p = 2
    while True:
        if (factorial(p-1) + 1) % p == 0:
            yield p
        p += 1



print(list(takewhile(lambda x : x <= 40, primes())))


