from itertools import product
CORNER = 5
INNER_CORDER = -2
CORNER_SIDE = -1
BORDER = 2

class stones:
    scores = {(0,0):CORNER, (7,0):CORNER, (0,7):CORNER, (7,7):CORNER,
              (1.1):INNER_CORDER, (6,1):INNER_CORDER, (1,6):INNER_CORDER, (6,6):INNER_CORDER,
              (1,0):CORNER_SIDE, (6, 0): CORNER_SIDE, (0,1):CORNER_SIDE, (0,6):CORNER_SIDE, (7, 1):CORNER_SIDE, (7,6):CORNER_SIDE, (1, 7):CORNER_SIDE, (6, 7):CORNER_SIDE,
              (2, 0):BORDER, (3, 0):BORDER, (4, 0):BORDER, (5, 0):BORDER, (2, 7):BORDER, (3, 7):BORDER, (4, 7):BORDER, (5, 7):BORDER, (0, 2):BORDER, (0, 3):BORDER, (0, 4):BORDER, (0, 5):BORDER, (7, 2):BORDER, (7, 3):BORDER, (7, 4):BORDER, (7,5):BORDER
              }
    
    def __init__(self, putStones):
        self.stones = putStones
        self.availablePositions = set(product(range(8), repeat=2)) - set(self.stones.keys())
        self.blackVsWhite = sum((-1,1)[who] for who in self.stones.values())
    

    def putStoneAndReverse(self, pos, who, reverse):
        for stone in reverse + [pos]:
            self.stones[stone] = who
        self.availablePositions.remove(pos)
        self.blackVsWhite += (-1, 1)[who] * (len(reverse) * 2 + self.scores.get(pos, 1))

    def removeStoneAndReverse(self, pos, who, reverse):
        for stone in reverse:
            self.stones[stone] = not who
        del self.stones[pos]
        self.availablePositions.add(pos)
        self.blackVsWhite -= (-1, 1)[who] * (len(reverse) * 2 + self.scores.get(pos, 1))

    def put(self, pos, black):
        if pos in self.stones:
            return False
        reverse = self.getReversePosistions(pos, black)
        if len(reverse) > 0:
            self.putStoneAndReverse(pos, black, reverse)
            return True
        return False
    
    def getReversePosistions(self, pos, black):
        reverse = []
        for i in range(8):
            reverseOnThisDirection = self._getReverseOfDirection(pos, black, i)
            reverse.extend(reverseOnThisDirection)
        
        return reverse
    
    def possibleMoves(self, who):
        for pos in self.availablePositions:
            if pos not in self.stones:
                reverses = self.getReversePosistions(pos, who)
                if reverses:
                    yield pos, reverses

    def _getReverseOfDirection(self, pos, black, direct):
        reverseOnThisDirection = []
        for neighbor in self._neighborsOf(pos, direct):
            if neighbor not in self.stones:
                reverseOnThisDirection = []
                break
            if self.stones[neighbor] == black:
                break
            reverseOnThisDirection.append(neighbor)
        return reverseOnThisDirection

    def _neighborsOf(self, pos, direct):
        while(True):
            pos = pos[0] + (0,0,-1,1,-1,1,-1,1)[direct], pos[1] + (-1,1,0,0,-1,-1,1,1)[direct]
            yield pos
        