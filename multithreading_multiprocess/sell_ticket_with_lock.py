# coding:gbk

import threading
import time

total = 5  # �ܹ���Ʊ��

lock = threading.RLock()  # ���������뻥����


def sale():
    global total

    lock.acquire()
    time.sleep(1)
    print('�����۳���%s��Ʊ\n' % total)
    time.sleep(1)

    total -= 1

    lock.release()


if __name__ == '__main__':
    threads = []

    for i in range(5):  # ����5���̣߳�����5����Ʊ����
        t = threading.Thread(target=sale, args=())
        threads.append(t)

    for t in threads:  # ��ʼ��Ʊ
        t.start()
