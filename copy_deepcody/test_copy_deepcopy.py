import copy

templist = [0, 1, 2, [3, 4]]

print(id(templist[0]), id(templist[3]))

# testlist = templist

testCopyList = copy.copy(templist)

testDeepCopyList = copy.deepcopy(templist)

templist.append('hello')
templist[3].append(5)
templist[0] = 19
print(id(templist[0]), id(templist[3]))
print(id(templist[0]), id(templist[3]))

print(templist, testCopyList, testDeepCopyList)