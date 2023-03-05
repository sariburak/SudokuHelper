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

easySudoku = [
    [0, 5, 0, 0, 0, 0, 0, 0, 4],
    [9, 0, 0, 4, 3, 0, 0, 0, 0],
    [0, 0, 0, 2, 0, 9, 3, 8, 0],
    [0, 9, 0, 0, 7, 0, 4, 5, 0],
    [3, 0, 0, 0, 0, 2, 0, 0, 0],
    [8, 7, 0, 0, 0, 0, 0, 1, 3],
    [5, 0, 1, 0, 0, 8, 0, 0, 0],
    [7, 0, 9, 3, 1, 0, 5, 6, 8],
    [6, 0, 4, 7, 2, 5, 0, 3, 9]
]

raySudoku = [
    [1, 2, 3, 0, 0, 0, 0, 0, 0],
    [0, 4, 0, 0, 0, 0, 0, 0, 0],
    [6, 7, 8, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
]

squareExample = [
    [9, 0, 0, 0, 2, 7, 0, 5, 0],
    [0, 5, 0, 0, 0, 0, 9, 0, 4],
    [0, 0, 0, 5, 0, 4, 0, 0, 0],
    [8, 0, 0, 0, 7, 5, 6, 4, 9],
    [1, 0, 0, 0, 4, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 9, 8, 0, 1],
    [0, 0, 0, 4, 5, 1, 0, 0, 0],
    [0, 0, 0, 7, 3, 0, 0, 1, 0],
    [5, 0, 1, 0, 0, 2, 0, 3, 7]
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

def calculateGridIndex(x, y):
    return (x // 3) * 3 + y // 3

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
def findPossibleDigitsForCells(grid, *opts):
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
    for opt in opts:
        opt(possibleDigits)

    return possibleDigits


def groupPossibleDigitsBasedOn3x3(possibleDigits):
    occurrences = {}
    for key, value in possibleDigits.items():
        gridKey = (key[0] // 3 )* 3 + key[1] // 3
        if gridKey not in occurrences:
            occurrences[gridKey] = {}

        for digit in value:
            if digit not in occurrences[gridKey]:
                occurrences[gridKey][digit] = []
            occurrences[gridKey][digit].append(key)
    return occurrences

def isSameRow(coordinates):
    if len(coordinates) == 0:
        return True

    row = coordinates[0][0]

    for coordinate in coordinates:
        if row != coordinate[0]:
            return False

    return True

def isSameColumn(coordinates):
    if len(coordinates) == 0:
        return True

    column = coordinates[0][1]

    for coordinate in coordinates:
        if column != coordinate[1]:
            return False

    return True

# TODO: I feel like there should be a way to refactor shootRayRow and shootRayColumn. They are almost identical
def shootRayRow(possibleDigits, digit, rowIndex, rayOrigin, exemptedGrids = []):
    for coordinate, digits in possibleDigits.items():
        if coordinate[0] == rowIndex and digit in digits: # if there is target digit in the target row
            targetGridIndex = (coordinate[0] // 3 ) * 3 + coordinate[1] // 3
            if targetGridIndex == rayOrigin: # skip if in the same 3x3
                continue
            # TODO: Embed rayOrigin into exemptedGrids
            if targetGridIndex in exemptedGrids:
                continue
            digits.remove(digit)

def shootRayColumn(possibleDigits, digit, columnIndex, rayOrigin):
    for coordinate, digits in possibleDigits.items():
        if coordinate[1] == columnIndex and digit in digits: # if there is target digit in the target row
            targetGridIndex = (coordinate[0] // 3 )* 3 + coordinate[1] // 3
            if targetGridIndex == rayOrigin: # skip if in the same 3x3
                continue
            digits.remove(digits)

def eliminateDigitsWithRay(possibleDigits):
    possibleDigitsOn3x3 = groupPossibleDigitsBasedOn3x3(possibleDigits)
    for gridIndex in possibleDigitsOn3x3:
        grid = possibleDigitsOn3x3[gridIndex]
        for digit, coordinates in grid.items():
            if len(coordinates) != 2:
                continue
            if isSameRow(coordinates):
                shootRayRow(possibleDigits, digit, coordinates[0][0], gridIndex)
            if isSameColumn(coordinates):
                shootRayColumn(possibleDigits, digit, coordinates[0][1], gridIndex)

def repeatingRows(coordinates):
    rows = set()
    for coordinate in coordinates:
        rows.add(coordinate[0])
    return list(rows)

def findOpposingSquareEdge(possibleDigitsOn3x3, originGrid, targetRows, targetNumber):
    start = (originGrid // 3) * 3
    targetGrids = [i for i in range(start, start + 3) if i != originGrid]
    res = []
    for targetGrid in targetGrids:
        grid = possibleDigitsOn3x3[targetGrid]
        if targetNumber in grid:
            coordinates = grid[targetNumber]
            if repeatingRows(coordinates) == targetRows:
                res.append(targetGrid)
    return res

def eliminateDigitsWithSquare(possibleDigits):
    possibleDigitsOn3x3 = groupPossibleDigitsBasedOn3x3(possibleDigits)
    for gridIndex, grid in possibleDigitsOn3x3.items():
        for number, coordinates in grid.items():
            rows = repeatingRows(coordinates)
            if len(rows) == 2:
                edgeGrids = findOpposingSquareEdge(possibleDigitsOn3x3, gridIndex, rows, number)
                pass
                for edgeGrid in edgeGrids:
                    shootRayRow(possibleDigits, number, rows[0], gridIndex, [edgeGrid])
                    shootRayRow(possibleDigits, number, rows[1], gridIndex, [edgeGrid])
                # targetGrids = [i for i in range(start, start + 3) if i != gridIndex and i not in edgeGrids]
                # for targetGrid in targetGrids:
                #     shootRayRow(possibleDigits, number, rows[0], grid, [targetGrid])
                #     shootRayRow(possibleDigits, number, rows[1], grid, [targetGrid])

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

def solveForOneCellWithOneDigit(grid, possibleDigits):
    """
    Checks if there is a cell that can only have one digit
    """
    # This is needed to avoid changing the original grid
    grid = copy.deepcopy(grid)
    for key, value in possibleDigits.items():
        if len(value) == 1:
            grid[key[0]][key[1]] = value[0]
    return grid

def solveOneDigitInARow(grid, possibleDigits):
    """
    Checks if there is a digit that can only be placed in one cell in a row
    """
    # This is needed to avoid changing the original grid
    grid = copy.deepcopy(grid)
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

def solveOneDigitInAColumn(grid, possibleDigits):
    """
    Checks if there is a digit that can only be placed in one cell in a column
    """
    # This is needed to avoid changing the original grid
    grid = copy.deepcopy(grid)
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

def solveOneDigitIn3x3(grid, possibleDigits):
    """
    Checks if there is a digit that can only be placed in one cell in a 3x3 grid
    """
    # This is needed to avoid changing the original grid
    grid = copy.deepcopy(grid)
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

def solveOneDigit(grid, possibleDigits):
    """
    Finds all the cells that can only have one digit and fills them
    """
    # This is needed to avoid changing the original grid
    result = copy.deepcopy(grid)
    # The results from different strategies are merged
    # It is important that the result of one strategy is NOT fed to the next strategy
    # This is because the strategies should be independent of each other.
    # This requirement may change later on
    result = mergeTwoGrids(result, solveForOneCellWithOneDigit(grid, possibleDigits))
    result = mergeTwoGrids(result, solveOneDigitInARow(grid, possibleDigits))
    result = mergeTwoGrids(result, solveOneDigitInAColumn(grid, possibleDigits))
    result = mergeTwoGrids(result, solveOneDigitIn3x3(grid, possibleDigits))
    return result

# This function is used to merge two grids
# If the two grids have the same value in the same cell, the value is kept
# If the two grids have different values in the same cell, error is raised
# If the cell from one grid is empty, the value from the other grid is kept
def mergeTwoGrids(grid1, grid2):
    grid = copy.deepcopy(grid1)
    for i in range(0, 9):
        for j in range(0, 9):
            if grid1[i][j] != grid2[i][j]:
                if grid1[i][j] == 0:
                    grid[i][j] = grid2[i][j]
                elif grid2[i][j] == 0:
                    grid[i][j] = grid1[i][j]
                else:
                    raise Exception("Two grids have different values in the same cell")
    return grid