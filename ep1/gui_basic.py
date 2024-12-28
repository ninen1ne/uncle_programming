# 28 dec 2024 - Nine
# Basic GUI
import tkinter as tk

window = tk.Tk()
window.geometry('500x500')

label1 = tk.Label(master=window, text='Hello/nWorld', font=(None, 30))
label1.pack()

window.mainloop()