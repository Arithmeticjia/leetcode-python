# coding=gbk
import threading
import time


class MyThread1(threading.Thread):
    def run(self):
        # ��mutexA����
        mutexA.acquire()

        # mutexA��������ʱ1�룬�ȴ������Ǹ��߳� ��mutexB����
        print(self.name + '----do1---up----')
        time.sleep(1)

        # ��ʱ���������Ϊ���mutexB�Ѿ���������߳�����������
        mutexB.acquire()
        print(self.name + '----do1---down----')
        mutexB.release()

        # ��mutexA����
        mutexA.release()


class MyThread2(threading.Thread):
    def run(self):
        # ��mutexB����
        mutexB.acquire()

        # mutexB��������ʱ1�룬�ȴ������Ǹ��߳� ��mutexA����
        print(self.name + '----do2---up----')
        time.sleep(1)

        # ��ʱ���������Ϊ���mutexA�Ѿ���������߳�����������
        mutexA.acquire()
        print(self.name + '----do2---down----')
        mutexA.release()

        # ��mutexB����
        mutexB.release()


mutexA = threading.Lock()
mutexB = threading.Lock()

if __name__ == '__main__':
    t1 = MyThread1()
    t2 = MyThread2()
    t1.start()
    t2.start()