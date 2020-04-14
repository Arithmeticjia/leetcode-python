import threading
from queue import Queue


def caculate(list, queue):
    for i in range(len(list)):
        list[i] = list[i] * 2

    queue.put(list)


if __name__ == '__main__':
    q = Queue()
    threads = []
    result = []
    data = [[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]]
    for i in range(5):
        t = threading.Thread(target=caculate(data[i], q))
        t.start()
        threads.append(t)

    for thread in threads:
        thread.join()

    for _ in range(5):
        result.append(q.get())

    print(result)

