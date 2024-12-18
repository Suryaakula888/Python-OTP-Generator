import tkinter as tk
from tkinter import Tk,Label,Spinbox,Button,Entry
import random
import string
import pyperclip

root=tk.Tk()
root.title("OTP Generator app")
root.geometry("300x300")
root.resizable(0,0)

Label(root,text="OTP Generator",font="arial 20 bold").pack()
Label(root,text="Surya",font="arial 20 bold").pack(side="bottom")

label_len = tk.Label(root,text="Length of OTP").pack()
label_len=tk.IntVar()

label_str=tk.Spinbox(root,from_=4,to_=15,textvariable=label_len,width=20).pack()
label_str=tk.IntVar()

def generator():
    password=[]

    if label_len.get()>=4:
        
        password.append(random.choice(string.digits))
        password.append(random.choice(string.digits))
        password.append(random.choice(string.digits))
        password.append(random.choice(string.digits))

        for _ in range(label_len.get()-4):
            password.append(random.choice(string.digits))
            
        random.shuffle(password)

    else:
        for _ in range(label_len.get()):
            password.append(random.choice(string.digits))

        
        
    label_str.set("".join(password))    


def copy_password():
    pyperclip.copy(label_str.get())   

Button(root,text="Generate",command=generator).pack(pady=30)
Entry(root,textvariable=label_str).pack(pady=30)

Button(root,text="copy password",command=copy_password).pack(pady=30)

root.mainloop()




