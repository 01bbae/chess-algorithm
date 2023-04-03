from node import *
import asyncio
import chess
from chess.engine import Cp
import typing
import queue
import random
from operator import itemgetter


class Tree:
    def __init__(self, starting_fen, depth, engine_path) -> None:
        self.engine_path = engine_path
        self.root_node = Node(chess.Board(fen=starting_fen), engine_path)
        self.tree = self.create_tree(self.root_node, depth)

    def create_tree(self, root, depth) -> Node:
        if (len(list(root.board.legal_moves)) > 0 and depth >= 0):
            for move in random.sample(list(root.board.legal_moves), 10): # only get 10 legal moves
                newboard = chess.Board(root.board.fen())
                newboard.push(move)
                # print(move)
                # print(newboard)

                child_node = Node(newboard, root.engine_path)
                # small pruning optimization
                # if next position has lower eval than current, cut itself and all children
                # if child_node.getEval().__ge__(root.getEval()):
                root.children.append(child_node)
                self.create_tree(child_node, depth-1)
        return root



    def get_root_fen(self):
        print(self.root_node.board.fen())
    
    def get_root_children(self):
        return self.root_node.get_children()

    def get_root_node(self):
        return self.root_node

    def print_root_board(self):
        print(self.root_node.board)
    
    def getBestNextMove(self):
        # list of tuples of "scores" and moves
        move_score = []
        for node_i in self.root_node.get_children():

            # Get the node with min eval for opposite color (min part of MinMax Algorithm)
            min_node = node_i.get_children()[0]
            for node_j in node_i.get_children():
                if min_node.getEval().__ge__(node_j.getEval()):
                    min_node = node_j
            
            # calculate the "overall score" for each of the branches
            # first calculate number of blunders, mistakes, inaccuracies, good, and excellent moves
            num_choices = 0
            num_blunder = 0
            num_mistake = 0
            num_inaccuracy = 0
            num_good = 0
            num_excellent = 0
            score = 0
            for curr_node in min_node.get_children():
                num_choices += 1
                # all calculated using centipawn loss
                print(curr_node.getEval())
                if (curr_node.getEval().__le__(Cp(min_node.getEval().score() - 300))):
                    num_blunder += 1
                elif(curr_node.getEval().__gt__(Cp(min_node.getEval().score() - 300)) and curr_node.getEval().__lt__(Cp(min_node.getEval().score() - 100))):
                    num_mistake += 1
                elif(curr_node.getEval().__ge__(Cp(min_node.getEval().score() - 100)) and curr_node.getEval().__lt__(Cp(min_node.getEval().score() + 0))):
                    num_inaccuracy += 1
                elif(curr_node.getEval().__gt__(Cp(min_node.getEval().score() - 0)) and curr_node.getEval().__lt__(Cp(min_node.getEval().score() + 300))):
                    num_good += 1
                elif(curr_node.getEval().__ge__(Cp(min_node.getEval().score() + 300))):
                    num_excellent += 1
                 # arbitrary parameters to weight different types of moves
                # use function 10/(x+2) to weight choices of moves (more = bad, less = good) This is also arbitrary
                score += num_blunder*-5 + num_mistake*-2 + num_inaccuracy*-1 + num_good*1 + num_excellent*1 + (10/(num_choices+2)) + curr_node.getEval().score()
                # print("num_choices", num_choices)
                # print("num_blunder", num_blunder)
                # print("num_mistake", num_mistake)
                # print("num_inaccuracy", num_inaccuracy)
                # print("num_good", num_good)
                # print("num_excellent", num_excellent)
            move_score.append((score, node_i))
        best_move = max(move_score, key=itemgetter(0))
        return best_move
                



