# Chess-Algorithm

## Description/Motivation

The motivation for modifying a chess algorithm to generate "good-enough" moves instead of solely the best move is to enhance the player experience and offer a more diverse set of gameplay scenarios. Current chess engines, such as Stockfish, use algorithms like alpha-beta pruning and mini-max to select the optimal move based on factors like material advantage, piece mobility, and king safety. While this approach has led to powerful and reliable chess engines, it may be problematic for players who want to learn while playing.

By introducing a chess algorithm that generates multiple viable moves, players have a broader range of options to choose from, allowing them to select moves that align with their play-style and chess openings. Although these moves may not be the absolute best, they are still strategically sound and can offer a unique gameplay experience. Additionally, playing against a chess engine that does not always choose the optimal move may make the game more challenging and enjoyable.

## Setup:

1. Make sure you have Python 3.7+ installed
2. git clone this repository
3. pip install chess
4. If you have a Mac, do 'brew install stockfish'. cd into /usr/local/Cellar/stockfish/{version}/bin. Copy the stockfish executable into the project directory.
5. cd into this repository directory. Run main.py

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
