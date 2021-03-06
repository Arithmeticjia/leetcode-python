# coding:gbk

import threading
import time

total = 5  # 总共的票数

lock = threading.Lock()  # 创建不可重入互斥锁
# rlock = threading.RLock()  # 创建可重入互斥锁


def sale():
    global total

    lock.acquire()
    lock.acquire()
    time.sleep(1)
    print('正在售出第%s张票\n' % total)
    time.sleep(1)

    total -= 1
    lock.release()
    lock.release()


if __name__ == '__main__':
    threads = []

    for i in range(5):  # 创建5个线程，代表5个售票窗口
        t = threading.Thread(target=sale, args=())
        threads.append(t)

    for t in threads:  # 开始售票
        t.start()
