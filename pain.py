from tkinter import *

root = Tk()

root.geometry("400x300")
root.title("Приложение Байель")

label = Label(root, text="Привет, Байель!", font=("Arial", 16), pady=20)
label.pack()

def show_second_message():
    label.config(text="Вы перешли на другую страницу")
    but_two.pack_forget()

def show_third_message():
    label.config(text="Ты чо тупой?")
    but.pack_forget()

but = Button(root, text="Далее", fg="white", bg="blue", font=("Arial", 14), command=show_second_message)
but.pack(pady=10)

but_two = Button(root, text="Мугагагага", fg="white", bg="red", font=("Arial", 14), command=show_third_message)
but_two.pack(pady=10)

root.mainloop()
