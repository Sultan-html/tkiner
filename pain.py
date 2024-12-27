from tkinter import *



root = Tk()

root.geometry("300x300")
root.title("Байель app")
label = Label(root, text="Привет Байель",font=(80))
label.pack()
def button_clicked():
    but.pack()
    label.forget()
    next_label = Label(root, text='Вы перешли на другую страницу',font=('arial',10))
    next_label.pack()
    but.forget()
but = Button(text='Далее',fg='yellow',bg='white',command=button_clicked,font=('Ariel',20))
but.pack()
root.mainloop()