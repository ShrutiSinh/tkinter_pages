from tkinter import *
shr=Tk()
def ptrp():
    p=int(t1.get())
    r=p//100
    var.set(str(r))
    pa=p-(r*100)
    asd.set(str(pa))

def km():
    k=int(t4.get())
    m=k*1000
    qwe.set(str(m))
    cm=m*100
    fgh.set(str(cm))
    mm=cm*10
    jkl.set(str(mm))
    
shr.config(bg="#e6e6fa")
h=shr.winfo_screenheight()
w=shr.winfo_screenwidth()
rw=w-400
rh=h-150
hpos=(h/2)-(rh/2)
wpos=(w/2)-(rw/2)
shr.geometry("%dx%d+%d+%d"%(rw,rh,wpos,hpos))
shr.title("CONVERTER")
la=Label(shr,text="CONVERTER",width=12,height=2,font=("ink free",22,"bold"),border=4)
la.configure(bg="black",fg="white",relief=RAISED)
la.place(x=300,y=50)

la=Label(shr,text="enter paise",font=("ink free",16,"bold"),border=4)
la.configure(bg="white",fg="black",relief=RAISED)
la.place(x=100,y=150)
la=Label(shr,text="Rupees",font=("ink free",16,"bold"))
la.configure(bg="white",fg="black",relief=RAISED)
la.place(x=100,y=200)
la=Label(shr,text="Paise",font=("ink free",16,"bold"))
la.configure(bg="white",fg="black",relief=RAISED)
la.place(x=100,y=250)

la=Label(shr,text="enter km",font=("ink free",16,"bold"),border=4)
la.configure(bg="white",fg="black",relief=RAISED)
la.place(x=100,y=350)
la=Label(shr,text="Metre",font=("ink free",16,"bold"))
la.configure(bg="white",fg="black",relief=RAISED)
la.place(x=100,y=400)
la=Label(shr,text="Centimeter",font=("ink free",16,"bold"))
la.configure(bg="white",fg="black",relief=RAISED)
la.place(x=100,y=450)
la=Label(shr,text="Millimeter",font=("ink free",16,"bold"))
la.configure(bg="white",fg="black",relief=RAISED)
la.place(x=100,y=500)
t1=Entry(shr,font=("ink free",16,"bold"),border=4,state=DISABLED)
t1.place(x=300,y=150)
#op
var=StringVar()
t2=Label(shr,textvar=var,font=("ink free",16,"bold"),border=4,height=1,width=20)
t2.place(x=300,y=200)
asd=StringVar()
t3=Label(shr,textvar=asd,font=("ink free",16,"bold"),border=4,height=1,width=20)
t3.place(x=300,y=250)

t4=Entry(shr,font=("ink free",16,"bold"),border=4)
t4.place(x=300,y=350)
#op
qwe=StringVar()
t5=Label(shr,textvar=qwe,font=("ink free",16,"bold"),border=4,height=1,width=20)
t5.place(x=300,y=400)
fgh=StringVar()
t6=Label(shr,textvar=fgh,font=("ink free",16,"bold"),border=4,height=1,width=20)
t6.place(x=300,y=450)
jkl=StringVar()
t7=Label(shr,textvar=jkl,font=("ink free",16,"bold"),border=4,height=1,width=20)
t7.place(x=300,y=500)
b1=Button(shr,text="convert",font=("ink free",16,"bold"),border=4,height=4,width=8,command=ptrp)
b1.config(bg="black",fg="white")
b1.place(x=700,y=150)

b1=Button(shr,text="convert",font=("ink free",16,"bold"),border=4,height=5,width=8,command=km)
b1.config(bg="black",fg="white")
b1.place(x=700,y=370)

b1=Button(shr,text="Exit",font=("ink free",16,"bold"),border=4,width=36,command=exit)
b1.config(bg="black",fg="white")
b1.place(x=150,y=550)






shr.mainloop()
