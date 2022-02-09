import mysql.connector
from mysql.connector import (connection)
from tkinter import *
from tkcalendar import Calendar
def getdate():
    l1.config(text=cal.get_date())
    cal.place(x=0,y=0,width=0,height=0)

def oc():
    cal.place(x=200,y=100,width=250,height=250)
    l1["text"]=""
    
    
mydb = mysql.connector.connect(  host="localhost",user="root",password="root",database="shrutidb",charset="utf8")

print(mydb)        
    
    

sh=Tk()
sh.geometry("1000x700")
l1=Label(sh,text="")
l1.place(x=100,y=100)
cal=Calendar(sh,selectmode="day",year=2021,month=9,day=16)

btn=Button(sh,text="date",command=getdate)
btn.place(x=400,y=400)
bt=Button(sh,text="^",command=oc)
bt.place(x=300,y=300)
btm=Button(sh,text="^",command=oc,state=DISABLED)
btm.place(x=300,y=400)



sh.mainloop()
