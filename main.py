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
newTree = Tree(chess.STARTING_FEN, 2, engine_path)
newTree.getBestNextMove().printPosition()
# print(newTree.get_root_children())
# newTree.print_root_board()
# print(newTree.get_root_node().getEval().white())
# print(newTree.get_root_node().getEval().black())
# print(newTree.get_root_node().getEval().relative)
# print(newTree.get_root_node().getEval().black().score())