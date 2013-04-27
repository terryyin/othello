#!/usr/bin/env python

try:
    from src.othello import game, ai
    from src.othello.board import board
except:
    from othello import game, board, ai
    from othello.board import board

ui = board()
game(ui, ui, ai()).start()