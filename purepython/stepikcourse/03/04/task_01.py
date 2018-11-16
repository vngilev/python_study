import requests
import sys
import re

sys.stdin = open("input1.txt", "r")

temp = r"\<a href=\"([^\>\"]+)\"[^\>]*\>"

req12 = re.findall(temp, str(input()))
req23 = re.findall(temp, str(input()))

try:
    res1 = requests.get(req12)
    step1 = re.findall(temp, res1.text)
except Exception:
    print("No")
    exit()

pr = "No"

for st1 in step1:
    if pr == "Yes":
        break
    try:
        res2 = requests.get(st1)
    except Exception:
        pr = "No"
        continue

    step2 = re.findall(temp, res2.text)

    for st2 in step2:
        if st2 == req23:
            pr = "Yes"
            break
print(pr)
