with open("1.txt", 'r') as inp , open ("2.txt", "w") as wr:
    k = 0
    buf = []
    for i in inp:
        buf.append(i)
        k += 1
    for i in (range(k)):
        wr.write(buf[k-i-1])
