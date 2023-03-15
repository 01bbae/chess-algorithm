import chess
import random

def init_zobrist():
    table = []
    for i in range(64):
        for j in range(12):
            table[i][j] = random.getrandbits(1)
    black_to_move = random.getrandbits(1)
def hashing(board):
    # Taken from Zobrist Hashing Wikipedia Page
    hash = 0
    if board.turn == chess.BLACK:
        h = h ^ 


# constant indices
#     white_pawn := 1
#     white_rook := 2
#     # etc.
#     black_king := 12

# function init_zobrist():
#     # fill a table of random numbers/bitstrings
#     table := a 2-d array of size 64×12
#     for i from 1 to 64:  # loop over the board, represented as a linear array
#         for j from 1 to 12:      # loop over the pieces
#             table[i][j] := random_bitstring()
#     table.black_to_move = random_bitstring()

# function hash(board):
#     h := 0
#     if is_black_turn(board):
#         h := h XOR table.black_to_move
#     for i from 1 to 64:      # loop over the board positions
#         if board[i] ≠ empty:
#             j := the piece at board[i], as listed in the constant indices, above
#             h := h XOR table[i][j]
#     return h