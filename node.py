import asyncio
import chess
import chess.engine
import typing


class Node:
    def __init__(self, fen, engine_path) -> None:
        self.fen = fen
        self.board = chess.Board(fen=fen)
        self.engine_path = engine_path
        self.children = []

    async def getEval(self) -> chess.engine.PovScore:
        transport, engine = await chess.engine.popen_uci("/usr/bin/stockfish")
        info = await engine.analyse(self.board, chess.engine.Limit(depth=20))
        await engine.quit()
        return info["score"]
