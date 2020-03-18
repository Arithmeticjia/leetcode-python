import os
import time
from multiprocessing import Process, Lock, Pool


def work_without_lock():
    print('%s is running' % os.getpid())
    time.sleep(2)
    print('%s is done' % os.getpid())


def work_with_lock(lock):
    lock.acquire()
    print('%s is running' % os.getpid())
    time.sleep(2)
    print('%s is done' % os.getpid())
    lock.release()


def start_with_lock():
    lock = Lock()
    for i in range(3):
        p = Process(target=work_with_lock, args=(lock,))
        p.start()


def start_without_lock():
    for i in range(3):
        p = Process(target=work_without_lock)
        p.start()


if __name__ == '__main__':
    # start_with_lock()
    start_without_lock()
