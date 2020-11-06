# encoding: UTF-8
import threading
import time


class MyThread(threading.Thread):
    def run(self):
        global num
        time.sleep(1)
        num = num+1
        msg = self.name+' set num to '+str(num)
        print(msg)


num = 0


def test():
    for i in range(1000):
        t = MyThread()
        t.start()


if __name__ == '__main__':
    test()