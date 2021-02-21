import pieces
import numpy as np

def start():
    # create a board with pieces
    board = np.array([
              np.array([pieces.Rook.id, pieces.Knight.id, pieces.Bishop.id, pieces.Queen.id, pieces.King.id, pieces.Bishop.id, pieces.Knight.id, pieces.Rook.id]),
              np.full(8, pieces.Pawn.id),
              np.zeros(8, dtype=np.int8),
              np.zeros(8, dtype=np.int8),
              np.zeros(8, dtype=np.int8),
              np.zeros(8, dtype=np.int8),
              np.full(8, pieces.Pawn.id),
              np.array([pieces.Rook.id, pieces.Knight.id, pieces.Bishop.id, pieces.Queen.id, pieces.King.id, pieces.Bishop.id, pieces.Knight.id, pieces.Rook.id]),
             ])
    print(board)
    print(board.shape)
