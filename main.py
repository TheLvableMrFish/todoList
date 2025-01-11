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
        self.item_height = item_height
        self.total_height = self.task_number * item_height

        # Frame for entry and button at top
        self.top_frame = ttk.Frame(self)
        self.top_frame.pack(fill='x', padx=10, pady=10)

        # Entry and Button
        self.entry_str = tk.StringVar()
        self.entry = ttk.Entry(self.top_frame, width=30, textvariable=self.entry_str)
        self.entry.pack(side='left', padx=(0, 10))
        self.button = ttk.Button(self.top_frame, text='Submit', command=lambda: self.add_new_task(self.entry_str.get(), todoList))
        self.button.pack(side='left')

        self.generate_canvas()

        self.generate_tasks()
            
        # events
        self.canvas.bind_all('<MouseWheel>', lambda e: self.canvas.yview_scroll(-int(e.delta/60), 'units'))
        self.bind('<Configure>', self.update_size)
    
    def generate_canvas(self):
        # canvas 
        self.canvas = tk.Canvas(self, background='red', scrollregion=(0, 0, self.winfo_width(), self.total_height))
        self.canvas.pack(expand=True, fill='both')

        # widget frame / display frame
        self.frame = ttk.Frame(self.canvas)

    def generate_tasks(self):
        for task in enumerate(self.tasks):
            self.create_tasks(task).pack(expand=True, fill='both', pady=4, padx=10)

    def create_tasks(self, task):
        frame = ttk.Frame(self.frame)

        # Grid layout
        frame.rowconfigure(0, weight=1)
        frame.columnconfigure((0, 1, 2, 3, 4), weight=1, uniform='a')

        # widgets
        ttk.Label(frame, text=f'{task[1][0]}').grid(row=0, column=0, columnspan=5, sticky='w')
        ttk.Button(frame, text='Delete', command=lambda: self.delete_task(task[0], todoList)).grid(row=0, column=5, columnspan=2, sticky='nsew')

        return frame
    
    def update_tasks(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

        self.tasks = getTodoList()
        self.task_number = len(self.tasks)
        self.total_height = self.task_number * self.item_height
        print(self.tasks, self.task_number, self.total_height)

        self.generate_tasks()
        self.canvas.configure(scrollregion=(0, 0, self.winfo_width(), self.total_height))

    
    def update_size(self, e):
        if self.total_height >= self.winfo_height():
            height = self.total_height
            self.canvas.bind_all('<MouseWheel>', lambda e: self.canvas.yview_scroll(-int(e.delta/60), 'units'))
        else:
            # height = self.winfo_height()
            height = self.total_height
            self.canvas.unbind_all('<MouseWheel>')
        self.canvas.create_window(
            (0,0),
            window=self.frame,
            anchor='nw',
            width=self.winfo_width(),
            height=height
        )
    
    def add_new_task(self, entry_str, todoList):
        addTask(entry_str, todoList) 
        self.update_tasks()

    def delete_task(self, index, todoList):
        deleteTask(index, todoList)
        self.update_tasks()


def create_list_frame(parent, todo_list, item_height):
    return ListFrame(parent, todo_list, item_height)

# initialize todoList
todoList = getTodoList()

# Create the main window
window = ttk.Window()
window.title('Todo List')
window.geometry('600x400')

create_list_frame(window, todoList, 50)

window.mainloop()