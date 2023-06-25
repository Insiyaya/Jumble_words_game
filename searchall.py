import tkinter
from tkinter import messagebox
import mysql.connector as myc
from tkinter import ttk

def searchwindow():
    searchwindow=tkinter.Tk()
    s=tkinter.Tk()
    s.geometry('800x400')
    s.title("Search All")
    frame1=tkinter.Frame(s)
    frame1.pack(side=tkinter.LEFT)
    tv=ttk.Treeview(frame1,columns=(1,2),show="headings",height="5")
    tv.pack()
    tv.heading(1,text="playerid")
    tv.heading(2,text="playername")
    try:  
        con=myc.connect(host="localhost",user='root',password="donainsiya",database="game")
        print("CONNECTED SUCCESSFULLY")
        rs=con.cursor()
        query="select * from wordjumble"
        rs.execute(query)
        rows=rs.fetchall()
        totalrows=rs.rowcount
        print(totalrows)
        for i in rows:
            tv.insert("",'end',values=i)

        rs.close()
        con.close()


    except Exception as e:
        print(e)

