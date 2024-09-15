from tkinter import *

window = Tk()
window.title("Profile Entry using Grids")
window.geometry("500x300")
window.maxsize(500,300)
window.config(bg="lightgrey")

image=PhotoImage(file="200w.gif")
img=image.subsample(2,2)
img1=Label(window,image=img)
img1.grid(row=0,column=0,padx=5,pady=5)

label=Label(window, text="Please enter your information:", bg="lightgrey")
label.grid(row=0,column=1,padx=5,pady=5)

Label(window, text="Name", bg="lightgrey").grid(row=1,column=1,padx=5,pady=5)
name=Entry(window,bd=3)
name.grid(row=1,column=2, padx=5,pady=5)

# male=IntVar()
# Checkbutton(window,width=20,text="Male", variable=male, bg="red").grid(row=2)
# female=IntVar()
# Checkbutton(window,width=20, text="Female", variable=female, bg="blue").grid(row=3)

gender=Menubutton(window,text="Gender")
gender.grid(row=2,column=2,padx=5,pady=5)
gender.menu=Menu(gender)
gender["menu"]=gender.menu
gender.menu.add_cascade(label="Male")
gender.menu.add_cascade(label="Female")
gender.menu.add_cascade(label="Others")

Label(window, text="Eyecolor",bg="lightgrey").grid(row=3, column=1,padx=5,pady=5)
eyecolor=Entry(window,bd=3)
eyecolor.grid(row=3,column=2, padx=5,pady=5)

Label(window, text="Height",bg="lightgrey").grid(row=4,column=1,padx=5,pady=5)
height=Entry(window,bd=3)
height.grid(row=4,column=2, padx=5,pady=5)
Label(window, text="inches",bg="lightgrey").grid(row=4, padx=5,pady=5, column=3)

Label(window, text="Weight", bg="lightgrey").grid(row=5,column=1,padx=5,pady=5)
weight=Entry(window,bd=3)
weight.grid(row=5,column=2, padx=5,pady=5)
Label(window, text="lbs",bg="lightgrey").grid(row=5, padx=5,pady=5, column=3)


window.mainloop()