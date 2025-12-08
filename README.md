## Setup

```
python3 -m venv ./.venv
```

```
source /path/to/activate
```

```
pip install -r requirements.txt
```

## Run

```
python3 gui.py
```
## Thanks

This project heavily depends on what I learn from `https://www.pythonguis.com/tutorials/creating-your-first-pyqt-window/`.


[One char validator for QLineEdit](https://stackoverflow.com/questions/17908040/is-there-a-convenient-way-to-input-only-one-character-by-some-qt-widget)


## TODO
- Add unit test for column square elimination
- Solve button should check if sudoku is really solved correctly. This is important to check if separate strategies are implemented correctly.
- Create docs for every elimination method

## Bugs
- Not known any

## How to run tets

`python -m unittest solvertest.py`

