from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title('CLOCK')

def time():
    string = strftime('%H:%M:%S %p')
    Label.config(text = string)
    Label.after(1000, time)

Label = Label(root, font = ('times new roman', 40, 'bold'),
               background = 'black',
               foreground =  'white')

Label.pack(anchor = 'center')
time()

mainloop()