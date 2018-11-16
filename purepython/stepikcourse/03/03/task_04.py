import sys
import re
sys.stdin = open("input4.txt", "r")

temp = r"\\"

for line in sys.stdin:
    line = line.rstrip()

    match = re.findall(temp, line)
    if match:
        print(line)


