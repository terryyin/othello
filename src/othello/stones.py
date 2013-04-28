
class stones:
    
    def __init__(self, putStones):
        self.stones = putStones
    

    def put(self, pos, black):
        if pos in self.stones:
            return False
        reverse = self._getReversePosistions(pos, black)
        if len(reverse) > 0:
            for stone in reverse + [pos]:
                self.stones[stone] = black
            return True
        return False
    
    def _getReversePosistions(self, pos, black):
        reverse = []
        for i in range(8):
            reverseOnThisDirection = self._getReverseOfDirection(pos, black, i)
            reverse.extend(reverseOnThisDirection)
        
        return reverse

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
        