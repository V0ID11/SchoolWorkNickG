import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        main_layout = QGridLayout()

        main_layout.addWidget(QLineEdit(),0,0)
        menubar = self.menuBar()
        file_menu = menubar.addMenu("File")

        open_action = QAction('Open',self)
        open_action.setShortcut('Ctrl+O')
        open_action.triggered.connect(self.open_text)

        file_menu.addAction(open_action)

        exit_action = QAction('Exit', self)
        exit_action.setShortcut(QKeySequence('Ctrl+S'))
        exit_action.triggered.connect(self.close)
        
        file_menu.addSeparator()
        file_menu.addAction(exit_action)

        edit_menu = menubar.addMenu("Edit")
        edit_menu.addAction("Copy", self.open_text)

        widget = QWidget()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)   

    def open_text(self):
        pass

    

app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
