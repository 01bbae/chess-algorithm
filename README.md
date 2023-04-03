# Chess-Algorithm

## Description

Currently, popular chess engines will evaluate the most ideal move on chess based on the best move. Stockfish, for example, uses the alpha-beta pruning algorithm to evaluate the best positions.

The goal of this project is to build on top of these popular chess engines; Specifically, we would like to add a chess algorithm that will return not the best move, but good-enough moves so players have variety of moves to choose from.

## Setup:

1. Make sure you have Python 3.7+ installed
2. git clone this repository
3. pip install chess
4. cd into this repository directory. Run main.py

## Progress:

- [x] Understand how stockfish and other chess engine algorithm is ran
- [x] Implemented stockfish library into python script
- [x] Implemented Zobrist Hashing Algorithm
- [ ] Connect Zobrist Hashing Algorithm to chessboard
- [x] Grab the list of "good moves"

## Contributors:

BJ Bae, Joan Karstrom, Tyler Kay, Eric Phan, Raymond Yan

## Useful References:

- https://python-chess.readthedocs.io/en/latest/
- https://healeycodes.com/building-my-own-chess-engine
- https://stackoverflow.com/questions/16500739/chess-high-branching-factor
- https://chess.stackexchange.com/questions/33161/do-chess-engines-hold-their-search-tree-in-memory
- https://en.wikipedia.org/wiki/Transposition_table
- https://en.wikipedia.org/wiki/Zobrist_hashing
- https://en.wikipedia.org/wiki/Zobrist_hashing
- https://support.chess.com/article/2965-how-are-moves-classified-what-is-a-blunder-or-brilliant-and-etc
