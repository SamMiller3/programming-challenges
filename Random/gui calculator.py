#calc CALCULATOR
from tkinter import *
import tkinter as tk
calc = Tk(className='calc Calculator')
calc.geometry("500x200")
txt = ""
tx = ""
temp = ""
label = Label(calc, text = str(txt))
def Click1():
    global txt
    global tx
    tx = tx + "1"
    txt = txt + "1"
    label.configure(text=txt)
def Click2():
    global txt
    global tx
    tx = tx + "2"
    txt = txt + "2"
    label.configure(text=txt)
def Click3():
    global txt
    global tx
    tx = tx + "3"
    txt = txt + "3"
    label.configure(text=txt)
def Click4():
    global txt
    global tx
    tx = tx + "4"
    txt = txt + "4"
    label.configure(text=txt)
def Click5():
    global txt
    global tx
    tx = tx + "5"
    txt = txt + "5"
    label.configure(text=txt)
def Click6():
    global txt
    global tx
    tx = tx + "6"
    txt = txt + "6"
    label.configure(text=txt)
def Click7():
    global txt
    global tx
    tx = tx + "7"
    txt = txt + "7"
    label.configure(text=txt)
def Click8():
    global txt
    global tx
    tx = tx + "8"
    txt = txt + "8"
    label.configure(text=txt)
def Click9():
    global txt
    global tx
    tx = tx + "9"
    txt = txt + "9"
    label.configure(text=txt)
def minus():
    global txt
    global temp
    global tx
    if "-" not in txt:
        temp = tx
        tx = ""
        txt = txt + "-"
        label.configure(text=txt)
    else:
        equals()
def plus():
    global txt
    global tx
    global temp
    if "+" not in txt:
        temp = tx
        tx = ""
        txt = txt + "+"
        label.configure(text=txt)
    else:
        equals()
def times():
    global txt
    global tx
    global temp
    if "*" not in txt:
        temp = tx
        tx = ""
        txt = txt + "*"
        label.configure(text=txt)
    else:
        equals()
def divide():
    global txt
    global tx
    global temp
    if "÷" not in txt:
        temp = tx
        tx = ""
        txt = txt + "÷"
        label.configure(text=txt)
    else:
        equals()
def delete():
    global txt
    global tx
    txt = txt[:-1]
    tx = tx[:-1]
    label.configure(text=txt)
def equals():
    global txt
    global temp
    global tx
    if "-" in txt:
        txt = str(int(temp) - int(tx))
    if "+" in txt:
        txt = str(int(temp) + int(tx))
    if "÷" in txt:
        txt = str(int(temp) / int(tx))
    if "*" in txt:
        txt = str(int(temp) * int(tx))
    
    tx = txt
    temp = ""
    label.configure(text=txt)
one = Button(calc, text="1", command = Click1)
two = Button(calc, text="2", command = Click2)
three = Button(calc, text="3", command = Click3)
four = Button(calc, text="4", command = Click4)
five = Button(calc, text="5", command = Click5)
six = Button(calc, text="6", command = Click6)
seven = Button(calc, text="7", command = Click7)
eight = Button(calc, text="8", command = Click8)
nine = Button(calc, text="9", command = Click9)
plus = Button(calc, text="+", command = plus)
minus = Button(calc, text="-", command = minus)
equal = Button(calc, text="=", command = equals)
divide = Button(calc, text="÷", command = divide)
times = Button(calc, text="*", command = times)
delete = Button(calc, text="del", command = delete)


one.grid(column=0, row=1)   
two.grid(column=1, row=1)
three.grid(column=2, row=1)   
four.grid(column=0, row=2)
label.grid(column=4, row=0)
five.grid(column=1, row=2)   
six.grid(column=2, row=2)
seven.grid(column=0, row=3)   
eight.grid(column=1, row=3) 
nine.grid(column=2, row=3)
minus.grid(column=0, row=4)   
plus.grid(column=1, row=4) 
equal.grid(column=2, row=4)
divide.grid(column=0, row=5)   
times.grid(column=1, row=5) 
delete.grid(column=2, row=5)

mainloop()
