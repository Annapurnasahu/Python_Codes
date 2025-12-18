#step1: importing
from tkinter import * 

#step2: gui interaction 
window = Tk()
window.geometry('500x500')

# ADD NAME LABEL
label = Label(window, text= "Calculator (Annapurna Sahu)", font=("Arial", 18, "bold"))
label.place(x=150, y=10)

# Entry Box (moved down)
e = Entry(window , width = 56, borderwidth = 5)
e.place(x = 0 , y = 50)

# BUTTONS
def click(num): 
    result = e.get()
    e.delete(0,END)
    e.insert(0,str(result) + str(num))

Button(window, text='1', width=12, command=lambda:click(1)).place(x=10, y=100)
Button(window, text='2', width=12, command=lambda:click(2)).place(x=80, y=100)
Button(window, text='3', width=12, command=lambda:click(3)).place(x=160, y=100)

Button(window, text='4', width=12, command=lambda:click(4)).place(x=10, y=160)
Button(window, text='5', width=12, command=lambda:click(5)).place(x=80, y=160)
Button(window, text='6', width=12, command=lambda:click(6)).place(x=170, y=160)

Button(window, text='7', width=12, command=lambda:click(7)).place(x=10, y=220)
Button(window, text='8', width=12, command=lambda:click(8)).place(x=80, y=220)
Button(window, text='9', width=12, command=lambda:click(9)).place(x=170, y=220)

Button(window, text='0', width=12, command=lambda:click(0)).place(x=10, y=280)

# operators
def add():
    global math, i
    math = "addition"
    i = int(e.get())
    e.delete(0,END)

Button(window, text='+', width=12, command=add).place(x=80, y=280)

def sub():
    global math, i
    math = "subtraction"
    i = int(e.get())
    e.delete(0,END)

Button(window, text='-', width=12, command=sub).place(x=170, y=280)

def mult():
    global math, i
    math = "Multiplication"
    i = int(e.get())
    e.delete(0,END)

Button(window, text='*', width=12, command=mult).place(x=10, y=340)

def div():
    global math, i
    math = "Division"
    i = int(e.get())
    e.delete(0,END)

Button(window, text='/', width=12, command=div).place(x=80, y=340)

def equal():
    n2 = int(e.get())
    e.delete(0, END)

    if math == "addition":
        e.insert(0, i + n2)
    elif math == "subtraction":
        e.insert(0, i - n2)
    elif math == "Multiplication":
        e.insert(0, i * n2)
    elif math == "Division":
        e.insert(0, i / n2)

Button(window, text='=', width=12, command=equal).place(x=170, y=340)

def clear():
    e.delete(0, END)

Button(window, text='clear', width=12, command=clear).place(x=10, y=400)

# step4: mainloop
mainloop()
