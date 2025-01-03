# 31 Dec 2024 - Nine
"""record expenses program
This program will record expenses into csv(comma-separated values) file
"""
import tkinter as tk
from tkinter import ttk
from datetime import datetime
import csv

root = tk.Tk()
root.title('Record expenses by Norawee')
root.geometry("500x500+470+200")

def save(event=None):
    # .get() ดึงค่าจาก v_expense = StringVar
    expense = v_expense.get()
    price = v_price.get()
    amount = v_amount.get()
    total = float(price) * float(amount)
    date = datetime.now()
    print(f'รายการ: {expense} ราคา: {price} จำนวน: {amount} total: {total:.2f} date: {date}')
    # clear previous data in entry field
    v_expense.set('')
    v_price.set('')
    v_amount.set('')
    write_to_csv(expense=expense, price=price, amount=amount, total=total, date=date)
    # made cursor go to the first entry as default
    Entry1.focus()

def write_to_csv(expense, price, amount, total, date):
    with open('ep3/savedata.csv', 'a',encoding='utf-8', newline='') as f:
        # with คือสั่งเปิด file เเล้วปิด autonomous
        # 'a' การบันทึกข้อมูลเรื่อยๆ เพิ่มต่อจากข้อมูลเก่า(append)
        # newline ทำให้ข้อมูลไม่มีบรรทัดว่าง
        file_writer = csv.writer(f) # create func to write data
        data = [expense, price, amount, total, date]
        file_writer.writerow(data)

# make entry avaible
root.bind('<Return>', save) # must add in def save() function too
root.bind('<Up>', lambda e: Entry1.focus())
root.bind('<Down>', lambda e: Entry2.focus())

frame1 = ttk.Frame(master=root)
frame1.place(x=115, y=50)

FONT1 = (None, 20)

#-------------text1--------------
Label = ttk.Label(master=frame1, text='รายการค่าใช้จ่าย', font=FONT1)
Label.pack()
v_expense = tk.StringVar() # special variable to stored data of gui
Entry1 = ttk.Entry(master=frame1, textvariable=v_expense, font=FONT1)
Entry1.pack()
#--------------------------------

# button1 = tk.Button(master=frame1, text='Hello')
# button1.pack(ipadx=40) # ipad: internal padding


#-------------text2--------------
Label = ttk.Label(master=frame1, text='ราคา (บาท)', font=FONT1)
Label.pack()
v_price = tk.StringVar()
Entry2 = ttk.Entry(master=frame1, textvariable=v_price, font=FONT1)
Entry2.pack()
#--------------------------------

Label = ttk.Label(master=frame1, text='จำนวนสินค้า', font=FONT1)
Label.pack()
v_amount = tk.StringVar()
Entry3 = ttk.Entry(master=frame1, textvariable=v_amount, font=FONT1)
Entry3.pack()


# do not called this func command argument will deal this part.
button2 = ttk.Button(master=frame1, text='Save', command=save) 
button2.pack(ipadx=50, ipady=20)


root.mainloop()

