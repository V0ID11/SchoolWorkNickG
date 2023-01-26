import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setWindowTitle("Text Editor")
        self.setWindowIcon(QIcon('download.png'))
        
        #Menu
        menuBar = self.menuBar()
        file_menu = menuBar.addMenu("File")

        open_action = QAction('Open', self)
        open_action.setShortcut('Ctrl+O')
        open_action.triggered.connect(self.open_text)

        save_action = QAction('Save', self)
        save_action.setShortcut('Ctrl+S')
        save_action.triggered.connect(self.save_text)

        save_as_action = QAction('Save As', self)
        save_as_action.setShortcut('Ctrl+Shift+S')
        save_as_action.triggered.connect(self.save_as_text)

        exit_Action = QAction('Exit', self)
        exit_Action.setShortcut('Ctrl+Shift+Q')
        exit_Action.triggered.connect(self.quit)

        file_menu.addAction(open_action)
        file_menu.addAction(save_action)
        file_menu.addAction(save_as_action)
        file_menu.addAction(exit_Action)

        #layout
        main_layout = QGridLayout()
        self.text_edit = QTextEdit()
        main_layout.addWidget(self.text_edit,0,0,3,3)
        widget = QWidget()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)   

    def open_text(self):
        filename, _ = QFileDialog.getOpenFileName(self,"Open File", ".", "All Files (*.*)")
        self.file = filename
        try:
            with open(filename,"r") as file:
                text = file.readlines()
                x = ""
                for i in text:
                    x += i
                self.text_edit.setPlainText(x)
        except:
            pass

    def save_text(self):
        try:
            try:
                with open(self.file,"w") as file:
                    file.writelines(self.text_edit.toPlainText())
            except:
                self.save_as_text()
        except:
            pass

    def save_as_text(self):
        try:
            filename,_ = QFileDialog.getSaveFileName(self, "Save File", ".", "All Files (*.*)")
            self.file = filename
            with open(self.file,"w") as file:
                file.writelines(self.text_edit.toPlainText())
        except:
            pass

    def quit(self):
        dlg = QMessageBox.warning(self, "Exit", "You Will Lose Unsaved Data", QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Save | QMessageBox.StandardButton.Cancel)
        if dlg == QMessageBox.StandardButton.Ok:
            self.close()
        elif dlg == QMessageBox.StandardButton.Save:
            self.save_text()
            self.close()
    
app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()