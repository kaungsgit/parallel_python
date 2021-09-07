from multiprocessing import Process
import multiprocessing
import PySimpleGUI as sg
import time


class SomeBench:
    def __init__(self):
        self.some_attr = 'some_attr'
        print('Scanning instruments...')
        time.sleep(5)
        print('Scanning completed!')


def gui_func(q):
    layout = [[sg.Text("Hello from PySimpleGUI")], [sg.Button("OK")]]

    # Create the window
    window = sg.Window("Demo", layout)

    initialized = False

    # Create an event loop
    while True:

        if not initialized:
            bench = SomeBench()
            initialized = True
            q.put(bench)

        event, values = window.read()
        # End program if user closes window or
        # presses the OK button
        if event == "OK" or event == sg.WIN_CLOSED:
            break

    window.close()


q = multiprocessing.Queue()

if __name__ == '__main__':
    p = Process(target=gui_func, args=[q])
    p.start()
    p.join()

    # what you're doing here can be done using sockets as well.
    # but, https://docs.python.org/3/library/multiprocessing.html#:~:text=Usually%20message%20passing shows how you can
    # do it using multiprocessing module.
    # also this link. https://www.youtube.com/watch?v=IynV6Y80vws&list=PLYxZHWrkz   4k5VL0hkE6U89tqrj8folyma&index=9&t=1527s&ab_channel=VoidRealms

    # while q.empty() is False:
    #     print(q.get())
