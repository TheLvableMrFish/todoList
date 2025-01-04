import tkinter as tk

# pip install ttkbootstrap
import ttkbootstrap as ttk

from getList import getTodoList
from taskFunctions import addTask

todoList = getTodoList()

# Create the main window
window = ttk.Window()
window.title('Todo List')
window.geometry('300x100')

# Create an entry widget for the task input
input_frame = ttk.Frame(master = window)
entry_str = tk.StringVar()
entry = ttk.Entry(master= input_frame, textvariable=entry_str)


# Create a button widget to enter task input
add_task_btn = ttk.Button(master = input_frame, text='Add', command=lambda: addTask(entry_str.get(), todoList))

# Attach entry, btn, and frame to the window
entry.pack(side='left', padx=(0,10))
add_task_btn.pack(side='right')
input_frame.pack(pady=10)

# Start the Tkinter event loop
window.mainloop()