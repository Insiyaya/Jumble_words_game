import tkinter
from tkinter import *
from tkinter import messagebox
import mysql.connector as myc
import wordjumble


def game():
        n.withdraw()
        wordjumble.wordjumble()

def saverecord( playerid ,playername):
	try:
		con=myc.connect(host="localhost",user="root",passwd="donainsiya",database="game")
		print("CONNECTED SUCCESSFULLY")
		rs=con.cursor()
		query="insert into wordjumble values({},'{}')".format(playerid,playername)
		rs.execute(query)
		con.commit()
		print("RECORD SAVED SUCCESSFULLY")
		rs.close()
		con.close()
		
	except Exception as e:
		print(e)
		

def newwindow():
        global n
        n=tkinter.Tk()
        n.geometry('400x300')
        n.title("NEW PLAYER")
        n['bg']="red"
        l2=Label(n,text="word jumble",font=("algerian",20),fg='blue',bg='red')
        l2.grid(column=0,row=1)
        tkinter.Label(n,text="playerid").place(x=30,y=60)
        me=tkinter.Entry(n)
        me.place(x=100,y=60)
        tkinter.Label(n,text="playername").place(x=30,y=80)
        name=tkinter.Entry(n)
        name.place(x=100,y=80)

        b=tkinter.Button(n,text='ENTER INFO',command=lambda:saverecord(me.get(),name.get())).place(x=150,y=240)
        b1=tkinter.Button(n,text='ENTER TO GAME',command=game).place(x=150,y=200)

#saverecord( playerid ,playername)
#newwindow()
