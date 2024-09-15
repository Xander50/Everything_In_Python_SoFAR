from tkinter import *

window = Tk()
window.title("About grids")
window.geometry("210x180")

def display_check():
    red=red1.get()
    blue=blue1.get()
    yellow=yellow1.get()
    green=green1.get()
    print("red:{}\n yellow:{}\n blue:{}\n green:{}".format(red,yellow,blue,green))

label=Label(window, text="Which is your favorite food?")
label.grid(row=0)

Label(window, text="Name",bg="grey").grid(row=1)
name=Entry(window,bd=3)
name.grid(row=1,column=2, padx=5,pady=5)

red1=IntVar()
Checkbutton(window,width=20,text="red", variable=red1, bg="red").grid(row=2)
blue1=IntVar()
Checkbutton(window,width=20, text="blue", variable=blue1, bg="blue" ).grid(row=3)
yellow1=IntVar()
Checkbutton(window,width=20,text="yellow", variable=yellow1, bg="yellow").grid(row=4)
green1=IntVar()
Checkbutton(window,width=20, text="green", variable=green1, bg="green" ).grid(row=5)

Button(window, text="Result",command=display_check).grid(row=6)
Button(window, text="End",command=window.quit).grid(row=7)


window.mainloop()