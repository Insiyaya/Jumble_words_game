import tkinter
from tkinter import *
from PIL import Image
from PIL import ImageTk
import random
from tkinter import messagebox

answers=['rot','ruin','page','trip','dew','tin','oily','rust','coin','book','troy','mines','lily','rope','ace','boa']
words=['tor','uirn','apeg','pitr','ewd','int','loiy','stru','ocin','obok','yotr','iesnm','illy','orpe','cae','oba']
n=random.randrange(1,15,1)

ma=['grudge','hussle','prick','hollow','fright','vanish','vague','hermit','estate','jewish','breed','goofy','dipper','critic','phobia','mantis']
mw=['urdgeg','susleh','pirkc','lowolh','rifgth','avinhs','avueg','timreh','tsatee','hsweji','ederb','ogoyf','piderd','riicct','hopaib','tinsma']
m=random.randrange(0,15,1)

da=['kryptonite','aristocrat','pleasure','dungeon','poseidon','meteor','quantum','chamomile','woodoo','harbour','silhouette','xaxophone','mandolin','viking']
dw=['oprytnteik','orttaairsc','sealrepu','gundneo','esponido','teeomr','nuatmuq','mmoilehca','oooodw','brouahr','littehuose','aoxxoenhp','lodinnam','iikngv']
h=['weakness of superhero.','person who belongs to higher class.','feeling of satisfaction.','prison in castle.','greek god.','matter from outer space.','field of physics.','type of tea','type of magic','place where ships moore in shelter','thing with ablack outline.','is an instrument.','is an instrument','type of warriors.' ]
f=random.randrange(0,14,1)

def wordjumble():

    
   
    def easy():
        def default():
            global words,answers,n
            lbl.config(text=words[n])
        def reset():
            global words,answers,n
            n=random.randrange(0,15,1)
            lbl.config(text=words[n])
            en.delete(0,END)
        def checkans():
            global words,answers,n
            v=en.get()
            if v == answers[n]:
                messagebox.showinfo("You are genius!!!!","THIS IS A CORRECT ANSWER")
                reset(),d.destroy(),easy()
            else:
                messagebox.showerror("ERROR","THIS IS NOT CORRECT,TRYAGAIN")
                en.delete(0,END),d.destroy(),easy()
        def end():
            messagebox.askquestion('end','surely end')
            d.destroy()
            i=Label(u,text= "!(•̀ᴗ•́)THANKYOU!(•̀ᴗ•́)!",font=('verdana',20),bg='green',fg='yellow',width=20)
            i.pack(pady=10)
        d=tkinter.Tk()
        d.title("JUMBLED WORDS")
        d['bg']="black"
        lb=Label(d,text="WELCOME TALENT",font=("algerian",21),bg="black",fg="white")
        lb.pack(pady=30)
        lbl=Label(d,text="WELCOmeTALNT",font=("verdana",20),bg="blue",fg='yellow',width=25,relief=GROOVE)
        lbl.pack(pady=30)
        k=StringVar()
        en=Entry(d,font=("verdana",15),textvariable=k)
        en.pack(pady=50)
        checkbtn=Button(d,text="check",font=("comic sans ms",16),bg='grey',fg='green',width=16,relief=GROOVE,command=checkans)
        checkbtn.pack(pady=50)
        resetbtn=Button(d,text="reset",font=("comic sans ms",16),bg='grey',fg='red',width=16,relief=GROOVE,command=reset)
        resetbtn.pack()
        endbtn=Button(d,text='END  ┌(˘⌣˘)ʃ',font=('verdana',20),fg='violet',bg='grey',width=18,command=end)
        endbtn.pack(pady=10)
        default()
        d.mainloop()
    def medium():
        def defaultm():
            global mw,ma,m
            lblm.config(text=mw[m])
        def resetm():
            global mw,ma,m
            m=random.randrange(0,15,1)
            lblm.config(text=mw[m])
            enm.delete(0,END)
        def checkansm():
            global mw,ma,m
            w=enm.get()
            if w == ma[m]:
                messagebox.showinfo("You are genius!!!!","THIS IS A CORRECT ANSWER")
                resetm(),t.destroy(),medium()
            else:
                messagebox.showerror("ERROR","THIS IS NOT CORRECT,TRYAGAIN")
                enm.delete(0,END),t.destroy(),medium()
        def end():
            messagebox.askquestion('end','surely end')
            t.destroy()
            i=Label(u,text= "!(•̀ᴗ•́)THANKYOU!(•̀ᴗ•́)!",font=('verdana',20),bg='green',fg='yellow',width=20)
            i.pack(pady=10)
        t=tkinter.Tk()
        t.title("JUMBLED WORDS")
        t['bg']="black"
        lbm=Label(t,text="WELCOME TALENT",font=("algerian",21),bg="black",fg="white")
        lbm.pack(pady=30)
        lblm=Label(t,text="WELCOmeTALNT",font=("verdana",20),bg="blue",fg='yellow',width=25,relief=GROOVE)
        lblm.pack(pady=30)
        g=StringVar()
        enm=Entry(t,font=("verdana",15),textvariable=g)
        enm.pack(pady=50)
        checkbtnm=Button(t,text="check",font=("comic sans ms",16),bg='grey',fg='green',width=16,relief=GROOVE,command=checkansm)
        checkbtnm.pack(pady=50)
        resetbtnm=Button(t,text="reset",font=("comic sans ms",16),bg='grey',fg='red',width=16,relief=GROOVE,command=resetm)
        resetbtnm.pack()
        endbtn=Button(t,text='END  ┌(˘⌣˘)ʃ',font=('verdana',20),fg='violet',bg='grey',width=18,command=end)
        endbtn.pack(pady=10)
        defaultm()
        t.mainloop()
    def hard():
        def default():
            global dw,da,f
            lbl.config(text=dw[f])
        def hint():
            global dw,da,f,j,jh
            j=Label(d,text="word is a",font=("verdana",20),bg='blue',fg='yellow',width=25)
            j.pack()
            jh=Label(d,text=h[f],font=("verdana",20),bg='blue',fg='yellow',width=25)
            jh.pack()
        def reset():
            global dw,da,f,h
            f=random.randrange(0,14,1)
            lbl.config(text=dw[f])
            en.delete(0,END)
            '''deletehint()'''
        def deletehint():
            jh.destroy()
            j.destroy()
        def checkans():
            global dw,da,f
            v=en.get()
            if v == da[f]:
                messagebox.showinfo("You are genius!!!!","THIS IS A CORRECT ANSWER")
                reset(),d.destroy(),hard(),deletehint()
            else:
                messagebox.showerror("ERROR","THIS IS NOT CORRECT,TRYAGAIN")
                en.delete(0,END),d.destroy(),hard()
        def end():
            messagebox.askquestion('end','surely end')
            d.destroy()
            i=Label(u,text= "!(•̀ᴗ•́)THANKYOU!(•̀ᴗ•́)!",font=('verdana',20),bg='green',fg='yellow',width=20)
            i.pack(pady=10)
        d=tkinter.Tk()
        d.title("JUMBLED WORDS")
        d['bg']="black"
        lb=Label(d,text="WELCOME TALENT",font=("algerian",21),bg="black",fg="white")
        lb.pack(pady=10)
        lbl=Label(d,text="WELCOmeTALNT",font=("verdana",20),bg="blue",fg='yellow',width=25,relief=GROOVE)
        lbl.pack(pady=10)
        k=StringVar()
        en=Entry(d,font=("verdana",15),textvariable=k)
        en.pack(pady=10)
        checkbtn=Button(d,text="check   ͡° ͜ʖ ͡°",font=("comic sans ms",16),bg='grey',fg='green',width=16,relief=GROOVE,command=checkans)
        checkbtn.pack(pady=10)
        resetbtn=Button(d,text="reset    ʕʘ̅͜ʘ̅ʔ",font=("comic sans ms",16),bg='grey',fg='red',width=16,relief=GROOVE,command=reset)
        resetbtn.pack()
        hintbtn=Button(d,text='hint   ☉_☉',font=('verdana',20),fg='yellow',bg='grey',width=18,command=hint)
        hintbtn.pack(pady=5)
        endbtn=Button(d,text='END  ┌(˘⌣˘)ʃ',font=('verdana',20),fg='violet',bg='grey',width=18,command=end)
        endbtn.pack(pady=10)
        default()
        d.mainloop()

    u=Toplevel()
    u.title(" words")
    u.geometry('800x500')
    u['bg']="black"
    

   
    
    bg=PhotoImage(file=r'C:/Users/Public/Pictures/Sample Pictures/asd.png')

    c=Canvas(u,width=800,height=500)

    c.pack(fill='both',expand=True)
    c.create_image(0,0,image=bg,anchor='nw')
    c.create_text(500,170,text='Select Level',font=('helvetica',50),fill='black')
    eb=Button(u,text="easy",font=("verdana",20),bg='black',fg='white',command=easy)
    #eb.pack(pady=50)
    em=Button(u,text="medium",font=("verdana",20),bg='black',fg='white',command=medium)
    #em.pack(pady=60)
    ed=Button(u,text="difficult",font=("verdana",20),bg='black',fg='white',command=hard)
    #ed.pack(pady=10)
    eb_window=c.create_window(625,300,anchor="nw",window=eb)
    em_window=c.create_window(610,425,anchor="nw",window=em)
    ed_window=c.create_window(613,550,anchor="nw",window=ed)

    u.mainloop()


'''wordjumble()'''







