# 2 Jan 2025 - Nine
# This file contain record class for record_expenses.py

import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from datetime import datetime
import csv

class Record(ctk.CTk):
    def __init__(self):
        # window setup
        ctk.set_appearance_mode('light')
        super().__init__(fg_color='white')

        self.title('Record expenses by Norawee')
        self.geometry("500x500+900+200")
        FONT1 = (None, 20)

        ctk.CTkLabel(self, text="Record expenses").pack()



        # widgets zone
        frame = ctk.CTkFrame(master=self, width=250, height=400)
        frame.place(x=125, y=50)
        label1 = ctk.CTkLabel(frame, text='รายการค่าใช้จ่าย', font=FONT1)
        label1.pack()
        self.v_expense = ctk.StringVar()
        self.entry1 = ctk.CTkEntry(frame, textvariable=self.v_expense, font=FONT1)
        self.entry1.pack(pady=10)

        label2 = ctk.CTkLabel(master=frame, text='ราคา (บาท)', font=FONT1)
        label2.pack()
        self.v_price = ctk.StringVar()
        self.entry2 = ctk.CTkEntry(frame, textvariable=self.v_price, font=FONT1)
        self.entry2.pack(pady=10)

        label3 = ctk.CTkLabel(frame, text='จำนวนสินค้า', font=FONT1)
        label3.pack()
        self.v_amount = ctk.StringVar()
        self.entry3 = ctk.CTkEntry(frame, textvariable=self.v_amount, font=FONT1)
        self.entry3.pack(pady=10)

        button = ctk.CTkButton(frame, text='Save', command=self.save) 
        button.pack(ipadx=50, ipady=10)

        # make entry avaible
        self.entry_fields = [self.entry1, self.entry2, self.entry3]
        self.bind('<Return>', self.save) # must add in def save() function too

        # loop
        self.mainloop()
    
    def save(self, event=''):
        # .get() ดึงค่าจาก v_expense = StringVar
        expense = self.v_expense.get()
        price = self.v_price.get()
        amount = self.v_amount.get()
        total = float(price) * float(amount)
        date = datetime.now()
        print(f'รายการ: {expense} ราคา: {price} จำนวน: {amount} total: {total:.2f} date: {date}')
        # clear previous data in entry field
        self.v_expense.set('')
        self.v_price.set('')
        self.v_amount.set('')
        self.write_to_csv(expense=expense, price=price, amount=amount, total=total, date=date)
        # made cursor go to the first entry as default
        self.entry1.focus()

    def write_to_csv(self, expense, price, amount, total, date):
        with open('ep3/savedata.csv', 'a',encoding='utf-8', newline='') as f:
            # with คือสั่งเปิด file เเล้วปิด autonomous
            # 'a' การบันทึกข้อมูลเรื่อยๆ เพิ่มต่อจากข้อมูลเก่า(append)
            # newline ทำให้ข้อมูลไม่มีบรรทัดว่าง
            file_writer = csv.writer(f) # create func to write data
            data = [expense, price, amount, total, date]
            file_writer.writerow(data)


record = Record()
