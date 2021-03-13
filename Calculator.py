from tkinter import *
import os

root = Tk()
root.title = "Simple Calculator"

#Creating Functions for Buttons

def button_Click(number):
    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))

def button_addition():
    global first_Number
    first= e.get()
    first_Number=int(first)
    e.delete(0,END)
    global symbol
    symbol="add"

def button_subtraction():
    global first_Number
    first = e.get()
    first_Number = int(first)
    e.delete(0,END)
    global symbol
    symbol = "sub"

def button_multiplication():
    global first_Number
    first = e.get()
    first_Number=int(first)
    e.delete(0,END)
    global symbol
    symbol = "mul"

def button_division():
    global first_Number
    first=e.get()
    first_Number=int(first)
    e.delete(0,END)
    global symbol
    symbol="div"

def button_clear():
    e.delete(0,END)

def button_equalto():
    second_Number=int(e.get())
    e.delete(0,END)
    
    if symbol=="add":
        e.insert(0,first_Number+second_Number)
    
    if symbol=="sub":
        e.insert(0,first_Number-second_Number)

    if symbol=="mul":
        e.insert(0,first_Number*second_Number)

    if symbol=="div":
        e.insert(0,first_Number/second_Number)

#Creating Entry Widget

e=Entry(root, width=50, borderwidth=4)
e.grid(row=0, column=0, columnspan=4, padx=40, pady=20)

#Creating Buttons

button_1=Button(root, text="1", padx=40, pady=40, command=lambda: button_Click(1))
button_2=Button(root, text="2", padx=40, pady=40, command=lambda: button_Click(2))
button_3=Button(root, text="3", padx=40, pady=40, command=lambda: button_Click(3))
button_4=Button(root, text="4", padx=40, pady=40, command=lambda: button_Click(4))
button_5=Button(root, text="5", padx=40, pady=40, command=lambda: button_Click(5))
button_6=Button(root, text="6", padx=40, pady=40, command=lambda: button_Click(6))
button_7=Button(root, text="7", padx=40, pady=40, command=lambda: button_Click(7))
button_8=Button(root, text="8", padx=40, pady=40, command=lambda: button_Click(8))
button_9=Button(root, text="9", padx=40, pady=40, command=lambda: button_Click(9))
button_0=Button(root, text="0", padx=40, pady=40, command=lambda: button_Click(0))
button_add=Button(root, text="+", padx=40, pady=40, command=button_addition)
button_sub=Button(root, text="-", padx=40, pady=40, command=button_subtraction)
button_mul=Button(root, text="*", padx=40, pady=40, command=button_multiplication)
button_div=Button(root, text="/", padx=40, pady=40, command=button_division) 
button_equal=Button(root, text="=", padx=40, pady=40, command=button_equalto)
button_clear=Button(root, text="Clear", padx=40, pady=40, command=button_clear)

#Placing Buttons on the Screen

button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)
button_add.grid(row=1, column=3)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_sub.grid(row=2, column=3)

button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)
button_mul.grid(row=3, column=3)

button_clear.grid(row=4, column=0)
button_0.grid(row=4, column=1)
button_equal.grid(row=4, column=2)
button_div.grid(row=4, column=3)

root.mainloop()
