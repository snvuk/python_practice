sudoku = [
    [0, 0, 0, 2, 0],
    [0, 0, 0, 1, 3],
    [1, 0, 0, 0, 4],
    [0, 0, 0, 4, 2],
    [0, 3, 2, 0, 0]
]

for row in range(5):
    for col in range(5):
        if sudoku [row][col] == 0:
            valid = True
            for i in range(5):
                if sudoku[row][i]