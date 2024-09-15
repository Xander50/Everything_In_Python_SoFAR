from tkinter import *
from tkinter.ttk import *

from time import strftime

window=Tk()
window.title("clock")

def time():
  string=strftime('%H:%M:%S %p')
  label.config(text=string)
  label.after(1000,time)

label=Label(window,font=("calibri",40,"bold"),background="blue",foreground="white")

label.pack(anchor="center")
time()

mainloop()