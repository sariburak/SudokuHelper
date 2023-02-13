import requests

# curl 'https://sudoku.com/api/level/medium' \
#   -H 'x-requested-with: XMLHttpRequest'

# Example response:
# {
#   "id": 1318,
#   "mission": "002300405080029700004560000500980070040050030800000000406000100010005090703100204",
#   "solution": "962378415185429763374561928531984672649257831827613549496832157218745396753196284",
#   "win_rate": 59.35
# }

# level: easy, medium, hard, expert, evil
url = "https://sudoku.com/api/level/{level}"
headers = {
   "x-requested-with": "XMLHttpRequest"
}

def get_sudoku(level):
    r = requests.get(url.format(level=level), headers=headers)
    sudoku = r.json().get("mission")
    grid = []
    for i in range(9):
        grid.append([int(sudoku[i*9+j]) for j in range(9)])
    return grid