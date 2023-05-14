# Chess-Algorithm

## Introduction

The game of Chess has changed dramatically throughout the bountiful years that it has been played all over the world. Movies and other forms of media have popularized the game, while mathematicians, strategists, among some of the smartest individuals have played and revolutionalized the game that we know it. Players have analyzed advances or withdraws and have memorized and choreographed counterplays to specific moves made during matches. Some are even able to foresee moves that their opponents will make. One, two, three moves in the future have already been planned, allowing for them to make the perfect adjustments. With these tools in their arsenal, it wouldn't be long until a player takes complete domination over the game. However, these players (even though they reign amongst the best) are still human and are very capable of making human errors during a game. So, what if they were against a computer that isn't able to?

The idea of a combination of Chess and Artificial Intelligence isn't unheard of. In the 1950s, Alan Turing began the process of writing a computer program that was able to simulate a game of chess. Within the same year, Claude Shannon wrote a paper about plans to make the program eventually be able to play "good" chess. However, due to the limitations of computers, it was difficult not to underestimate the idea which seemed like a pipedream. Chess programs kept on getting beaten by human players since then and while the computer programs would sometimes get a win or tie, it was never any real contest. It allowed for newer players to quickly learn the game but proved to be no match for any decent player. It wasn't until recently, when a tournament of two dozen Chess players from around the world would compete in such a memorable event. The matches were being livestreamed on Twitch and after about a month of playing, there was one clear winner: Stockfish, "the strongest chess computer to date."

## Description/Motivation

It was a unanimous decision that we were all interested in learning more about the incredible works of the chess engine that is called Stockfish. As we diligently researched about the topic, we all kept looping back to the same idea. Although the chess engines today are compelling and can easily beat the best players in the world, they don’t necessarily help with allowing users to learn from the moves. They are sometimes too abstract in the sense that a human would never play that certain move. Which led us to this idea.

The motivation for modifying a chess algorithm to generate "good-enough" moves instead of solely the best move is to enhance the player experience and offer a more diverse set of gameplay scenarios. Current chess engines, such as Stockfish, use algorithms like alpha-beta pruning and minimax to select the optimal move based on factors like material advantage, piece mobility, and king safety. While this approach has led to powerful and reliable chess engines, it may be problematic for players who want to learn while playing.

By introducing a chess algorithm that generates multiple viable moves, players have a broader range of options to choose from, allowing them to select moves that align with their play-style and chess openings. Although these moves may not be the absolute best, they are still strategically sound and can offer a unique gameplay experience. Additionally, playing against a chess engine that does not always choose the optimal move may make the game more challenging and enjoyable.

## Literature Review

### [Computer Chess: Past to Present](https://cs.uwaterloo.ca/~alopez-o/divulge/chimp.html#:~:text=in%20computer%20development.-,History%20of%20Computer%20Chess,program%20with%20pencil%20and%20paper)

Before diving into a topic one hardly knows anything about, it is best to familiarize with the content and rich history of it first. This article gives a vital yet brief coverage of how Chess is linked with the idea of machine learning and artificial intelligence. It also allows readers who are new to the topic to easily digest the content as it isn't as dense as some others. It goes over the theory of games and introduces ideas of how computers play chess (which is through specific algorithms). If there is anybody new to the topic of AI, we recommend you start with this article and allow your curiosity to continue from there. 

### [Can Chess Survive Artificial Intelligence](https://www.thenewatlantis.com/publications/can-chess-survive-artificial-intelligence)

Although this article reads more like a narrative, it is still quite insightful. Of course it is critical to focus on the technical aspect of a project, this article allowed us to step back and view it as an opportunity to help people (chess players of all levels) or rather allowed us see the bigger picture. The article talks about chess engines and possibly how they are taking over, but does not view this necessarily as a negative aspect. In fact, the article introduced us to an idea some of us have not heard of -- Centaur Chess. This, like several other articles, inspired us to work on this project as whole.

### [Chess AI: Competing Paradigms for Machine Intelligence](https://www.mdpi.com/1099-4300/24/4/550)

This article was necessary for us to proceed with our project. It takes one of the most famously studied chess endgames and places it into several chess engines to see how each would respond to it differently. Not only does it show how they solved it, the article talks about what methods were explicitly used. Since we were using Stockfish's engine we were mainly focused on that aspect and how they were using the alpha-beta pruning search algorithm and how exactly it was improving minimax searches, but if anybody is taking a look at our project and would like to expand on the idea, we highly recommend taking a look at this article.

## Setup:

1. Make sure you have Python 3.7+ installed
2. git clone this repository
3. pip install chess
4. If you have a Mac, do 'brew install stockfish'. cd into /usr/local/Cellar/stockfish/{version}/bin. Copy the stockfish executable into the project directory.
5. cd into this repository directory. Run main.py

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
- https://www.thenewatlantis.com/publications/can-chess-survive-artificial-intelligence
- https://www.mdpi.com/1099-4300/24/4/550



