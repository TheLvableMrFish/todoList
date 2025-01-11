from datetime import datetime

from store import write_to_excel

# Adds a task todoList and then writes it all to excel
def addTask(task, todoList):
    
    if(task != ""):
        todoList.append(
            [
                task,
                "incomplete",
                f"{datetime.now()}",
                "N/A"
            ]
        )

        write_to_excel(todoList)

def deleteTask(taskIndex, todoList):
    del todoList[taskIndex]
    write_to_excel(todoList)
