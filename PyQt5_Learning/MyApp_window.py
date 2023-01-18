import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setWindowTitle("Form And Grid Layout")
        self.setFixedWidth(500)
        self.setFixedHeight(225)
        self.count = 0
        self.mainWindow()

    def mainWindow(self):
                main_layout = QGridLayout()
                
                form = QFormLayout()
                self.name_Edit = QLineEdit()
                self.name_Edit.textChanged.connect(self.on_text_changed)
                self.name_Edit.setPlaceholderText("Enter Name")
                form.addRow("Name:",self.name_Edit)
                self.location_Edit = QLineEdit()
                self.location_Edit.setPlaceholderText("Enter Location")
                form.addRow("Location:",self.location_Edit)
                main_layout.addLayout(form,0,0,1,3)

                combo = QComboBox()
                combo.addItems(["1","2","3","4"])
                main_layout.addWidget(combo,1,0,1,2)

                ok_btn = QPushButton("Ok")
                ok_btn.clicked.connect(self.displayDetails)
                self.clicker = QCheckBox("Click Me")
                main_layout.addWidget(self.clicker,1,2,1,1)
                main_layout.addWidget(ok_btn,2,1,1,1)

                self.cancel_btn = QPushButton("Cancel")
                self.cancel_btn.clicked.connect(self.close)
                main_layout.addWidget(self.cancel_btn,2,2,1,1)


                widget = QWidget()
                widget.setLayout(main_layout)
                self.setCentralWidget(widget)
    def displayDetails(self):
        if self.clicker.isChecked():
            layout = QGridLayout()
            layout.addWidget(QLabel(f"Name: {self.name_Edit.displayText()}"),0,0,1,3)
            layout.addWidget(QLabel(f"Location: {self.location_Edit.displayText()}"),1,0,1,3)
            self.cancel_btn.setText("Close")
            layout.addWidget(self.cancel_btn,2,1,1,1)
        else:
            layout = QVBoxLayout()
            layout.addWidget(QLabel("Must Press The Button"))
            retry_btn = QPushButton("Retry")
            retry_btn.clicked.connect(self.mainWindow)
            layout.addWidget(retry_btn)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def on_text_changed(self,text):
        print(text)
   
        

app = QApplication(sys.argv)

window = MainWindow()
window.show()
sys.exit(app.exec_())