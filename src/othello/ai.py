class ai:
    def registerPutEvent(self, onPut):
        self.put = onPut
        
    def think(self, stones, whoAmI):
        self.put((0, 2))
