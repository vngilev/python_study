t = [1, 3, 5, 7, 9, 11]
book = {
    "key1": "test1",
    "key2": "test2",
    "key3": "test3",
    "key4": "test4"
}

string = "Hello? world!"

for i in t:
    print(i)

it = iter(t)

while True:
    try:
        i = next(it)
        print(i)
    except StopIteration:
        break

