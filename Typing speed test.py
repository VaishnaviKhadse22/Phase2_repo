 '''Phase.2 - Task1'''
'''TYPING SPEED TEST'''

                           
from tkinter import *
import random
from timeit import default_timer 
import difflib
print("-----------Speed Typing Test in Python------------")
root=Tk()
root.title('Speed Typing Test in Python')
root.geometry("400x400")
entered=StringVar() 
greet = Label(root, font = ('arial', 30, 'bold'), text = "Welcome!")
greet.grid(row = 0,columnspan = 3)
words=["Let's check the typing speed!"]
word=random.choice(words)
def check():

    global entered
    global word
    global start

    string=f"{entered.get()}"
    end= default_timer()
    time= round(end-start,2)
    print(time)
    speed=round(len(word.split())*60/time,2)
    print(speed)
    if string==word:

        Msg1 ="Time= " + str(time) + ' seconds'
        Msg2=" Accuracy= 100% "
        Msg3= " Speed= " + str(speed) + 'wpm' 
    else:
        accuracy=difflib.SequenceMatcher(None,word,string).ratio()
        accuracy=str(round(accuracy*100,2))
        Msg1 ="Time= "+ str(time) + ' seconds'
        Msg2=" Accuracy= " + accuracy + '%'
        Msg3= " Speed= " + str(speed) + ' wpm'
    label=Label(root, font = ('arial', 15, 'bold'), text = Msg1)
    label.grid(row = 7, columnspan = 3)
    label=Label(root, font = ('arial', 15, 'bold'), text = Msg2)
    label.grid(row = 8, columnspan = 3)
    label=Label(root, font = ('arial', 15, 'bold'), text = Msg3)
    label.grid(row = 9, columnspan = 3)
def play():

    global word
    global start
    global entered 
    label=Label(root, font = ('arial', 15), text = "Type here")
    label.grid(row = 5, column=1)
    entered=StringVar() 
    enter=Entry(root,textvariable=entered,font =('arial', 15),width=20)
    enter.grid(row=5,column=3)
    btn = Button(root, text = "Check",command=check,bg="DodgerBlue2",fg="white", font = ('arial', 10))
    btn.grid(row = 6,columnspan = 6)
label=Label(root, font = ('arial', 20, 'bold'), text = word)
label.grid(row = 3, columnspan = 3)
btn = Button(root, text = " Start typing",command=play,bg="DodgerBlue2",fg="white", font = ('arial', 10))
btn.grid(row = 4,columnspan = 6)
start= default_timer()
mainloop()
