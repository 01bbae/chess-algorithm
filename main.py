from tree import *  # Import the Tree class from the "tree" module
import os
import chess
import time

# Determine the path to the Stockfish engine based on the operating system
if os.name == "nt":
    engine_path = "stockfish-windows-2022-x86-64-avx2.exe"
elif os.name == "posix":
    engine_path = "stockfish"
else:
    raise Exception("OS Error: OS not recognized")

print("\nChess-Algorithm\n")

# Prompt the user to enter the FEN to analyze, depth, and number of branches
fen = input("Enter FEN to analyze (Press enter to use default initial chess position): ")
depth = input("Enter depth to analyze (WARNING: having a large depth might crash your computer. We recommend having depth of 2 or 3): ")
num_branches = input("Enter number of branches to analyze (WARNING: having a large number of branches might crash your computer. We recommend having depth of less than 10): ")

# Set the default FEN to the starting position if no input is provided
if len(fen) == 0:
    fen = chess.STARTING_FEN

print("\nLoading...")
print("This might take a few minutes...")

# Create a new Tree instance with the provided FEN, depth, number of branches, and engine path
newTree = Tree(fen, int(depth), int(num_branches), engine_path)
print("\nAnalysis tree created.\n")

while True:
    print("================================================================")
    print("What would you like to do:")
    print("1. Get evaluation of the current position using Stockfish")
    print("2. Get the best next move in the current position")
    print("3. Exit program")
    print("================================================================")

    choice = input("\nEnter choice number: ")

    if int(choice) == 1:
        print(newTree.get_root_node().getEval())  # Get the evaluation of the current position using Stockfish and print it
        time.sleep(2.5)  # Pause for 2.5 seconds
    elif int(choice) == 2:
        best_move = newTree.getBestNextMove()  # Get the best next move in the current position
        print(best_move[1].getBoard())  # Print the board after the best move
        print("Score: ", best_move[0])  # Print the score associated with the best move
        print("Eval: ", best_move[1].getEval())  # Print the evaluation of the resulting position
        time.sleep(2.5)  # Pause for 2.5 seconds
    elif int(choice) == 3:
        exit()  # Exit the program



# newTree.getBestNextMove().printPosition()
# print(newTree.get_root_children())
# newTree.print_root_board()
# print(newTree.get_root_node().getEval().white())
# print(newTree.get_root_node().getEval().black())
# print(newTree.get_root_node().getEval().relative)
# print(newTree.get_root_node().getEval().black().score())