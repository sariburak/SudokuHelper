import unittest

import solver

class TestSolverMethods(unittest.TestCase):
    def testMergeTwoGrids(self):
        tests = [
            {
                "description": "One extra digit in second grid",
                "grid1": [
                    [0, 5, 0, 0, 0, 0, 0, 0, 4],
                    [9, 0, 0, 4, 3, 0, 0, 0, 0],
                    [0, 0, 0, 2, 0, 9, 3, 8, 0],
                    [0, 9, 0, 0, 7, 0, 4, 5, 0],
                    [3, 0, 0, 0, 0, 2, 0, 0, 0],
                    [8, 7, 0, 0, 0, 0, 0, 1, 3],
                    [5, 0, 1, 0, 0, 8, 0, 0, 0],
                    [7, 0, 9, 3, 1, 0, 5, 6, 8],
                    [6, 0, 4, 7, 2, 5, 0, 3, 9]
                ],
                "grid2": [
                    [2, 5, 0, 0, 0, 0, 0, 0, 4],
                    [9, 0, 0, 4, 3, 0, 0, 0, 0],
                    [0, 0, 0, 2, 0, 9, 3, 8, 0],
                    [0, 9, 0, 0, 7, 0, 4, 5, 0],
                    [3, 0, 0, 0, 0, 2, 0, 0, 0],
                    [8, 7, 0, 0, 0, 0, 0, 1, 3],
                    [5, 0, 1, 0, 0, 8, 0, 0, 0],
                    [7, 0, 9, 3, 1, 0, 5, 6, 8],
                    [6, 0, 4, 7, 2, 5, 0, 3, 9]
                ],
                "want": [
                    [2, 5, 0, 0, 0, 0, 0, 0, 4],
                    [9, 0, 0, 4, 3, 0, 0, 0, 0],
                    [0, 0, 0, 2, 0, 9, 3, 8, 0],
                    [0, 9, 0, 0, 7, 0, 4, 5, 0],
                    [3, 0, 0, 0, 0, 2, 0, 0, 0],
                    [8, 7, 0, 0, 0, 0, 0, 1, 3],
                    [5, 0, 1, 0, 0, 8, 0, 0, 0],
                    [7, 0, 9, 3, 1, 0, 5, 6, 8],
                    [6, 0, 4, 7, 2, 5, 0, 3, 9]
                ]
            },
            {
                "description": "Extra digits in both grid",
                "grid1": [
                    [0, 5, 0, 0, 0, 0, 0, 0, 4],
                    [9, 0, 0, 4, 3, 0, 0, 0, 0],
                    [0, 0, 0, 2, 0, 9, 3, 8, 3],
                    [0, 9, 0, 0, 7, 0, 4, 5, 0],
                    [3, 0, 0, 0, 0, 2, 0, 0, 0],
                    [8, 7, 0, 0, 0, 0, 0, 1, 3],
                    [5, 0, 1, 0, 0, 8, 0, 0, 0],
                    [7, 5, 9, 3, 1, 0, 5, 6, 8],
                    [6, 0, 4, 7, 2, 5, 0, 3, 9]
                ],
                "grid2": [
                    [0, 5, 0, 0, 0, 0, 0, 0, 4],
                    [9, 0, 0, 4, 3, 0, 0, 0, 0],
                    [0, 0, 0, 2, 0, 9, 3, 8, 0],
                    [0, 9, 0, 0, 7, 0, 4, 5, 0],
                    [3, 0, 0, 0, 0, 2, 0, 0, 0],
                    [8, 7, 0, 0, 0, 0, 0, 1, 3],
                    [5, 0, 1, 0, 0, 8, 0, 0, 0],
                    [7, 0, 9, 3, 1, 0, 5, 6, 8],
                    [6, 0, 4, 7, 2, 5, 0, 3, 9]
                ],
                "want": [
                    [0, 5, 0, 0, 0, 0, 0, 0, 4],
                    [9, 0, 0, 4, 3, 0, 0, 0, 0],
                    [0, 0, 0, 2, 0, 9, 3, 8, 3],
                    [0, 9, 0, 0, 7, 0, 4, 5, 0],
                    [3, 0, 0, 0, 0, 2, 0, 0, 0],
                    [8, 7, 0, 0, 0, 0, 0, 1, 3],
                    [5, 0, 1, 0, 0, 8, 0, 0, 0],
                    [7, 5, 9, 3, 1, 0, 5, 6, 8],
                    [6, 0, 4, 7, 2, 5, 0, 3, 9]
                ]
            }
        ]

        for test in tests:
            self.assertEqual(test["want"], solver.mergeTwoGrids(test["grid1"], test["grid2"]))

    def testSolveForOnceCellWithOneDigit(self):
        tests =  [
            {
                "description": "simple example",
                "grid": [
                    [1, 2, 3, 4, 5, 6, 7, 8, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                ],
                "want": [
                    [1, 2, 3, 4, 5, 6, 7, 8, 9],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                ]
            },
            {
                "description": "complex example",
                "grid": [
                    [0, 5, 0, 0, 0, 0, 0, 0, 4],
                    [9, 0, 0, 4, 3, 0, 0, 0, 0],
                    [0, 0, 0, 2, 0, 9, 3, 8, 0],
                    [0, 9, 0, 0, 7, 0, 4, 5, 0],
                    [3, 0, 0, 0, 0, 2, 0, 0, 0],
                    [8, 7, 0, 0, 0, 0, 0, 1, 3],
                    [5, 0, 1, 0, 0, 8, 0, 0, 0],
                    [7, 0, 9, 3, 1, 0, 5, 6, 8],
                    [6, 0, 4, 7, 2, 5, 0, 3, 9]
                ],
                "want": [
                    [0, 5, 0, 0, 0, 0, 0, 0, 4],
                    [9, 0, 0, 4, 3, 0, 0, 0, 0],
                    [0, 0, 0, 2, 0, 9, 3, 8, 0],
                    [0, 9, 0, 0, 7, 0, 4, 5, 0],
                    [3, 0, 0, 0, 0, 2, 0, 0, 0],
                    [8, 7, 0, 0, 0, 0, 0, 1, 3],
                    [5, 0, 1, 0, 0, 8, 0, 0, 0],
                    [7, 2, 9, 3, 1, 4, 5, 6, 8],
                    [6, 8, 4, 7, 2, 5, 1, 3, 9]
                ]
            }
        ]

        for test in tests:
            possible = solver.findPossibleDigitsForCells(test["grid"])
            self.assertEqual(test["want"], solver.solveForOneCellWithOneDigit(test["grid"], possible))

    def testSolveOneDigitInARow(self):
        tests = [
            {
                "describe": "simple example",
                "grid": [
                    [1, 0, 3, 4, 0, 6, 7, 0, 9],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 5, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 5, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                ],
                "want": [
                    [1, 0, 3, 4, 5, 6, 7, 0, 9],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 5, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 5, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                ]
            },
            {
                "describe": "complex example",
                "grid": [
                    [0, 5, 0, 0, 0, 0, 0, 0, 4],
                    [9, 0, 0, 4, 3, 0, 0, 0, 0],
                    [0, 0, 0, 2, 0, 9, 3, 8, 0],
                    [0, 9, 0, 0, 7, 0, 4, 5, 0],
                    [3, 0, 0, 0, 0, 2, 0, 0, 0],
                    [8, 7, 0, 0, 0, 0, 0, 1, 3],
                    [5, 0, 1, 0, 0, 8, 0, 0, 0],
                    [7, 0, 9, 3, 1, 0, 5, 6, 8],
                    [6, 0, 4, 7, 2, 5, 0, 3, 9]
                ],
                "want": [
                    [0, 5, 3, 0, 0, 0, 0, 0, 4],
                    [9, 0, 0, 4, 3, 0, 0, 0, 5],
                    [0, 0, 0, 2, 0, 9, 3, 8, 0],
                    [0, 9, 0, 8, 7, 3, 4, 5, 0],
                    [3, 0, 0, 0, 0, 2, 0, 0, 0],
                    [8, 7, 0, 0, 0, 0, 0, 1, 3],
                    [5, 3, 1, 0, 0, 8, 0, 0, 0],
                    [7, 2, 9, 3, 1, 4, 5, 6, 8],
                    [6, 8, 4, 7, 2, 5, 1, 3, 9]
                ]
            }
        ]

        for test in tests:
            possible = solver.findPossibleDigitsForCells(test["grid"])
            self.assertEqual(test["want"], solver.solveOneDigitInARow(test["grid"], possible))

    def testSolveOneDigitInAColumn(self):
        tests = [
            {
                "describe": "simple example",
                "grid": [
                    [1, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 5, 0, 0, 0, 0],
                    [3, 0, 0, 0, 0, 0, 0, 0, 0],
                    [4, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [6, 0, 0, 0, 0, 0, 0, 0, 0],
                    [7, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 5, 0],
                    [9, 0, 0, 0, 0, 0, 0, 0, 0]
                ],
                "want": [
                    [1, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 5, 0, 0, 0, 0],
                    [3, 0, 0, 0, 0, 0, 0, 0, 0],
                    [4, 0, 0, 0, 0, 0, 0, 0, 0],
                    [5, 0, 0, 0, 0, 0, 0, 0, 0],
                    [6, 0, 0, 0, 0, 0, 0, 0, 0],
                    [7, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 5, 0],
                    [9, 0, 0, 0, 0, 0, 0, 0, 0]
                ]
            },
            {
                "describe": "complex example",
                "grid": [
                    [0, 5, 0, 0, 0, 0, 0, 0, 4],
                    [9, 0, 0, 4, 3, 0, 0, 0, 0],
                    [0, 0, 0, 2, 0, 9, 3, 8, 0],
                    [0, 9, 0, 0, 7, 0, 4, 5, 0],
                    [3, 0, 0, 0, 0, 2, 0, 0, 0],
                    [8, 7, 0, 0, 0, 0, 0, 1, 3],
                    [5, 0, 1, 0, 0, 8, 0, 0, 0],
                    [7, 0, 9, 3, 1, 0, 5, 6, 8],
                    [6, 0, 4, 7, 2, 5, 0, 3, 9]
                ],
                "want": [
                    [0, 5, 3, 0, 0, 0, 0, 0, 4],
                    [9, 0, 0, 4, 3, 0, 0, 0, 0],
                    [4, 0, 0, 2, 0, 9, 3, 8, 0],
                    [0, 9, 0, 0, 7, 3, 4, 5, 0],
                    [3, 0, 0, 0, 0, 2, 8, 0, 0],
                    [8, 7, 0, 0, 0, 0, 0, 1, 3],
                    [5, 3, 1, 0, 0, 8, 0, 4, 0],
                    [7, 0, 9, 3, 1, 0, 5, 6, 8],
                    [6, 0, 4, 7, 2, 5, 0, 3, 9]
                ]
            }
        ]

        for test in tests:
            possible = solver.findPossibleDigitsForCells(test["grid"])
            self.assertEqual(test["want"], solver.solveOneDigitInAColumn(test["grid"], possible))

    def testSolveOneDigitIn3x3(self):
        tests = [
            {
                "describe": "simple example",
                "grid": [
                    [1, 2, 0, 0, 0, 0, 0, 0, 0],
                    [4, 0, 6, 0, 0, 0, 0, 0, 0],
                    [7, 8, 9, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 5, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                ],
                "want": [
                    [1, 2, 5, 0, 0, 0, 0, 0, 0],
                    [4, 0, 6, 0, 0, 0, 0, 0, 0],
                    [7, 8, 9, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 5, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                ]
            },
            {
                "describe": "complex example",
                "grid": [
                    [0, 5, 0, 0, 0, 0, 0, 0, 4],
                    [9, 0, 0, 4, 3, 0, 0, 0, 0],
                    [0, 0, 0, 2, 0, 9, 3, 8, 0],
                    [0, 9, 0, 0, 7, 0, 4, 5, 0],
                    [3, 0, 0, 0, 0, 2, 0, 0, 0],
                    [8, 7, 0, 0, 0, 0, 0, 1, 3],
                    [5, 0, 1, 0, 0, 8, 0, 0, 0],
                    [7, 0, 9, 3, 1, 0, 5, 6, 8],
                    [6, 0, 4, 7, 2, 5, 0, 3, 9]
                ],
                "want": [
                    [0, 5, 3, 0, 0, 0, 0, 0, 4],
                    [9, 0, 0, 4, 3, 0, 0, 0, 0],
                    [0, 0, 0, 2, 5, 9, 3, 8, 0],
                    [0, 9, 0, 0, 7, 3, 4, 5, 0],
                    [3, 4, 0, 0, 0, 2, 8, 0, 0],
                    [8, 7, 0, 0, 0, 0, 0, 1, 3],
                    [5, 3, 1, 0, 0, 8, 0, 4, 0],
                    [7, 0, 9, 3, 1, 0, 5, 6, 8],
                    [6, 8, 4, 7, 2, 5, 1, 3, 9]
                ]
            }
        ]

        for test in tests:
            possible = solver.findPossibleDigitsForCells(test["grid"])
            self.assertEqual(test["want"], solver.solveOneDigitIn3x3(test["grid"], possible))

    def testEliminateDigitsWithRay(self):
        tests = [
            {
                "description": "simple example",
                "grid": [
                    [1, 2, 3, 0, 0, 0, 0, 0, 0],
                    [0, 4, 0, 0, 0, 0, 0, 0, 0],
                    [6, 7, 8, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                ],
                "expects": {
                    "row": 1,
                    "exceptionGrid": 0,
                    "notPossible": {0, 9}
                }
            }
        ]

        for test in tests:
            possible = solver.findPossibleDigitsForCells(test["grid"])
            solver.eliminateDigitsWithRay(possible)
            for coordinate, digits in possible.items():
                gridIndex = solver.calculateGridIndex(*coordinate)
                if gridIndex == test["expects"]["exceptionGrid"] or coordinate[0] != test["expects"]["row"]:
                    continue
                self.assertTrue(test["expects"]["notPossible"].isdisjoint(set(digits)))

    def testRepeatingRows(self):
        tests =  [
            {
                "description": "simple example",
                "coordinates": [(0,1), (2,1)],
                "want": [0, 2]
            }
        ]

        for test in tests:
            self.assertEqual(test["want"], solver.repeatingRows(test["coordinates"]))

    def testGetSquareEliminatedGrids(self):
        tests = [
            {
                "description": "simple example",
                "grid": [
                    [9, 0, 0, 0, 2, 7, 0, 5, 0],
                    [0, 5, 0, 0, 0, 0, 9, 0, 4],
                    [0, 0, 0, 5, 0, 4, 0, 0, 0],
                    [8, 0, 0, 0, 7, 5, 6, 4, 9],
                    [1, 0, 0, 0, 4, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 9, 8, 0, 1],
                    [0, 0, 0, 4, 5, 1, 0, 0, 0],
                    [0, 0, 0, 7, 3, 0, 0, 1, 0],
                    [5, 0, 1, 0, 0, 2, 0, 3, 7]
                ],
                "originGrid": 0,
                "targetRows": [0, 2],
                "targetNumber": 1,
                "want": [2]
            }
        ]

        for test in tests:
            possible = solver.findPossibleDigitsForCells(test["grid"])
            possibleDigitsOn3x3 = solver.groupPossibleDigitsBasedOn3x3(possible)
            self.assertEqual(test["want"], solver.findOpposingSquareEdge(possibleDigitsOn3x3, test["originGrid"], test["targetRows"], test["targetNumber"]))

    def testEliminateDigitsWithSquare(self):
        tests = [
            {
                "description": "simple example",
                "grid": [
                    [9, 0, 0, 0, 2, 7, 0, 5, 0],
                    [0, 5, 0, 0, 0, 0, 9, 0, 4],
                    [0, 0, 0, 5, 0, 4, 0, 0, 0],
                    [8, 0, 0, 0, 7, 5, 6, 4, 9],
                    [1, 0, 0, 0, 4, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 9, 8, 0, 1],
                    [0, 0, 0, 4, 5, 1, 0, 0, 0],
                    [0, 0, 0, 7, 3, 0, 0, 1, 0],
                    [5, 0, 1, 0, 0, 2, 0, 3, 7]
                ],
                "notPossible": {
                    "coordinates": [(0, 3), (0, 4), (0,5), (2, 3), (2, 4), (2,5)],
                    "number": 1
                }
            }
        ]

        for test in tests:
            possible = solver.findPossibleDigitsForCells(test["grid"])
            solver.eliminateDigitsWithSquare(possible)
            for coordinate in test['notPossible']['coordinates']:
                if coordinate in possible:
                    self.assertTrue(test['notPossible']['number'] not in possible[coordinate])

    if __name__ == '__main__':
        unittest.main()