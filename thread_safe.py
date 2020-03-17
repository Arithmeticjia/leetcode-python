import threading
import time

zero = [3]
lock = threading.Lock()


def change_zero():
    global zero
    for i in range(3000000):
        # zero += 1
        # zero -= 1
        with lock:
            zero[0] = zero[0] + 1
            zero[0] = zero[0] - 1


th1 = threading.Thread(target=change_zero)
th2 = threading.Thread(target=change_zero)
th1.start()
th2.start()
th1.join()
th2.join()
print(zero)
