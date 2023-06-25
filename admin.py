import tkinter
from tkinter import messagebox
import newentry
import searchall

def callnewentry():
    newentry.newwindow()
def callsearchall():
    searchall.searchwindow()
def adminwindow():
    a=tkinter.Tk()
    a['bg']="#6A1B4D"
    a.title("ADMIN")
    b1=tkinter.Button(a,text="New Player",command=callnewentry).place(x=200,y=50)
    b2=tkinter.Button(a,text="Show All Record",command=callsearchall).place(x=200,y=100)
    b3=tkinter.Button(a,text="update",command=callsearchall).place(x=200,y=150)

    
