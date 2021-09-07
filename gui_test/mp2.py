from multiprocessing import Process, Queue, Pipe
from mp1 import f

# what you're doing here can be done using sockets as well.
# but, https://docs.python.org/3/library/multiprocessing.html#:~:text=Usually%20message%20passing shows how you can
# do it using multiprocessing module.
# also this link. https://www.youtube.com/watch?v=IynV6Y80vws&list=PLYxZHWrkz   4k5VL0hkE6U89tqrj8folyma&index=9&t=1527s&ab_channel=VoidRealms

if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p = Process(target=f, args=(child_conn,))
    p.start()
    print(parent_conn.recv())  # prints "Hello"
