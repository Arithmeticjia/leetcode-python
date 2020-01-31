import threading
import time


class ChangeMoney():
    def First(name):
        global money
        for i in range(20):
            money = money+1
            msg = "%s set money to " % name + str(money)
            print(msg)


    def Second(name):
        global money
        for i in range(20):
            money = money+1
            msg = "%s set money to " % name + str(money)
            print(msg)



    def Third(name):
        global money
        for i in range(20):
            money = money+1
            msg = "%s set money to " % name + str(money)
            print(msg)


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
    '''for i in range(5):
        t = ChangeMoney()
        t.start()'''