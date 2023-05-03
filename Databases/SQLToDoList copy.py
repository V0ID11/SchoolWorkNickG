import sqlite3
import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

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



class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setWindowTitle("ToDo")

        main_layout = QGridLayout()

        add_action = QPushButton("Add Item")
        add_action.clicked.connect(self.add_item)
        main_layout.addWidget(add_action,0,0)

        view_action = QPushButton("View Table")
        view_action.clicked.connect(self.ViewTable)
        main_layout.addWidget(view_action,1,0)

        widget = QWidget()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)
    
    def AddItem(self,):
        tasks = sqlite3.connect('ToDo.db')
        insert = """
        INSERT INTO tasks (name,priority,status_id)
        VALUES (?,?,0)"""
        tasks.execute(insert, (self.description.displayText(),self.priority.currentText()))
        tasks.commit()
        tasks.close()
        self.main()

    def ViewTable(self):
        
        view_layout = QGridLayout()
        tasks = sqlite3.connect('ToDo.db')
        query = """SELECT name From tasks WHERE status_id != TRUE ORDER BY priority ASC"""
        cursor = tasks.execute(query)
        
        for i,desc in enumerate(cursor):
            display = QLabel(f"{i+1}.")
            item = QLabel(desc[0])
            view_layout.addWidget(display,i,0)
            view_layout.addWidget(item,i,1)
            final_value = i
        
        tasks.close()

        ok_btn = QPushButton("Ok")
        ok_btn.clicked.connect(self.main)
        view_layout.addWidget(ok_btn,final_value+1,0,1,2)

        widget = QWidget()
        widget.setLayout(view_layout)
        self.setCentralWidget(widget)

    def completeTask(self,num):
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
        
    
    def main(self):
        main_layout = QGridLayout()

        add_action = QPushButton("Add Item")
        add_action.clicked.connect(self.add_item)
        main_layout.addWidget(add_action,0,0)

        view_action = QPushButton("View Table")
        view_action.clicked.connect(self.ViewTable)
        main_layout.addWidget(view_action,1,0)


        widget = QWidget()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)
        
    def add_item(self):
        add_layout = QGridLayout()
        self.description = QLineEdit()
        self.priority = QComboBox()
        self.priority.addItems(["1","2","3"])
        ok_btn = QPushButton("Ok")
        ok_btn.clicked.connect(self.AddItem)
        add_layout.addWidget(self.description,0,0,1,2)
        add_layout.addWidget(self.priority,0,3)
        add_layout.addWidget(ok_btn,2,0,1,3)
        
        widget = QWidget()
        widget.setLayout(add_layout)
        self.setCentralWidget(widget)

    

        

app = QApplication(sys.argv)

window = MainWindow()
window.show()
sys.exit(app.exec())
