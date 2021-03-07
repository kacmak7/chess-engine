import pieces
import numpy as np

class Board:

    def __init__(self):
        self.A = np.array([
            np.array([pieces.Rook.id, pieces.Knight.id, pieces.Bishop.id, pieces.Queen.id, pieces.King.id, pieces.Bishop.id, pieces.Knight.id, pieces.Rook.id]),
            np.full(8, pieces.Pawn.id),
            np.zeros(8, dtype=np.int8),
            np.zeros(8, dtype=np.int8),
            np.zeros(8, dtype=np.int8),np.zeros(8, dtype=np.int8),
            np.full(8, pieces.Pawn.id),
            np.array([pieces.Rook.id, pieces.Knight.id, pieces.Bishop.id, pieces.Queen.id, pieces.King.id, pieces.Bishop.id, pieces.Knight.id, pieces.Rook.id]),
        ])

    def display(self):
        print(self.A)

    def move(self, cx, cy, nx, ny):
        self.A[nx, ny] = self.A[cx, cy]
        self.A[cx, cy] = 0




