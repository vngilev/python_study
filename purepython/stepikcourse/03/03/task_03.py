import sys
import re
sys.stdin = open("input3.txt", "r")

temp = r"z.{3}z"

for line in sys.stdin:
    line = line.rstrip()

    match = re.findall(temp, line)
    if match:
        print(line)


