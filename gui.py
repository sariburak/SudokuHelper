import sys

import solver
import gridsamples

from PyQt6.QtGui import QContextMenuEvent, QAction, QFocusEvent, QValidator, QRegularExpressionValidator
from PyQt6.QtCore import QSize, Qt, QRegularExpression
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout,QHBoxLayout, QLineEdit, QLabel, QWidget, QMenu, QGridLayout

def findColors(old, new):
    colors = []
    for i in range(9):
        tmp = []
        for j in range(9):
            if old[i][j] != new [i][j]:
                tmp.append("green")
            else:
                tmp.append("")
        colors.append(tmp)
    return colors

class StyleSheet():
    def background(self, color):
        if color is None:
            return "" # If color is not given, return default color
        return "background-color: {}".format(color)

#A cell is an input field dedicted to show the user only one sudoku digit field
#A cell can contain only one character as an input
#This input is restricted to be between 1-9
class CellGUI(QLineEdit):
    def __init__(self, content=""):
        super().__init__()

        validator = QRegularExpressionValidator(QRegularExpression("^[1-9]$"))
        self.setValidator(validator)
    def __str__(self) -> str:
        return self.text()

class SudokuBoardGUI(QWidget):
    def __init__(self):
        super().__init__()
        """
        Layout of this widget:
        ----------------------------------
        |                   |            |
        |                   |            |
        |                   |Vertical    |
        | Grid Box layout   |Layout      |
        |                   |For         |
        |                   |Other stuff |
        ---------------------------------
        """
        self.styleSheetGenerator = StyleSheet()
        # Initialize and fill grid layout
        self.gridLayout = QGridLayout()
        self.sudokuGrid = []
        for i in range(9):
            self.sudokuGrid.append([])
            for j in range(9):
                cell = CellGUI()
                self.sudokuGrid[i].append(cell)
                self.gridLayout.addWidget(cell, i, j)

        # Initialize and fill vertical layout
        pushy_button = QPushButton("Fill Blanks")
        pushy_button.clicked.connect(self.fill_blanks)
        solve_button = QPushButton("Solve")
        solve_button.clicked.connect(self.solve)
        step1_button = QPushButton("Step 1")
        step1_button.clicked.connect(self.step_1)
        step2_button = QPushButton("Step 2")
        step2_button.clicked.connect(self.step_2)

        right_sidebar = QVBoxLayout()
        right_sidebar.addWidget(pushy_button)
        right_sidebar.addWidget(step1_button)
        right_sidebar.addWidget(step2_button)
        right_sidebar.addWidget(solve_button)


        # Outermost layout
        self.layout = QHBoxLayout()
        self.layout.addLayout(self.gridLayout)
        self.layout.addLayout(right_sidebar)

        # TODO: Do we really need to keep this widget?
        self.widget = QWidget()
        self.setLayout(self.layout)

    def step_1(self):
        print("Step 1 button is clicked")
        grid = self.exportGrid()
        solution = solver.solveForOneCellWithOneDigit(grid)
        colors = findColors(grid, solution)
        self.importGrid(solution, colors)

    def step_2(self):
        print("Step 2 button is clicked")
        grid = self.exportGrid()
        solution = solver.solveOneDigit(grid)
        colors = findColors(grid, solution)
        self.importGrid(solution, colors)

    def fill_blanks(self):
        print("Fill Blanks button is clicked")
        self.importGrid(gridsamples.easySudoku)

    def solve(self):
        print("Solve button is clicked")
        grid = self.exportGrid()
        solutions = solver.solveSudoku(grid)
        if len(solutions) != 0:
            colors = findColors(grid, solutions[0])
            self.importGrid(solutions[0], colors)
        else:
            print("No solution!")

    def exportGrid(self):
        grid = []
        for row in self.sudokuGrid:
            tmp = []
            for cell in row:
                text = cell.text()
                if text == '':
                    tmp.append(0)
                else:
                    tmp.append(int(cell.text()))
            grid.append(tmp)
        return grid


    def importGrid(self, sudokuGrid, colors=None):
        # Check if valid sudoku grid
        if len(sudokuGrid) != 9:
            raise Exception("given sudoku grid does not have 9 rows, given grid: {}".format(sudokuGrid))
        if len(sudokuGrid[0]) != 9:
            raise Exception("given sudoku grid does not have 9 cols, given grid: {}".format(sudokuGrid))

        for rowC, row in enumerate(sudokuGrid):
            for colC, number in enumerate(row):
                cell = self.sudokuGrid[rowC][colC]
                cell.setText(str(number))

        self.importColors(colors)

    def importColors(self, colors):
        for i in range(9):
            for j in range(9):
                backgroundColor = "" if colors is None else colors[i][j]
                self.sudokuGrid[i][j].setStyleSheet(self.styleSheetGenerator.background(backgroundColor))

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        widget = SudokuBoardGUI()

        # widget.setMaxLength(1)
        self.setCentralWidget(widget)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()