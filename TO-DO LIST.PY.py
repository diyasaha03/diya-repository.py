import tkinter as tk

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def delete_task():
    try:
        index = listbox.curselection()[0]
        listbox.delete(index)
    except IndexError:
        pass

def mark_task():
    try:
        index = listbox.curselection()[0]
        listbox.itemconfig(index, fg="red")
    except IndexError:
        pass

root = tk.Tk()  
root.title("To-Do List")

frame = tk.Frame(root)   
frame.pack()

listbox = tk.Listbox(frame, width=50, height=10, bd=0, font=("Courier New", 12), selectbackground="#a3a3a3")
listbox.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

entry = tk.Entry(root, font=("Courier New", 12))   
entry.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

add_button = tk.Button(button_frame, text="Add Task", command=add_task, font=("Courier New", 12))
add_button.pack(side=tk.LEFT)

delete_button = tk.Button(button_frame, text="Delete Task", command=delete_task, font=("Courier New", 12))
delete_button.pack(side=tk.LEFT)

mark_button = tk.Button(button_frame, text="Mark Task", command=mark_task, font=("Courier New", 12))  # Corrected button creation syntax
mark_button.pack(side=tk.LEFT)

root.mainloop()