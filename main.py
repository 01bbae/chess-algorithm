from tree import *
import os
import chess
import time

# Warning: Currently the program is running into memory limitations due to the recursive implementation of the algorithm
if (os.name == "nt"):
    engine_path = "stockfish-windows-2022-x86-64-avx2.exe"
elif (os.name == "posix"):
    engine_path = "stockfish"
else:
    raise Exception("OS Error: OS not recognized")
print("Chess-Algorithm")
fen = input("Enter FEN to analyze (Press enter to use default initial chess position): ")
depth = input("Enter depth to analyze (WARNING: having a large depth might crash your computer. We recommend having depth of 2 or 3): ")
num_branches = input("Enter number of branches to analyze (WARNING: having a large number of branches might crash your computer. We recommend having depth of less than 10): ")
if len(fen)==0:
    fen = chess.STARTING_FEN
print("Loading...")
print("This might take a few minutes...")
newTree = Tree(fen, int(depth), int(num_branches), engine_path)
print("Analysis tree created.")
while True:
    print("================================================================")
    print("What would you like to do:")
    print("1. Get evaluation of the current position using stockfish")
    print("2. Get best next move in the current position")
    print("3. Exit program")
    print("================================================================")

    choice = input("Enter choice number: ")

    if int(choice) == 1:
        print(newTree.get_root_node().getEval())
        time.sleep(2.5)
    elif int(choice) == 2:
        best_move = newTree.getBestNextMove()
        print(best_move[1].getBoard())
        print("Score: ", best_move[0])
        print("Eval: ", best_move[1].getEval())
        time.sleep(2.5)
    elif int(choice) == 3:
        exit()



# newTree.getBestNextMove().printPosition()
# print(newTree.get_root_children())
# newTree.print_root_board()
# print(newTree.get_root_node().getEval().white())
# print(newTree.get_root_node().getEval().black())
# print(newTree.get_root_node().getEval().relative)
# print(newTree.get_root_node().getEval().black().score())