
from .stones import stones

BLACK = 1
WHITE = 0

class game:
    def __init__(self, board, white, black):
        self.board = board
        self.players = [white, black]
        self.white = white
        self.black = black
        self.white.registerPutEvent(self.onPutWhite)
        self.black.registerPutEvent(self.onPutBlack)
        self.stones = stones({ (3, 3) : WHITE,
                       (4, 4) : WHITE,
                       (3, 4) : BLACK,
                       (4, 3) : BLACK
                      })
        self.board.drawStones(self.stones.stones)
        self.players[BLACK].think(self.stones, BLACK)
    
    def start(self):
        self.board.eventLoop()
        return self
    
    def onPutWhite(self, pos):
        self.onPut(pos, WHITE)
        
    def onPutBlack(self, pos):
        self.onPut(pos, BLACK)
        
    def onPut(self, pos, who):
        if self.stones.put(pos, who):
            self.board.drawStones(self.stones.stones)
            who = not who
            if not list(self.stones.possibleMoves(who)):
                who = not who
                if not list(self.stones.possibleMoves(who)):
                    self.board.end(self.stones.blackVsWhite)
                    return
            self.players[who].think(self.stones, who)
        else:
            self.players[who].deny()

