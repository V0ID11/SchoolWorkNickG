import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        x = "Feet"
        to = "Metres"
        self.setWindowTitle("Conversion Tool")
        main_layout = QVBoxLayout()
        # selection = QComboBox()
        # selection.addItems(["Feet-Metres","Metres-Feet"])
        # selection.currentIndexChanged

        layout = QFormLayout()
        self.data = QLineEdit("0.0")
        self.data.textEdited.connect(self.updateFeet)
        layout.addRow(x, self.data)
        self.output = QLineEdit("0.0")
        self.output.textEdited.connect(self.updateMetre)
        layout.addRow(to, self.output)
        main_layout.addLayout(layout)

        widget = QWidget()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)   

    def updateFeet(self,text):
        try:
            self.output.setText(f"{round(float(text)/3.28084,3)}")
        except:
            self.output.setText("0.0")

    def updateMetre(self,text):
        try:
            self.data.setText(f"{round(float(text)*3.28084,3)}")
        except:
            self.data.setText("0.0")



app = QApplication(sys.argv)

window = MainWindow()
window.show()
sys.exit(app.exec())