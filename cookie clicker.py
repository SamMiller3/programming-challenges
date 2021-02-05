from tkinter import *
import time
click = 0
db = 1
master = Tk()

def buttonDouble():
    global db
    if db == 2:
        print("already baught")
    if db == 1:
        if clicks > 250:
            db = 2
            print("double clicks baught")
        if clicks < 250:
            print("more coins required, you need 250")
def buttonClick():
    global click
    click += 1 * db
    print("Cookie Clicks: " + str(click))
mainClickButton = Button(master, text="Click!", command = buttonClick)
mainBuyButton = Button(master, text="Buy Double Clicks", command = buttonDouble)
mainClickButton.pack()
mainBuyButton.pack()
mainloop()
