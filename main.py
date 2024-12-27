import tkinter as tk
from random import randint

def on_yes():
    label.config(text="Я знал...")
    yes_button.place_forget()
    no_button.place_forget()
    yes_button.place_forget()
def on_no(event=None):
    no_button.place(x=randint(50, 90), y=randint(50, 100))

window = tk.Tk()
window.geometry("300x250")

label = tk.Label(window, text="Ты гей?", font=("Arial", 30))
label.pack(pady=30)

yes_button = tk.Button(window, text="Да", command=on_yes)
yes_button.pack(side="left", padx=50, pady=50)

no_button = tk.Button(window, text="Нет", command=on_no)
no_button.pack(side="right", padx=30, pady=30, )

window.mainloop()
