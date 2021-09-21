import datetime as d
import tkinter as t
import threading


def digital_clock():
    frame = t.Tk()
    frame.geometry('300x100')
    frame.title('Digital Clock')
    global l
    l = t.Label(frame, text=d.datetime.now(), font=100, fg='red')
    l.place(x=10, y=50)
    i = 0

    def a():
        while i >= 0:
            l.config(text=(d.datetime.now()))

    m = threading.Thread(target=a)
    m.start()
    frame.mainloop()
    pass
