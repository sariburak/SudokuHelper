import copy

exampleGrid = [
    [5, 0, 0, 6, 1, 9, 0, 3, 0],
    [0, 3, 0, 4, 8, 2, 1, 0, 0],
    [0, 0, 0, 7, 3, 5, 0, 4, 0],
    [0, 2, 0, 0, 7, 0, 0, 0, 0],
    [0, 0, 0, 0, 5, 0, 6, 0, 0],
    [8, 0, 0, 2, 9, 6, 0, 0, 4],
    [0, 0, 9, 5, 4, 7, 0, 0, 8],
    [0, 5, 8, 3, 2, 1, 4, 0, 0],
    [0, 0, 0, 9, 6, 8, 0, 0, 0]
]

exampleGrid2 = [
    [5, 8, 2, 6, 1, 9, 0, 3, 4],
    [0, 3, 0, 4, 8, 2, 1, 0, 0],
    [0, 0, 0, 7, 3, 5, 0, 4, 0],
    [0, 2, 0, 0, 7, 0, 0, 0, 0],
    [0, 0, 0, 0, 5, 0, 6, 0, 0],
    [8, 0, 0, 2, 9, 6, 0, 0, 4],
    [0, 0, 9, 5, 4, 7, 0, 0, 8],
    [0, 5, 8, 3, 2, 1, 4, 0, 0],
    [0, 0, 0, 9, 6, 8, 0, 0, 0]
]

gridFirstRowMissingFive = [
    [1, 2, 0, 4, 0, 6, 7, 0, 9],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 5, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 5, 0, 0, 0, 0, 0, 0]
]

gridFirstColumnMissingFive = [
    [1, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 5, 0, 0, 0, 0],
    [4, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [6, 0, 0, 0, 0, 0, 0, 0, 0],
    [7, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 5, 0],
    [9, 0, 0, 0, 0, 0, 0, 0, 0]
]

gridFirst3x3MissingFive = [
    [1, 0, 0, 0, 0, 0, 0, 0, 0],
    [4, 2, 6, 0, 0, 0, 0, 0, 0],
    [7, 0, 9, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 5, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

exampleColors = [
    ["red" for _ in range(9)],
    ["blue" for _ in range(9)],
    ["green" for _ in range(9)],
    ["" for _ in range(9)],
    ["" for _ in range(9)],
    ["" for _ in range(9)],
    ["" for _ in range(9)],
    ["" for _ in range(9)],
    ["" for _ in range(9)]
]

# Checks if the given number is suitable for point (i, j)
def checkIfPossible(grid, number, i, j):
    if number in grid[i]:
        return False

    for row in grid:
        if row[j] == number:
            return False

    rowStart = i // 3 * 3
    columnStart = j // 3 *3

    for x in range(rowStart, rowStart+3):
        for y in range(columnStart, columnStart+3):
            if grid[x][y] == number:
                return False

    return True

# findPossibleDigitsForCells return a map of (int, int) -> [int].
# The key of this map is the index on the grid
# The value of this map is the list of possible digits that can be placed in that cell
def findPossibleDigitsForCells(grid):
    possibleDigits = {}
    for i in range(0,9):
        for j in range(0, 9):
            if grid[i][j] == 0:
                for digit in range(1,10):
                    if(checkIfPossible(grid, digit, i, j)):
                        if (i,j) in possibleDigits.keys():
                            possibleDigits[(i, j)].append(digit)
                        else:
                            possibleDigits[(i, j)] = [digit]
    return possibleDigits

def solveSudoku(grid):
    solutions = []
    solveSudokuHelper(grid, solutions)
    return solutions

def solveSudokuHelper(grid, solutions):
    for i in range(0, 9):
        for j in range(0, 9):
            if grid[i][j] == 0:
                # Put any of the [0,9] and see that solves the sudoku
                # If solves, done
                # If does not solve, put back 0 to the index and try another number
                for possible in range(1,10):
                    if checkIfPossible(grid, possible ,i, j):
                        grid[i][j] = possible
                        solveSudokuHelper(grid, solutions)
                        grid[i][j] = 0
                return

    solutions.append(copy.deepcopy(grid))

# This function is not used in the final solution
# It is used to check if the sudoku is solved
def isSolved(grid):
    for i in range(0, 9):
        for j in range(0, 9):
            if grid[i][j] == 0:
                return False
    return True

def step1(grid):
    """
    Checks if there is a cell that can only have one digit
    """
    possibleDigits = findPossibleDigitsForCells(grid)
    for key, value in possibleDigits.items():
        if len(value) == 1:
            grid[key[0]][key[1]] = value[0]
    return grid

def step2(grid):
    """
    Checks if there is a digit that can only be placed in one cell in a row
    """
    possibleDigits = findPossibleDigitsForCells(grid)
    for i in range(0, 9):
        for digit in range(1, 10):
            count = 0
            for j in range(0, 9):
                if (i, j) in possibleDigits.keys() and digit in possibleDigits[(i, j)]:
                    count += 1
                    index = (i, j)
            if count == 1:
                grid[index[0]][index[1]] = digit
    return grid

def step3(grid):
    """
    Checks if there is a digit that can only be placed in one cell in a column
    """
    possibleDigits = findPossibleDigitsForCells(grid)
    for j in range(0, 9):
        for digit in range(1, 10):
            count = 0
            for i in range(0, 9):
                if (i, j) in possibleDigits.keys() and digit in possibleDigits[(i, j)]:
                    count += 1
                    index = (i, j)
            if count == 1:
                grid[index[0]][index[1]] = digit
    return grid

def step4(grid):
    """
    Checks if there is a digit that can only be placed in one cell in a 3x3 grid
    """
    possibleDigits = findPossibleDigitsForCells(grid)
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            for digit in range(1, 10):
                count = 0
                for x in range(i, i+3):
                    for y in range(j, j+3):
                        if (x, y) in possibleDigits.keys() and digit in possibleDigits[(x, y)]:
                            count += 1
                            index = (x, y)
                if count == 1:
                    grid[index[0]][index[1]] = digit
    return grid
