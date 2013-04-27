NameOfTheGame = "Othello"

from Tkinter import *
import Tkinter

BOARD_SIZE = 8
class board():
    PADDING = 2
    BORDER = 10
    LINE_THICKNESS = 1
    def __init__(self):
        self.root = Tk()
        self.root.title(NameOfTheGame)
        Label(self.root, text='Welcome To The Othello Game!').pack(pady=10)
        self.canvas = Tkinter.Canvas(self.root, height=600, width=600)
        self.canvas.pack()
        width = int(self.canvas["width"])
        height = int(self.canvas["height"])
        self.GRID_SIZE = ([width, height][width > height] - self.BORDER * 2) / (BOARD_SIZE)
        self._drawGround()
        def handler(event, self=self):
            return self.__onClick(event)
        def undo(event, self=self):
            return self.__undo(event)
        self.canvas.bind('<Button-1>', handler)
        self.canvas.bind('<Button-2>', undo)
        self.myTurn = False
        
    def _drawGround(self):
        for i in range(0, BOARD_SIZE + 1):
            self.canvas.create_line(
                               self.BORDER,
                               self.BORDER + self.GRID_SIZE * i,
                               self.BORDER + self.GRID_SIZE * BOARD_SIZE,
                               self.BORDER + self.GRID_SIZE * i,
                               width=self.LINE_THICKNESS)
            self.canvas.create_line(
                               self.BORDER + self.GRID_SIZE * i,
                               self.BORDER,
                               self.BORDER + self.GRID_SIZE * i,
                               self.BORDER + self.GRID_SIZE * BOARD_SIZE,
                               width=self.LINE_THICKNESS)
        
    def __onClick(self, event):
        if self.myTurn:
            pos = self._getPosition(event.x, event.y)
            self.myTurn = False
            self.onPut(pos)
    
    def __undo(self, event):
        #self.canvas.delete(m[2])
        pass
    
    def __drawStone(self, position, color):
        xy = self._getCoordination(position)
        return self.canvas.create_oval(xy[0], xy[1], xy[0] + self.GRID_SIZE, xy[1] + self.GRID_SIZE, fill=color)
    
    def _getPosition(self, x, y):
        toGround = lambda x: (x - self.BORDER) / self.GRID_SIZE
        return (toGround(x), toGround(y))
    
    def _getCoordination(self, position):
        toAxis = lambda x: self.GRID_SIZE * x + self.BORDER
        return (toAxis(position[0]), toAxis(position[1]))

    def registerPutEvent(self, onPut):
        self.onPut = onPut
        
    def think(self):
        self.myTurn = True
    
    def deny(self):
        self.myTurn = True
    
    def drawStones(self, stones):
        for pos, isBlack in stones.items():
            [self.drawWhite, self.drawBlack][isBlack](pos)
            
    def drawWhite(self, pos):
        self.__drawStone(pos, "white")
        
    def drawBlack(self, pos):
        self.__drawStone(pos, "black")
        
    def eventLoop(self):
        self.root.mainloop()
