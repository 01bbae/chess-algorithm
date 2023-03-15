from tree import *
import chess

newTree = Tree(chess.STARTING_FEN, "./stockfish")
# newTree.print_root_board()
newTree.create_tree(newTree.root_node, 2)
