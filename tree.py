import node
import asyncio
import chess
import chess.engine
import typing


class Tree:
    def __init__(self, starting_fen, engine_path) -> None:
        self.root_fen = starting_fen
        self.root_node = node(starting_fen, engine_path)

    def create_branches(self, node) -> None:
        if len(node.board.legal_moves()) != 0:
            for moves in node.board.legal_moves():
                # node = node(moves.)
                # node.children.append()
                # create_branches()
                pass

    def get_children(self, node) -> list[int]:
        pass
