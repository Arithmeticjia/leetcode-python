import copy

templist = [(2,), 1, 2, [3, 4]]

print(id(templist), id(templist[0]), id(templist[1]), id(templist[2]), id(templist[3]), id(templist[3][0]), id(templist[3][1]))

# testlist = templist

testCopyList = copy.copy(templist)

testDeepCopyList = copy.deepcopy(templist)

# templist.append('hello')
templist[3].append(5)
templist[3] = [5, 6, 8]
# templist[3][0] = 10
# templist[0] = 19
# templist[0]['abc'] = 333

print(id(testCopyList), id(testCopyList[0]), id(testCopyList[1]), id(testCopyList[2]), id(testCopyList[3]), id(testCopyList[3][0]), id(testCopyList[3][1]))
print(id(testDeepCopyList), id(testDeepCopyList[0]), id(testDeepCopyList[1]), id(testDeepCopyList[2]),id(testDeepCopyList[3]),id(testDeepCopyList[3][0]),
      id(testDeepCopyList[3][1]))
print(templist, testCopyList, testDeepCopyList)

t = (0, 1)
m = copy.copy(t)
print(id(t), id(m))
