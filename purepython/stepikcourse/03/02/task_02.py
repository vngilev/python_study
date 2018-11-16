import sys
sys.stdin = open("input_02.txt", "r")

s = str(input())
t = str(input())
cnt = 0
savepos = -1
curpos = 0

for i in range(len(s)):
    curpos = s.find(t, i)
    if curpos == -1:
        break
    if curpos != savepos:
        cnt += 1
        savepos = curpos
print(cnt)
