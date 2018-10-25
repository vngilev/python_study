templist = []
for obj in objects:
  if obj not in templist:
    templist.append(obj)
print(len(templist))