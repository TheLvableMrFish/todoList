import tkinter as tk

# pip install ttkbootstrap
import ttkbootstrap as ttk

from getList import getTodoList
from taskFunctions import addTask, deleteTask

def clear_task_list_widget(task_grid):
    for widget in task_grid.winfo_children():
        widget.destroy()

def del_task(index, todoList):
    deleteTask(index, todoList)

    clear_task_list_widget(task_grid)

    generateList(todoList, task_grid)

def add_new_task(entry_str, todoList):
    addTask(entry_str, todoList) 

    generateList(todoList, task_grid)

def generateList(todoList, task_grid):
    
    for i, item in enumerate(todoList):

    # Create a label for each task
        task_label = ttk.Label(master=task_grid, text=f"{item[0]}")
        task_label.grid(row=i, column=0)

        task_btn = ttk.Button(master=task_grid, text="X", command=lambda i=i: del_task(i, todoList))
        task_btn.grid(row=i, column=2)

    task_grid.pack()

todoList = getTodoList()

# Create the main window
window = ttk.Window()
window.title('Todo List')
window.geometry('600x400')

# Create an entry widget for the task input
input_frame = ttk.Frame(master = window)
entry_str = tk.StringVar()
entry = ttk.Entry(master= input_frame, textvariable=entry_str)


# Create a button widget to enter task input
add_task_btn = ttk.Button(master = input_frame, text='Add Task', command=lambda: add_new_task(entry_str.get(), todoList))

# Attach entry, btn, and frame to the window
entry.pack(side='left', padx=(0,10))
add_task_btn.pack(side='right')
input_frame.pack(pady=10)

task_grid = ttk.Frame(master=window)

generateList(todoList, task_grid)

# Start the Tkinter event loop
window.mainloop()