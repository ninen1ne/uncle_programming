# 31 Dec 2024 - Nine
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("500x500+470+200")

def hello():
    print('Greeting!')

frame1 = ttk.Frame(master=root)
frame1.place(x=20, y=50)

button1 = tk.Button(master=frame1, text='Hello')
button1.pack(ipadx=40) # ipad: internal padding

# do not called this func command argument will deal this part.
button2 = ttk.Button(master=frame1, text='hello2', command=hello) 
button2.pack(ipadx=20)


root.mainloop()