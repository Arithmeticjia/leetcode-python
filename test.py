import matplotlib.pyplot as plt
import numpy as np
from numpy import *

'''def sigmoid(x):
    # 直接返回sigmoid函数
    return 1. / (1. + np.exp(-x))


def plot_sigmoid():
    # param:起点，终点，间距
    x = np.arange(-30, 30, 0.2)
    y = sigmoid(x)
    plt.plot(x, y)
    plt.show()


if __name__ == '__main__':
    plot_sigmoid()'''

'''a = [3,2,7,6,6,4,3,2,7,4]
b = [3,2,6,6,7,4,3,2,7,4]
res = 0
ses = 0
for i in range (len(a)):
    res ^= a[i]

for i in range (len(b)):
    ses ^= b[i]

print(res,ses)
ooo = [1,2,3,4,5,6,7]
from random import choice
print(choice(ooo))'''

'''a = random.rand(5,5)
print(type(a))
print(a)
randomMat = mat(a)
print(type(randomMat))
print(randomMat)
x = np.mat([[3,5],[2,6]])
print(x)
y = np.mat([[1,7],[6,4]])
print(y)
print(type(x))
print(x*y)
xx = np.array([[3,5],[2,6]])
print(xx)
yy = np.array([[1,7],[6,4]])
print(yy)
print(type(xx))
print(xx*yy)
print(np.dot(xx,yy))
randomMat = mat(random.rand(5,5))
#print(type(randomMat))
#print(randomMat,randomMat.I)
xrandomMat = randomMat.T
print(randomMat,xrandomMat)
# encoding: UTF-8
import threading
import time


class ChangeMoney(threading.Thread):
    def run(self):
        global money
        #time.sleep(1)
        money = money+1
        msg = self.name+' set money to '+str(money)
        print(msg)


money = 0


if __name__ == '__main__':
    for i in range(5):
        t = ChangeMoney()
        t.start()
# encoding: UTF-8
import threading
import time


class ChangeMoney():
    def First(name):
        global money
        for i in range(20):
            if mutex.acquire():
                money = money+1
                msg = "%s set money to " % name + str(money)
                print(msg)
                mutex.release()


    def Second(name):
        global money
        for i in range(20):
            if mutex.acquire():
                money = money+1
                msg = "%s set money to " % name + str(money)
                print(msg)
                mutex.release()


    def Third(name):
        global money
        for i in range(20):
            if mutex.acquire():
                money = money+1
                msg = "%s set money to " % name + str(money)
                print(msg)
                mutex.release()


money = 0
mutex = threading.Lock()

threads = []
t1 = threading.Thread(target=ChangeMoney.First,args=(u'First',))
threads.append(t1)
t2 = threading.Thread(target=ChangeMoney.Second,args=(u'Second',))
threads.append(t2)
t3 = threading.Thread(target=ChangeMoney.Third,args=(u'Third',))
threads.append(t3)

if __name__ == '__main__':
    for t in threads:
        #t = ChangeMoney()
        t.start()
    for i in range(5):
        t = ChangeMoney()
        t.start()'''


class Solution:
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        result = []

        for word in words:
            fix = dict()
            for i in range(len(pattern)):
                fix[pattern[i]] = word[i]
            # print(fix)
            # func = lambda z、: dict([(x, y) for y, x in z.items()])
            # print(func(fix))
            # print(func(func(fix)))
            fix = dict([(x, y) for y, x in dict([(x, y) for y, x in fix.items()]).items()])
            if all(word[i] == fix.get(pattern[i]) for i in range(len(fix))):
                result.append(word)
        return result

Solution().findAndReplacePattern(["badc","abab","dddd","dede","yyxx"],"baba")