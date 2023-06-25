import tkinter
from tkinter import messagebox
import pymysql as pmc
from tkinter import ttk

'''import pymysql
#db=pymysql.connect(host="127.0.0.1",
                   user="root",
                   password="K6hawK7867@!",
                   db="gameinfo"
                   )'''

def saverecords(PlayerName,Scores):
	try:
		con=pmc.connect(host="127.0.0.1",user='root',password="K6hawK7867@!",database="game")
		print("CONNECTED SUCCESSFULLY")
		rs=con.cursor()
		query="insert into playersinfo values('{}',{})".format(PlayerName,Scores)
		rs.execute(query)
		con.commit()
		print("RECORD SAVED SUCCESSFULLY")
		rs.close()
		con.close()
		
	except Exception as e:
		print(e)
		
saverecords(PlayerName,Scores)

def newwindow():
	n=tkinter.Tk()
	n.title("NEW PLAYER")
	n.eval('tk::PlaceWindow.center')
	tkinter.Label(n,text="PLAYERNAME").place(x=50,y=60)
	me=tkinter.Entry(n)
	me.place(x=120,y=100)
	b=tkinter.Button(n,text='ENTER TO GAME',command=lambda:saverecord(me.get())).place(x=150,y=240)


newwindow()
