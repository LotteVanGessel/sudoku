import z3
from const import ROWS, COLS

class SudokuSolver:
    def __init__(self, board) -> None:
        self.board = board
        self.variables = [[ 0 for i in range(COLS)] for j in range(ROWS)]
        self.model = None 

        
    def solve(self):
        if not self.model:
            s = z3.Solver()
            for row in range(ROWS):
                for col in range(COLS):
                    square = self.board.squares[row][col]
                    self.variables[row][col] = z3.Int(f"s_{row}_{col}")
                    x = self.variables[row][col]
                    if square.static:
                        print("here")
                        s.add(x == square.number)
                    else:
                        s.add(z3.Or(x == 1, x == 2, x==3, x==4, x== 5, x==6, x==7, x==8, x ==9))
            for col in range(COLS):
                for i in range(1, 10):
                    s.add(z3.Or(self.variables[0][col] == i, self.variables[1][col] == i, self.variables[2][col] == i, self.variables[3][col] == i, self.variables[4][col] == i, self.variables[5][col] == i, self.variables[6][col] == i, self.variables[7][col] == i, self.variables[8][col] == i))
            for row in range(ROWS):
                for i in range(1, 10):
                    s.add(z3.Or(self.variables[row][0] == i, self.variables[row][1] == i, self.variables[row][2] == i, self.variables[row][3] == i, self.variables[row][4] == i, self.variables[row][5] == i, self.variables[row][6] == i, self.variables[row][7] == i, self.variables[row][8] == i))
        
            s.check()
            m = s.model()
            print(m)
            self.model = m
