import tkinter as tk
from tkinter import StringVar, Entry, Button, Frame

def click(event):
    global scvalue
    text = event.widget.cget("text")

    if text == "=":
        try:
            value = eval(scvalue.get())
            scvalue.set(value)
        except Exception as e:
            scvalue.set("Error")
        screen.update()
    elif text == "AC":
        scvalue.set("")
        screen.update()
    elif text == "⌫":
        scvalue.set(scvalue.get()[:-1])
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

root = tk.Tk()
root.geometry("400x600")
root.title("Calculator")
root.configure(bg="white")

scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font="lucida 16 bold", bg="white", fg="black", bd=0, justify='right')
screen.pack(fill=tk.X, ipadx=8, pady=10, padx=10)

button_texts = [
    ["AC", "%", "⌫", "÷"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["00", "0", ".", "="]
]

button_colors = {
    "=": "red",
    "AC": "gray",
    "⌫": "gray",
    "÷": "gray",
    "*": "gray",
    "%": "gray",
    "-": "gray",
    "+": "gray"
}

for row in button_texts:
    f = Frame(root, bg="white")
    for text in row:
        bg_color = button_colors.get(text, "black")
        fg_color = "white" if bg_color == "black" else "black"
        b = Button(f, text=text, padx=20, pady=20, font="lucida 18 bold", bg=bg_color, fg=fg_color, bd=0, highlightthickness=0)
        b.pack(side=tk.LEFT, padx=10, pady=10)
        b.bind("<Button-1>", click)
    f.pack()

root.mainloop()