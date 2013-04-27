class game:
    def __init__(self, board, white, black):
        self.board = board
        self.white = white
        self.black = black
        self.white.registerPutEvent(self.onPutWhite)
        self.black.registerPutEvent(self.onPutBlack)
        self.board.drawWhite((3, 3))
        self.board.drawWhite((4, 4))
        self.board.drawBlack((3, 4))
        self.board.drawBlack((4, 3))
        self.black.think()
    
    def start(self):
        self.board.eventLoop()
        return self
    
    def onPutWhite(self, pos):
        self.board.drawWhite(pos)
        self.black.think()
        
    def onPutBlack(self, pos):
        self.board.drawBlack(pos)
        self.white.think()