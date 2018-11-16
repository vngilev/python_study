import sys
import re
sys.stdin = open("input1.txt", "r")

temp = r"[\s\S]*cat[\s\S]*cat[\s\S]*"

for line in sys.stdin:
    line = line.rstrip()

    match = re.findall(temp, line)
    if match:
        print(line)


