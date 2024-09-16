import tkinter as tk
from tkinter import PhotoImage, messagebox
def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Enter the task !")

def delete_task():
    selected_task = listbox.curselection()
    if selected_task:
        listbox.delete(selected_task)
    else:
        messagebox.showwarning("Warning", "SELECT A TASK TO DELETE !")

def mark_complete():
    selected_task = listbox.curselection()
    if selected_task:
        task = listbox.get(selected_task)
        listbox.delete(selected_task)
        listbox.insert(tk.END, f"{task} - Completed")
    else:
        messagebox.showwarning("Warning", "SELECT A TASK TO BE MARKED AS COMPLETED !")
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x500")
root.resizable(False, False)
bgi = PhotoImage(file="C:/Users/dell/Downloads/1000108336.png")
bgl = tk.Label(root, image=bgi)
bgl.place(x=0, y=0, relwidth=1, relheight=1)
entry = tk.Entry(root, width=35)
entry.pack(pady=10)
listbox = tk.Listbox(root, width=35, height=12)
listbox.pack(pady=10)
tk.Button(root, text="Add Task", command=add_task).pack(pady=5)
tk.Button(root, text="Delete Task", command=delete_task).pack(pady=5)
tk.Button(root, text="Mark as Complete", command=mark_complete).pack(pady=5)
root.mainloop()
