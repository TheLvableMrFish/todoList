import tkinter as tk

from getList import getTodoList
from taskFunctions import addTask

todoList = getTodoList()

# Create the main window
root = tk.Tk()
root.title("Todo List")

# Create an entry widget for the task input
entry = tk.Entry(root, width=30)
entry.pack(padx=10, pady=10)

# Create a button widget to enter task input
add_task_btn = tk.Button(root, text="Add", command=lambda: addTask(entry.get(), todoList))
add_task_btn.pack(padx=10, pady=20)

# Create the frame to hold the lists
frame = tk.Frame(root)
frame.pack(padx=180, pady=40)

# Start the Tkinter event loop
root.mainloop()