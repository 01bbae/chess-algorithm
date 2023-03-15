from tree import *
import os
import chess

# Warning: Currently the program is running into memory limitations due to the recursive implementation of the algorithm
if (os.name == "nt"):
    engine_path = "stockfish-windows-2022-x86-64-avx2.exe"
elif (os.name == "posix"):
    engine_path = "stockfish"
else:
    raise Exception("OS Error: OS not recognized")
newTree = Tree(chess.STARTING_FEN, engine_path)
# newTree.print_root_board()
newTree.create_tree(newTree.root_node, 2)
