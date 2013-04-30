
class ai:
    def registerPutEvent(self, onPut):
        self.put = onPut
        self.depth = 5
        
    def think(self, stones, whoAmI):
        self.put(self.makeChoice(stones, whoAmI))

    def makeChoice(self, stones, whoAmI):
        choice = None
        alpha = -100
        beta = 100
        for pos, reverses in list(stones.possibleMoves(whoAmI)):
            stones.putStoneAndReverse(pos, whoAmI, reverses)
            val = self.negamax(stones, self.depth, -beta, -alpha, whoAmI)
            if val > alpha:
                alpha = val
                choice = pos
            stones.removeStoneAndReverse(pos, whoAmI, reverses)
        self.minWin = alpha
        return choice
        

    def negamax(self, stones, depth, alpha, beta, lastWho):
        if depth == 0:
            alpha = stones.blackVsWhite * (-1, 1)[lastWho]
        else:
            moves = list(stones.possibleMoves(not lastWho))
            if not moves:
                val = -self.negamax(stones, depth - 1, -beta, -alpha, not lastWho)
                if val >= beta:
                    alpha = val
                if val > alpha:
                    alpha = val
            else:
                for pos, reverses in moves:
                    stones.putStoneAndReverse(pos, not lastWho, reverses)
                    val = -self.negamax(stones, depth - 1, -beta, -alpha, not lastWho)
                    stones.removeStoneAndReverse(pos, not lastWho, reverses)
                    if val >= beta:
                        alpha = val
                        break
                    if val > alpha:
                        alpha = val
                
        return alpha
        
        