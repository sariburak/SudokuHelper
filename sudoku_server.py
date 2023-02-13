import requests

url = "https://sudoku-generator1.p.rapidapi.com/sudoku/generate"
headers = {
    'X-RapidAPI-Key': 'f852b7bb72msh6e89f14fe4a0ecfp1a39bbjsn9c2f7273854c',
    'X-RapidAPI-Host': 'sudoku-generator1.p.rapidapi.com'
}
params = {
    'seed': '1337',
    'difficulty': 'easy',
}

#Example response
# {
#   "seed": 1337,
#   "difficulty": "Easy",
#   "puzzle": "..3465..2.862..7..92...7.1.6....234..15....69.42..8.......364717..5.49.3..987.5.."
# }

# Generate a sudoku puzzle
# difficulty: easy, medium, hard
def generateSudoku(difficulty = None):
    if difficulty:
        params['difficulty'] = difficulty
    response = requests.request("GET", url, headers=headers, params=params)
    puzzle = response.json()['puzzle']
    # Convert puzzle into 2D array
    grid = []
    for i in range(9):
        grid.append([])
        for j in range(9):
            index = i*9+j
            if puzzle[index] == '.':
                grid[i].append(0)
            else:
                grid[i].append(int(puzzle[i*9+j]))
    return grid

