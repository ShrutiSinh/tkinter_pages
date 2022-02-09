from tkinter import *
import tkinter as tk
shr=Tk()

counter=0
def co():
    def count():
        global counter
        counter +=1
        label.config(text=str(counter))
        label.after(1000,count)



shr.config(bg="#e6e6fa")
h=shr.winfo_screenheight()
w=shr.winfo_screenwidth()
rw=w-400
rh=h-150
hpos=(h/2)-(rh/2)
wpos=(w/2)-(rw/2)
shr.geometry("%dx%d+%d+%d"%(rw,rh,wpos,hpos))
shr.title("IMG")
label=Label(shr,text="l")
label.place(x=100,y=100)
b=Button(shr,text="stop",command=co)
b.place(x=100,y=200)
shr.mainloop()
shr.mainloop
