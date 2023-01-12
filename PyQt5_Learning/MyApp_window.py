import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow,QLineEdit, QWidget,QLayout,QHBoxLayout,QComboBox
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()

        self.setWindowTitle("My Awesome App")

        widget = QComboBox()
        widget.addItems(["Jack","Sam","Fake-Sam","Jacob"])

        

        self.setCentralWidget(widget)

app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec_()