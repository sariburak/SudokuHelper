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

def solveForOneDigit(grid):
    for i in range(0,9):
        for j in range(0, 9):
            # print("({},{}) is {}".format(i, j, grid[i][j]))
            if grid[i][j] == 0:
                for digit in range(1,10):
                    if(checkIfPossible(grid, digit, i, j)):
                        print("{} possible at ({},{})".format(digit, i, j)) 

solveForOneDigit(exampleGrid)

    