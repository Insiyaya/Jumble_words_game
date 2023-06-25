import tkinter
from tkinter import *
from tkinter import messagebox
import admin
import newentry
w=tkinter.Tk()
w.title('login')
w.geometry('400x400')
w['bg']="black"
l1=Label(w,text="WELCOME",font=("algerian",20,'underline'),fg="yellow",bg="black")
l1.grid(column=0,row=1)
tkinter.Label(w,text='playername').place(x=10,y=60)
playername=tkinter.Entry(w)
playername.place(x=120,y=60)

tkinter.Label(w,text='password').place(x=10,y=90)
password=tkinter.Entry(w,show="*")
password.place(x=120,y=90)

def login():
   player=playername.get()
   secret=password.get()
   if player=='myname' and secret=='mybunny':
     messagebox.showinfo("login","login successfully")
     admin.adminwindow()
     w.destroy()
   else:
     messagebox.showinfo("login","invalid username and password")
		
button1=tkinter.Button(w,text='login',command=login).place(x=10,y=120)
button2=tkinter.Button(w,text='exit',command=w.destroy).place(x=100,y=120)
w.mainloop()
