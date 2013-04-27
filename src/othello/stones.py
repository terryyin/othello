
class stones:
    
    def __init__(self, putStones):
        self.stones = putStones
    
    def put(self, pos, black):
        if pos not in self.stones:
            neighbor = pos[0], pos[1] - 1
            if neighbor in self.stones:
                self.stones[neighbor] = black
                self.stones[pos] = black
                return True
        