# Chess-Algorithm

## Description

The motivation behind modifying a chess algorithm that returns "good-enough" moves instead of just the best move is to enhance the player experience and increase the variety of possible gameplay scenarios. Currently, popular chess engines such as Stockfish are designed to evaluate and choose the most optimal move based on a given set of parameters, such as material advantage, piece mobility, and king safety. These popular chess engines use algorithms such as alpha-beta pruning, and mini-max algorithm.

While this approach has been successful in producing strong and reliable chess engines, it can also lead to repetitive gameplay and lack of variety. Players may feel like they are always playing against the same strategy, which can become monotonous over time.

By introducing a chess algorithm that returns good-enough moves, players are given a wider range of options to choose from. These moves may not be the absolute best, but they can still be strong and strategically sound, providing a fresh and varied gameplay experience. Additionally, players may find it more challenging and enjoyable to play against a chess engine that is not always making the optimal move.

Overall, the goal of this project is to add an element of unpredictability and excitement to chess gameplay, while still maintaining a high level of strategic and tactical sophistication.

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
