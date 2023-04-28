from node import *
import asyncio
import chess
from chess.engine import Cp
import typing
import queue
import random
from operator import itemgetter


class Tree:
    def __init__(self, starting_fen, depth, num_branches, engine_path) -> None:
        self.engine_path = engine_path
        self.root_node = Node(chess.Board(fen=starting_fen), engine_path)
        self.tree = self.create_tree(self.root_node, depth, num_branches)

    def create_tree(self, root, depth, num_branches) -> Node:
        if (len(list(root.board.legal_moves)) > 0 and depth >= 0):
            # only get "num_branches" legal moves
            for move in random.sample(list(root.board.legal_moves), num_branches):
                newboard = chess.Board(root.board.fen())
                newboard.push(move)
                # print(move)
                # print(newboard)

                child_node = Node(newboard, root.engine_path)
                # small pruning optimization
                # if next position has lower eval than current, cut itself and all children
                # if child_node.getEval().__ge__(root.getEval()):
                root.children.append(child_node)
                self.create_tree(child_node, depth-1, num_branches)
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
        # initialize max node to be the first white move in the depth 3 of the tree (white1->black1->white2)
        max_node = self.root_node.get_children()[0].get_children()[
            0].get_children()[0]
        # window of 100 centipawn score to select "good moves"
        window = 100
        for white1 in self.root_node.get_children():

            # Get the node with min eval for opposite color (min part of MinMax Algorithm)
            min_black_node = white1.get_children()[0]
            for black1 in white1.get_children():
                if min_black_node.getEval().__ge__(black1.getEval()):
                    min_black_node = black1

            # calculate the "overall score" for each of the branches
            # first calculate number of blunders, mistakes, inaccuracies, good, and excellent moves
            # all calculated using centipawn loss
            for white2 in min_black_node.get_children():
                if max_node.getEval().__le__(white2.getEval()):
                    max_node = white2

            print(max_node.getEval())

            num_good_moves = 0
            for white2 in min_black_node.get_children():
                if (white2.getEval().score() - max_node.getEval().score()) < (window):
                    num_good_moves += 1
            score = num_good_moves
            move_score.append((score, white1))
            # if (curr_node.getEval().__le__(Cp(min_black_node.getEval().score() - 300))):
            #     num_blunder += 1
            # elif(curr_node.getEval().__gt__(Cp(min_black_node.getEval().score() - 300)) and curr_node.getEval().__lt__(Cp(min_black_node.getEval().score() - 100))):
            #     num_mistake += 1
            # elif(curr_node.getEval().__ge__(Cp(min_black_node.getEval().score() - 100)) and curr_node.getEval().__lt__(Cp(min_black_node.getEval().score() + 0))):
            #     num_inaccuracy += 1
            # elif(curr_node.getEval().__gt__(Cp(min_black_node.getEval().score() - 0)) and curr_node.getEval().__lt__(Cp(min_black_node.getEval().score() + 300))):
            #     num_good += 1
            # elif(curr_node.getEval().__ge__(Cp(min_black_node.getEval().score() + 300))):
            #     num_excellent += 1

            # arbitrary parameters to weight different types of moves
            # use function 10/(x+2) to weight choices of moves (more = bad, less = good) This is also arbitrary
            # score += num_blunder*-5 + num_mistake*-2 + num_inaccuracy*-1 + num_good * \
            #     1 + num_excellent*1 + \
            #     (10/(num_choices+2)) + curr_node.getEval().score()
        best_move = max(move_score, key=itemgetter(0))
        return best_move
