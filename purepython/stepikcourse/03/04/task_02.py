import requests
import sys
import re

templateHREF = r"\<a href=\"([^\>\"]+)\"[^\>]*\>"
templatePATH = r"\<a href=[\'\"]([^\>]+)[\'\"][^\>]*\>"
templateDOMAIN = r"(?(?=[http|https|ftp|smtp|file])\w*|\s"
#start_HTML = requests.get(re.sub(templateHREF, "/1", str(input())))
#listLinks = re.findall(templateHREF, start_HTML.text)

sys.stdin = open("input2.txt", "r")
listLinks = []

for line in sys.stdin:
    #listLinks.append(line.rstrip())
    print(re.findall(templatePATH, line.rstrip()))
    listLinks.append(re.findall(templatePATH, line.rstrip()))

print(listLinks)

for i in range(len(listLinks)):
    print(re.findall(templateDOMAIN, listLinks[i][0]))
    #print(listLinks[i])
