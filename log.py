from tkinter import *
from PIL import ImageTk,Image
import os
import tkinter.messagebox as m
shr=Tk()
def ok():
    un=t1.get()
    pas=t2.get()
    if un=="meshru" and pas=="11111":
        shr.destroy()
        os.system("splash.py")

    else:
        m.showinfo("INcorrect","Acess Denied")

def show():
    
    btn["text"]="hide"
    t2["show"]=""
    def hide():
        btn["text"]="show"
        t2["show"]="*"
        btn["command"]=show

    btn["command"]=hide  

shr.title("gymmer")
shr.config(bg="black")
#geometry
sw=shr.winfo_screenwidth()
sh=shr.winfo_screenheight()

shr.geometry("%dx%d"%(sw,sh))

sh=sh-40
#bgimage
im=Image.open("log.jpg")
res=im.resize((900,600))
i=ImageTk.PhotoImage(res)

l=Label(shr,image=i,bd=0)
l.im=i
l.place(x=0,y=100)
lab=Label(shr,text="AUTHENTICATION",width=50,font=("lucida sans unicode",24,"bold"))
lab.place(x=170,y=50)
fr=Frame(shr,height=500,width=500)
fr.place(x=800,y=150)
la=Label(fr,text="LOGIN",font=("impact",40))
la.place(x=10,y=10)
la=Label(fr,text="Username",font=("ink free",20,"bold"))
la.config(fg="grey")
la.place(x=10,y=130)
la=Label(fr,text="Password",font=("ink free",20,"bold"))
la.config(fg="grey")
la.place(x=10,y=180)
t1=Entry(shr,font=("ink free",16,"bold"))
t2=Entry(shr,font=("ink free",16,"bold"),show="*")
t1.place(x=950,y=280)
t2.place(x=950,y=330)

btno=Button(shr,text="OK",width=4,command=ok)
btno.config(fg="black",bg="grey")
btno.place(x=1000,y=500)

btn=Button(shr,text="show",width=4,command=show)
btn.config(fg="black",bg="grey")
btn.place(x=1245,y=330)







shr.mainloop()
