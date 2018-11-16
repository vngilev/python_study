import requests
import requests.exceptions
import random
import time
import sys
import re

#sys.stdin = open("input1.txt", "r")

#temp = r"\<a href=\"([^\>\"]+)\"[^\>]*\>"

#req12 = re.findall(temp, str(input()))
#req23 = re.findall(temp, str(input()))

refTRNS = "http://ec2-34-245-46-182.eu-west-1.compute.amazonaws.com/tws/transfers"
refTRN = "http://ec2-34-245-46-182.eu-west-1.compute.amazonaws.com/tws/transfer.json"
refCRDS = "http://ec2-34-245-46-182.eu-west-1.compute.amazonaws.com/tws/cards"
localTransfers = "http://localhost:8080/tws/transfers"
localTransfer = "http://localhost:8080/tws/transfer"

headers = {'Content-Type': 'application/xml', 'Accept': 'application/xml'}
cardPfx = "card"

for i in range(3):
    data = {
            "Transfer": [
                {
                    "from": cardPfx+str(random.randint(1, 5)),
                    "to": cardPfx+str(random.randint(1, 5)),
                    "amount": cardPfx+str(random.randint(1, 10000))
                }]}

#    data = "<Transfer><from>" + cardPfx + str(random.randint(1, 5))+"</from><to>" + cardPfx+str(random.randint(1, 5))
#    data = data + "</to><amount>" + str(random.randint(1, 10000))+"</amount></Transfer>"

    try:
    #res1 = requests.get(refCRDS, headers)
        res2 = requests.post(refTRN, data=data, headers=headers)
        print(res2.status_code)
        print(res2.text)
        time.sleep(2)
    except requests.exceptions.RequestException:
        print("No")


