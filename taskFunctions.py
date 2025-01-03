from datetime import datetime

from store import write_to_excel

def addTask(task, todoList):
    
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

# todoList = [
#     ["task 1", "complete", "yesterday", "today"],
#     ["task 2", "complete", "yesterday", "today"],
#     ["task 3", "complete", "yesterday", "today"],
#     ["task 4", "complete", "yesterday", "today"],
# ]



# write_to_excel(todoList)
# print('works')