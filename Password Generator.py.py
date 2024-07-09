
import tkinter as tk
from tkinter import StringVar, IntVar
import random
import string

def get_pass():
    pass1 = string.ascii_letters + string.digits + string.punctuation
    password = ""

    for x in range(pwd_len.get()):
        password += random.choice(pass1)
    
    passstr.set(password)

def set_length(length):
    pwd_len.set(length)

root = tk.Tk()
root.geometry("400x250")

passstr = StringVar()
pwd_len = IntVar()

tk.Label(root, text="Password Generator", font=("Calibri", 18, "bold")).pack()
tk.Label(root, text="Select password length").pack(pady=9)

length_frame = tk.Frame(root)
length_frame.pack(pady=2)

tk.Radiobutton(length_frame, text="Small (8 chars)", variable=pwd_len, value=8, command=lambda: set_length(8)).pack(side=tk.LEFT)
tk.Radiobutton(length_frame, text="Medium (12 chars)", variable=pwd_len, value=12, command=lambda: set_length(12)).pack(side=tk.LEFT)
tk.Radiobutton(length_frame, text="Large (16 chars)", variable=pwd_len, value=16, command=lambda: set_length(16)).pack(side=tk.LEFT)

tk.Button(root, text="Generate Password", command=get_pass).pack(pady=15)
tk.Entry(root, textvariable=passstr).pack(pady=2)

root.mainloop()