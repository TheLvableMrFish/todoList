from store import write_to_excel

todoList = [
    ["task 1", "complete", "yesterday", "today"],
    ["task 2", "complete", "yesterday", "today"],
    ["task 3", "complete", "yesterday", "today"],
    ["task 4", "complete", "yesterday", "today"],
]

def addTask(task):
    todoList.append(task)

def deleteTask(taskIndex):
    del todoList[taskIndex]

write_to_excel(todoList)
print('works')