import unittest
from .mock import Mock
from src.othello import ai
from src.othello.stones import stones


def StoneBuilder(pattern):
    stonesDict = {}
    available = []
    y = 0
    for line in pattern.splitlines():
        x = 0
        for c in line.strip():
            if c == '.':
                available.append((x, y))
            else:
                stonesDict[(x, y)] = int(c)
            x+=1
        y+=1
    stonesObj = stones(stonesDict)
    stonesObj.availablePositions = set(available)
    return stonesObj


class TestAi(unittest.TestCase):

    def testShouldPutAtValidPositionWhenGettingChanceToThink(self):
        a = ai()
        onPut = Mock()
        me = 1
        currentStones = stones({(0,0):me, (1,0):not me})
        a.registerPutEvent(onPut)
        a.think(currentStones, me)
        pos = onPut.call_args[0][0]
        self.assertTrue(currentStones.getReversePosistions(pos, me))

    def testShouldPutAtWinningPositionWhenHaving2Choices(self):
        a = ai()
        onPut = Mock()
        me = 1
        currentStones = StoneBuilder('''
        10.
        100.
        ''')
        a.registerPutEvent(onPut)
        a.think(currentStones, me)
        pos = onPut.call_args[0][0]
        self.assertTrue(currentStones.getReversePosistions(pos, me))


