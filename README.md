# Chess-Algorithm

## Introduction

The game of Chess has changed dramatically throughout the bountiful years that it has been played all over the world. Movies and other forms of media have popularized the game, while mathematicians, strategists, among some of the smartest individuals have played and revolutionalized the game that we know it. Players have analyzed advances or withdraws and have memorized and choreographed counterplays to specific moves made during matches. Some are even able to foresee moves that their opponents will make. One, two, three moves in the future have already been planned, allowing for them to make the perfect adjustments. With these tools in their arsenal, it wouldn't be long until a player takes complete domination over the game. However, these players (even though they reign amongst the best) are still human and are very capable of making human errors during a game. So, what if they were against a computer that isn't able to?

The idea of a combination of Chess and Artificial Intelligence isn't unheard of. In the 1950s, Alan Turing began the process of writing a computer program that was able to simulate a game of chess. Within the same year, Claude Shannon wrote a paper about plans to make the program eventually be able to play "good" chess. However, due to the limitations of computers, it was difficult not to underestimate the idea which seemed like a pipedream. Chess programs kept on getting beaten by human players since then and while the computer programs would sometimes get a win or tie, it was never any real contest. It allowed for newer players to quickly learn the game but proved to be no match for any decent player. It wasn't until recently, when a tournament of two dozen Chess players from around the world would compete in such a memorable event. The matches were being livestreamed on Twitch and after about a month of playing, there was one clear winner: Stockfish, "the strongest chess computer to date."

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
- https://cs.uwaterloo.ca/~alopez-o/divulge/chimp.html#:~:text=in%20computer%20development.-,History%20of%20Computer%20Chess,program%20with%20pencil%20and%20paper

