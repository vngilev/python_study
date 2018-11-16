import sys
sys.stdin = open("input_01.txt", "r")

s = str(input())
a = str(input())
b = str(input())
cnt = 0

while True:
    if s.count(a):
        s = s.replace(a, b)
        cnt += 1
    else:
        print(cnt)
        break
    if cnt >= 100:
        print("Impossible")
        break

