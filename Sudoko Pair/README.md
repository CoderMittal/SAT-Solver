
# Sudoku Pair

Sudoko Pair program is where we solve a pair of sudoku simultaneously such that the value at corresponding cells of two sudokus is not the same and all the rules of sudoku are applied

## Requirements
We are using SAT solver to solve the sudoku which is implemented using Python-based library PYSat

`pip install python-sat`

### Sudoku Pair Solver
Given a sudoku pair of size `k` in CSV file, it solves them using the solve.py file.
`python3 solve.py`

### Sudoku Pair Generator
Given the size `k` of the sudoku pair we generate a valid pair of sudoku.
`python3 generate.py`
