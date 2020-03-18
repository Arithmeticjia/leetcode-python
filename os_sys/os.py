import os

filepath = '/Users/Arithmetic/PycharmProjects/leetcode/multithreading_multiprocess'

if os.path.isdir(filepath):
    for everyChild in os.listdir(filepath):
        everyChildPath = os.path.join(filepath,everyChild)
        if os.path.isfile(everyChildPath):
            print(os.path.basename(everyChildPath))
        elif os.path.isdir(everyChildPath):
            print('%s is DIR' % everyChildPath)

else:
    print('Not DIR')