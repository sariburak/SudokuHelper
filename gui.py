import sys
from tabnanny import check

from PyQt6.QtGui import QContextMenuEvent, QAction, QFocusEvent, QValidator
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QLineEdit, QLabel, QWidget, QMenu, QGridLayout



#A cell is an input field dedicted to show the user only one sudoku digit field
#A cell can contain only one character as an input
#This input is restricted to be between 1-9
class CellGUI(QLineEdit):
    def __init__(self):
        super().__init__()

        #Input can only be lenght of 1
        # self.setMaxLength(1)

        #Input can only be characters of 1-9
        self.setInputMask("D")



    def focusInEvent(self, a0: QFocusEvent) -> None:

        if a0 == Qt.FocusReason.MouseFocusReason:
            self.setText("")
            
        return super().focusInEvent(a0)

class SudokuBoardGUI(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QGridLayout()

        for i in range(9):
            for j in range(9):
                self.addWidget(CellGUI(), i, j)


        #TODO: Do we really need to keep this widget?
        self.widget = QWidget()

        self.setLayout(self.layout)
    

    def addWidget(self, widget, row, col):
        self.layout.addWidget(widget, row, col)





class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        widget = CellGUI()

        # widget.setMaxLength(1)
        self.setCentralWidget(widget)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()