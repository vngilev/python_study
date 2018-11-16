import sys
import re
sys.stdin = open("input2.txt", "r")


temp = r"\b(?!-)cat\b(?!-)"

for line in sys.stdin:
    line = line.rstrip()

    match = re.findall(temp, line)
    if match:
        print(line)
