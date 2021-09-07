from multiprocessing import Process, Pipe


# what you're doing here can be done using sockets as well.
# but, https://docs.python.org/3/library/multiprocessing.html#:~:text=Usually%20message%20passing shows how you can
# do it using multiprocessing module.
# also this link. https://www.youtube.com/watch?v=IynV6Y80vws&list=PLYxZHWrkz   4k5VL0hkE6U89tqrj8folyma&index=9&t=1527s&ab_channel=VoidRealms

def f(child_conn):
    msg = "Hello"
    child_conn.send(msg)
    child_conn.close()
