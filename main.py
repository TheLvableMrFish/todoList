import tkinter as tk

# pip install ttkbootstrap
import ttkbootstrap as ttk
# from tkinter import ttk

from getList import getTodoList
from taskFunctions import addTask, deleteTask

class ListFrame(ttk.Frame):
    def __init__(self, parent, tasks, item_height):
        super().__init__(master=parent)
        self.pack(expand=True, fill='both')

        # widget data
        self.tasks = tasks
        self.task_number = len(tasks)
        self.item_height = self.task_number * item_height

        # Frame for entry and button at top
        self.top_frame = ttk.Frame(self)
        self.top_frame.pack(fill='x', padx=10, pady=10)

        # Entry and Button
        self.entry = ttk.Entry(self.top_frame, width=30)
        self.entry.pack(side='left', padx=(0, 10))
        self.button = ttk.Button(self.top_frame, text='Submit', command=self) # fix
        self.button.pack(side='left')

        # canvas 
        self.canvas = tk.Canvas(self, background='red', scrollregion=(0, 0, self.winfo_width(), self.item_height))
        self.canvas.pack(expand=True, fill='both')

        # widget frame / display frame
        self.frame = ttk.Frame(self.canvas)

        for task in enumerate(self.tasks):
            self.create_task(task).pack(expand=True, fill='both', pady=4, padx=10)
            
        # events
        self.canvas.bind_all('<MouseWheel>', lambda e: self.canvas.yview_scroll(-int(e.delta/60), 'units'))
        self.bind('<Configure>', self.update_size)

    def create_task(self, task):
        frame = ttk.Frame(self.frame)

        # Grid layout
        frame.rowconfigure(0, weight=1)
        frame.columnconfigure((0, 1, 2, 3, 4), weight=1, uniform='a')

        # widgets
        ttk.Label(frame, text=f'{task[1]}').grid(row=0, column=0, columnspan=5, sticky='w')
        ttk.Button(frame, text='Delete').grid(row=0, column=5, columnspan=2, sticky='nsew')

        return frame
    
    def update_size(self, e):
        if self.item_height >= self.winfo_height():
            height = self.item_height
            self.canvas.bind_all('<MouseWheel>', lambda e: self.canvas.yview_scroll(-int(e.delta/60), 'units'))
        else:
            height = self.winfo_height()
            self.canvas.unbind_all('<MouseWheel>')
        self.canvas.create_window(
            (0,0),
            window=self.frame,
            anchor='nw',
            width=self.winfo_width(),
            height=height
        )


# def clear_task_list_widget(task_grid):
#     for widget in task_grid.winfo_children():
#         widget.destroy()

# def del_task(index, todoList):
#     deleteTask(index, todoList)

#     clear_task_list_widget(task_grid)

#     generateList(todoList, task_grid)

# def add_new_task(entry_str, todoList):
#     addTask(entry_str, todoList) 

#     generateList(todoList, task_grid)

# def generateList(todoList, task_grid):
    
#     for i, item in enumerate(todoList):

#     # Create a label for each task
#         task_label = ttk.Label(master=task_grid, text=f"{item[0]}")
#         task_label.grid(row=i, column=0)

#         task_btn = ttk.Button(master=task_grid, text="X", command=lambda i=i: del_task(i, todoList))
#         task_btn.grid(row=i, column=2)

#     task_grid.pack()

todoList = getTodoList()

# Create the main window
window = ttk.Window()
# window = tk.Tk()
window.title('Todo List')
window.geometry('600x400')

# # Create an entry widget for the task input
# input_frame = ttk.Frame(master = window)
# entry_str = tk.StringVar()
# entry = ttk.Entry(master= input_frame, textvariable=entry_str)


# # Create a button widget to enter task input
# add_task_btn = ttk.Button(master = input_frame, text='Add Task', command=lambda: add_new_task(entry_str.get(), todoList))

# # Attach entry, btn, and frame to the window
# entry.pack(side='left', padx=(0,10))
# add_task_btn.pack(side='right')
# input_frame.pack(pady=10)

# task_grid = ttk.Frame(master=window)

# generateList(todoList, task_grid)

# sample List
task_list = ['Milk cow','fix bus', 'create a mouse', 'find pluto', 'save the world']

list_frame = ListFrame(window, task_list, 100)

# Start the Tkinter event loop
window.mainloop()