import sqlite3

tasks = sqlite3.connect('ToDo.db')

def createTable():
    tasks = sqlite3.connect('ToDo.db')
    create = """
    CREATE TABLE IF NOT EXISTS tasks (
    id integer PRIMARY KEY AUTOINCREMENT,
    name text NOT NULL,
    priority integer,
    status_id bool NOT NULL
    )"""
    tasks.execute(create)
    tasks.commit()
    tasks.close()
createTable()

def AddItem(desc,priority):
    tasks = sqlite3.connect('ToDo.db')
    insert = """
    INSERT INTO tasks (name,priority,status_id)
    VALUES (?,?,0)"""
    tasks.execute(insert, (desc,priority))
    tasks.commit()
    tasks.close()


def ViewTable():
    tasks = sqlite3.connect('ToDo.db')
    query = """SELECT name From tasks WHERE status_id != TRUE ORDER BY priority ASC"""
    cursor = tasks.execute(query)
    print("\nTo Do")
    for i,desc in enumerate(cursor):
        print(f"{i+1}. {desc[0]}")
    tasks.close()

def completeTask(num):
    tasks = sqlite3.connect('ToDo.db')
    query = """SELECT name,id From tasks where status_id != TRUE ORDER BY priority ASC"""
    cursor = tasks.execute(query)
    final = []
    for i in cursor:
        final.append(i)
    print(final)
    id = final[num-1][1]
    updateQuery = """UPDATE tasks SET status_id = TRUE WHERE id = (?)"""
    tasks.execute(updateQuery, str(id))
    tasks.commit()
    tasks.close()

def createMenu():
    while True:
        action = int(input("\n1. Add Task\n2. Complete Task\n3. View Table\n4. Quit: "))
        if action == 1:
            desc = input("What is your task: ")
            priority = input("What priority value do you want to give this: ")
            AddItem(desc, priority)
        elif action == 2:
            num = int(input("What task do you want to complete: "))
            completeTask(num)
        elif action == 3:
            ViewTable()
        else:
            quit()
createMenu()