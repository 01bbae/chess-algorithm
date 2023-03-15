from node import *
import asyncio
import chess
import chess.engine
import typing


class Tree:
    def __init__(self, starting_fen, engine_path) -> None:
        self.engine_path = engine_path
        self.root_node = Node(chess.Board(fen=starting_fen), engine_path)

    def create_tree(self, root, depth) -> None:
        # print(list(root.board.legal_moves))
        if (len(list(root.board.legal_moves)) != 0 and depth >= 0):
            for move in root.board.legal_moves:
                print(move)
                newboard = chess.Board(root.board.fen())
                newboard.push(move)
                print(newboard)
                child_node = Node(newboard, root.engine_path)
                root.children.append(child_node)
                self.create_tree(child_node, depth-1)

    def get_children(self, node) -> list[int]:
        print(node.children)

    def get_root_fen(self):
        print(self.root_node.board.fen())

    def print_root_board(self):
        print(self.root_node.board)
