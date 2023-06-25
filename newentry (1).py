import tkinter
from tkinter import *
from tkinter import messagebox
import tictactoe


def game():
        tictactoe.tictactoe()



global n
n=tkinter.Tk()
n.geometry('400x300')
n.title("NEW PLAYER")
n['bg']="red"
l2=Label(n,text="TIC-TAC-TOE",font=("algerian",20),fg='blue',bg='red')
l2.grid(column=0,row=1)
tkinter.Label(n,text="playername").place(x=30,y=80)
name=tkinter.Entry(n)
name.place(x=100,y=80)
b1=tkinter.Button(n,text='ENTER TO GAME',command=game).place(x=150,y=200)

