import chess
import random



num_rows = 8
num_columns = 8
num_squares = num_rows * num_columns
type_pieces = {
    "white_pawn" : 1, 
    "white_rook" : 2, 
    "white_knight" : 3, 
    "white_bishop" : 4, 
    "white_queen" : 5, 
    "white_king" : 6, 
    "black_pawn" : 7, 
    "black_rook" : 8, 
    "black_knight" : 9, 
    "black_bishop" : 10, 
    "black_queen" : 11, 
    "black_king" : 12
}

def init_zobrist():
    table = []
    for i in range(num_rows):  # Iterate over rows
        for j in range(num_columns):  # Iterate over columns
            for k in range(len(type_pieces)):  # Iterate over piece types
                table[i][j][k] = random.getrandbits(1)  # Generate a random bit and assign it to the corresponding position in the table
    return table

def hashing():
    board = get_board()  # Get the game board
    zob_table = get_zobrist_table()  # Get the Zobrist table

    h = 0  # Initialize the hash value
    for i in range(num_rows):  # Iterate over rows
        for j in range(num_columns):  # Iterate over columns
            piece = get_piece(board, i, j)  # Get the piece at the current position on the board
            if piece != empty:  # Check if the position is not empty
                h ^= zob_table[i][j][piece]  # XOR the hash value with the Zobrist value for the piece at the current position
    return h  # Return the final hash value


#FIXME
#utility functions that need to be modified to work with the main program
def get_zobrist_table():
    #return zobrist table generated from init_zobrist()
    return None

def get_board():
    #return the chessboard from the main program
    return None

def get_piece(board, row_id, col_id):
    #get piece name on a specific square on board, or return "empty"
    return board[row_id][col_id]




#credit:
#https://en.wikipedia.org/wiki/Zobrist_hashing
#https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-5-zobrist-hashing/