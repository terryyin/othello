class ai:
    def registerPutEvent(self, onPut):
        self.put = onPut
        
    def think(self, stones, whoAmI):
        for pos in stones.possibleMoves(whoAmI):
            self.put(pos)
