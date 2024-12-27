from tkinter import *
import random

root = Tk()
root.geometry("200x250")

title_label = Label(root, text="повешение зарплата?")
title_label.pack()

def yes_click():
    title_label.config(text="Хороший сотрудник")
    yes.place_forget()
    no.place_forget()

def no_click():
    no.place(x=random.randint(20, 150), y=random.randint(20, 150))

yes = Button(root, text="Yes", command=yes_click, bg="green", fg="white")
yes.place(x=20, y=100)

no = Button(root, text='No', command=no_click, bg="red", fg="white")
no.place(x=100, y=100)

root.mainloop()
