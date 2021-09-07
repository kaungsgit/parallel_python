import numpy as np

from multiprocessing import Process
from threading import Thread
import os
import time


def square_numbers():
    for i in range(100):
        i = i * i
        time.sleep(0.1)


if __name__ == "__main__":
    processes = []
    num_processes = os.cpu_count()

    for i in range(num_processes):
        p = Process(target=square_numbers)
        processes.append(p)

    for p in processes:
        p.start()

    for p in processes:
        p.join()

    print('end main')

# if __name__ == "__main__":
#     threads = []
#     num_threads = 8
#
#     for i in range(num_threads):
#         t = Thread(target=square_numbers)
#         threads.append(t)
#
#     for t in threads:
#         t.start()
#
#     for t in threads:
#         t.join()
#
#     print('end main')
