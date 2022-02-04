from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()

root.title('DIGITAL CLOCK')

def clock():
    tick = strftime('%H:%M:%S %p')

    label.config(text = tick)

    label.after(1000, clock)

label = Label(root, font = ('sans' , 80),background = 'black' , foreground = 'cyan')

label.pack(anchor = 'center')

clock()
mainloop()


import datetime

x = datetime.datetime.now()
print(x.year)
print(x.time)