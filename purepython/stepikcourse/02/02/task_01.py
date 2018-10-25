import sys
sys.stdin = open("task_01_01.txt", "r")

import datetime
inpdate = [int(x) for x in str(input()).split()]
ndate = datetime.date(inpdate[0], inpdate[1], inpdate[2]) + datetime.timedelta(int(input()))
print(str(ndate.year)+" "+str(ndate.month)+" "+str(ndate.day))