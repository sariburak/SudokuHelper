from pathlib import Path
import pickle

home = str(Path.home())
default_path = home + "/.sudoku/save"

# check if save file exists
def save_exists(file_path=default_path):
    return Path(file_path).is_file()

# create save file if it doesn't exist recursively
def create_save_file(file_path=default_path):
    if not save_exists(file_path):
        Path(file_path).parent.mkdir(parents=True, exist_ok=True)
        Path(file_path).touch()

# save sudoku to file as pickle
def save_sudoku(sudoku, file_path=default_path):
    create_save_file(file_path)
    with open(file_path, "wb") as f:
        pickle.dump(sudoku, f)

# load sudoku from file
def load_sudoku(file_path=default_path):
    if save_exists(file_path):
        with open(file_path, "rb") as f:
            return pickle.load(f)
    else:
        return None