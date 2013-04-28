
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
        self.stones = stones({ (3, 3) : BLACK,
                       (4, 4) : BLACK,
                       (3, 4) : WHITE,
                       (4, 3) : WHITE
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
        
    def onPut(self, pos, black):
        if self.stones.put(pos, black):
            self.board.drawStones(self.stones.stones)
            self.players[not black].think(self.stones, not black)
        else:
            self.players[black].deny()

