#!/usr/bin/env python

try:
    from src.othello import game, board, ai
except:
    from othello import game, board, ai

ui = board()
game(ui, ui, ai()).start()