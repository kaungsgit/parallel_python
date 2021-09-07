import gui_test.pysimplegui_test as ps1

if __name__ == '__main__':
    while ps1.q.empty() is False:
        print(ps1.q.get())
