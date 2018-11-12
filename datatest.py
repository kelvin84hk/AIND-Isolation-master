# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 20:58:45 2018

@author: Kelvin
"""

from game_agent import (MinimaxPlayer, AlphaBetaPlayer, custom_score,
                        custom_score_2, custom_score_3, custom_score_4, custom_score_5)

from sample_players import (RandomPlayer, open_move_score,
                            improved_score, center_score)
from isolation import Board
import random
import timeit

player1 = RandomPlayer()
player2 = AlphaBetaPlayer(score_fn=improved_score)

player3 = AlphaBetaPlayer(score_fn=custom_score)
player4 = AlphaBetaPlayer(score_fn=custom_score_2)
player5 = AlphaBetaPlayer(score_fn=custom_score_3)
player6 = AlphaBetaPlayer(score_fn=custom_score_4)
player7 = AlphaBetaPlayer(score_fn=custom_score_5)


    
time_limit=150
time_millis = lambda: 1000 * timeit.default_timer()

players=[player2,player3,player4,player5,player6,player7]

i=0
for p in players:
    
    game = Board(p,player1)
    #for _ in range(2):
       # move = random.choice(game.get_legal_moves())
    game.apply_move((2,2))
    game.apply_move((6,6))

    c=0
    for _ in range(5000):
        move_start = time_millis()
        time_left = lambda : time_limit - (time_millis() - move_start)
        curr_move = p.get_move(game, time_left)
        c+=p.search_depth
    print('function ', str(i), ' depth :', str(c/5000))
    i=i+1
    del game
#game1 = Board(player3,player1)
#for _ in range(2):
#    move = random.choice(game1.get_legal_moves())
#    game1.apply_move(move)
#c=0
#for _ in range(1000):
#    move_start = time_millis()
#    time_left = lambda : time_limit - (time_millis() - move_start)
#    curr_move = player3.get_move(game1, time_left)
#    c+=player3.search_depth
#print('cus 1 depth :', str(c/1000))
#
#game2 = Board(player4,player1)
#for _ in range(2):
#    move = random.choice(game2.get_legal_moves())
#    game2.apply_move(move)
#c=0
#for _ in range(1000):
#    move_start = time_millis()
#    time_left = lambda : time_limit - (time_millis() - move_start)
#    curr_move = player3.get_move(game1, time_left)
#    c+=player4.search_depth
#print('cus 2 depth :', str(c/1000))


