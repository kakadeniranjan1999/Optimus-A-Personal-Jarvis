from threading import *
from tkinter import *
import datetime
import time
flag=0
d={'one':None,'two':None,'three':None,'four':None,'five':None,'six':None,'seven':None,'eight':None,'nine':None}
def change(a):
    global flag
    global d
    global winner
    winner='none'
    if(a==0):
        rset()
    elif(d.get('one')=='X' and d.get('two')=='X' and d.get('three')=='X' or d.get('four')=='X' and d.get('five')=='X' and d.get('six')=='X' or d.get('seven')=='X' and d.get('eight')=='X' and d.get('nine')=='X' or d.get('one')=='X' and d.get('five')=='X' and d.get('nine')=='X' or d.get('three')=='X' and d.get('five')=='X' and d.get('seven')=='X' or d.get('one')=='X' and d.get('four')=='X' and d.get('seven')=='X' or d.get('two')=='X' and d.get('five')=='X' and d.get('eight')=='X' or d.get('three')=='X' and d.get('six')=='X' and d.get('nine')=='X'):
        l.config(text='X wins',fg='red')  
        winner='X is the winner'
        d={'one':None,'two':None,'three':None,'four':None,'five':None,'six':None,'seven':None,'eight':None,'nine':None}
    elif(d.get('one')=='O' and d.get('two')=='O' and d.get('three')=='O' or d.get('four')=='O' and d.get('five')=='O' and d.get('six')=='O' or d.get('seven')=='O' and d.get('eight')=='O' and d.get('nine')=='O' or d.get('one')=='O' and d.get('five')=='O' and d.get('nine')=='O' or d.get('three')=='O' and d.get('five')=='O' and d.get('seven')=='O' or d.get('one')=='O' and d.get('four')=='O' and d.get('seven')=='O' or d.get('two')=='O' and d.get('five')=='O' and d.get('eight')=='O' or d.get('three')=='O' and d.get('six')=='O' and d.get('nine')=='O'):
        l.config(text='O wins',fg='green')
        winner='O is the winner'
        d={'one':None,'two':None,'three':None,'four':None,'five':None,'six':None,'seven':None,'eight':None,'nine':None}
    else:
        if(a==1):
            if(flag==0):
                b1.config(text='X',bg='Red')
                d['one']='X'
                flag=1
            else:    
                b1.config(text='O',bg='Green')
                d['one']='O'
                flag=0
        elif(a==2):
            if(flag==0):            
                b2.config(text='X',bg='Red')
                flag=1
                d['two']='X'
            else:    
                b2.config(text='O',bg='Green')
                flag=0
                d['two']='O'
        elif(a==3):
            if(flag==0):            
                b3.config(text='X',bg='Red')
                flag=1
                d['three']='X'
            else:    
                b3.config(text='O',bg='Green')
                flag=0
                d['three']='O'
        elif(a==4):
            if(flag==0):            
                b4.config(text='X',bg='Red')
                flag=1
                d['four']='X'
            else:    
                b4.config(text='O',bg='Green')
                flag=0
                d['four']='O'
        elif(a==5):
            if(flag==0):            
                b5.config(text='X',bg='Red')
                flag=1
                d['five']='X'
            else:    
                b5.config(text='O',bg='Green')
                flag=0
                d['five']='O'
        elif(a==6):
            if(flag==0):            
                b6.config(text='X',bg='Red')
                flag=1
                d['six']='X'
            else:    
                b6.config(text='O',bg='Green')
                d['six']='O'
                flag=0
        elif(a==7):
             if(flag==0):
                 b7.config(text='X',bg='Red')
                 flag=1
                 d['seven']='X'
             else:    
                 b7.config(text='O',bg='Green')
                 d['seven']='O'
                 flag=0
        elif(a==8):
             if(flag==0):            
                 b8.config(text='X',bg='Red')
                 flag=1
                 d['eight']='X'
             else:    
                 b8.config(text='O',bg='Green')
                 d['eight']='O'
                 flag=0
        elif(a==9):
             if(flag==0):            
                 b9.config(text='X',bg='Red')
                 flag=1
                 d['nine']='X'
             else:    
                 b9.config(text='O',bg='Green')
                 flag=0
                 d['nine']='O'
def rset():
    b1.config(text='1',height=5,width=10,bg='light grey')
    b2.config(text='2',height=5,width=10,bg='light grey')
    b3.config(text='3',height=5,width=10,bg='light grey')
    b4.config(text='4',height=5,width=10,bg='light grey')
    b5.config(text='5',height=5,width=10,bg='light grey')
    b6.config(text='6',height=5,width=10,bg='light grey')
    b7.config(text='7',height=5,width=10,bg='light grey')
    b8.config(text='8',height=5,width=10,bg='light grey')
    b9.config(text='9',height=5,width=10,bg='light grey')  
    l.config(text='',fg='green')
    d={'one':None,'two':None,'three':None,'four':None,'five':None,'six':None,'seven':None,'eight':None,'nine':None}
def timer_print():
    while(True):
        l1.config(text=datetime.datetime.now())
        time.sleep(1)
frame=Tk()
frame.geometry('500x500')
frame.title('Tic-Tac-Toe')
b1=Button(frame,text='1',command=lambda:change(1),height=5,width=10)
b1.place(x=20,y=100)
b2=Button(frame,text='2',command=lambda:change(2),height=5,width=10)
b2.place(x=100,y=100)
b3=Button(frame,text='3',command=lambda:change(3),height=5,width=10)
b3.place(x=180.5,y=100)
b4=Button(frame,text='4',command=lambda:change(4),height=5,width=10)
b4.place(x=20,y=184.5)
b5=Button(frame,text='5',command=lambda:change(5),height=5,width=10)
b5.place(x=100,y=184.5)
b6=Button(frame,text='6',command=lambda:change(6),height=5,width=10)
b6.place(x=180.5,y=184.5)
b7=Button(frame,text='7',command=lambda:change(7),height=5,width=10)
b7.place(x=20,y=269.5)
b8=Button(frame,text='8',command=lambda:change(8),height=5,width=10)
b8.place(x=100,y=269.5)
b9=Button(frame,text='9',command=lambda:change(9),height=5,width=10)
b9.place(x=180.5,y=269.5)
reset=Button(frame,text='Reset',command=lambda:change(0),font=44)
reset.place(x=105,y=390)
l=Label(frame,font=100)
l.place(x=105,y=50)
l1=Label(frame,font=100,text=datetime.datetime.now())
l1.place(x=110,y=20)
thread1=Thread(target=timer_print)
thread1.start()
def start_game():
    frame.mainloop()