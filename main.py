# import os

from datetime import datetime

from store import write_to_excel
from getList import getTodoList

# if os.path.exists("tasks.xlsx"):
    
todoList = getTodoList()

# todoList = [
#     ["task 1", "complete", "yesterday", "today"],
#     ["task 2", "complete", "yesterday", "today"],
#     ["task 3", "complete", "yesterday", "today"],
#     ["task 4", "complete", "yesterday", "today"],
# ]

def addTask(task):
    
    todoList.append(
        [
            task,
            "incomplete",
            f"{datetime.now()}",
            "N/A"
        ]
    )

    write_to_excel(todoList)

addTask("Clean")

def deleteTask(taskIndex):
    del todoList[taskIndex]

# write_to_excel(todoList)
# print('works')