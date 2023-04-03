import asyncio
import chess
import chess.engine
import typing


class Node:
    def __init__(self, board, engine_path) -> None:
        self.board = board
        self.engine_path = engine_path
        self.children = []
        engine = chess.engine.SimpleEngine.popen_uci(self.engine_path)
        info = engine.analyse(self.board, chess.engine.Limit(depth=10))
        self.eval = info["score"]
        engine.quit()

    def getEval(self) -> chess.engine.PovScore:
        return self.eval

    def get_node_info(self):
        return (self.board.fen(), self.eval)
    
    def get_children(self):
        return self.children
    
    def get_num_children(self):
        return len(self.children)
    
    def getBoard(self):
        return self.board

    
