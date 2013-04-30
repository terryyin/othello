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
            elif c != ' ':
                stonesDict[(x, y)] = int(c)
            x+=1
        y+=1
    stonesObj = stones(stonesDict)
    stonesObj.availablePositions = set(available)
    return stonesObj


me = 1
class TestAi(unittest.TestCase):
    
    def setUp(self):
        self.ai = ai()
        self.onPut = Mock()
        self.ai.registerPutEvent(self.onPut)


    def putPos(self):
        return self.onPut.call_args[0][0]

    def testShouldPutAtValidPositionWhenGettingChanceToThink(self):
        currentStones = stones({(0,0):me, (1,0):not me})
        self.ai.think(currentStones, me)
        self.assertTrue(currentStones.getReversePosistions(self.putPos(), me))

    def testShouldPutAtWinningPositionWhenHaving2Choices(self):
        self.ai.depth = 0
        currentStones = StoneBuilder(
            '''100.
            
               10.
        ''')
        self.ai.think(currentStones, me)
        self.assertEqual((3, 0), self.putPos())

    def testShouldPutAtWinningPositionForDepthN(self):
        self.ai.depth = 3
        currentStones = StoneBuilder(
            '''10.
        ''')
        self.ai.think(currentStones, me)
        self.assertEqual(4, self.ai.minWin)

    def testShouldWorkForWhiteToo(self):
        self.ai.depth = 3
        currentStones = StoneBuilder(
            '''01.
        ''')
        self.ai.think(currentStones, 0)
        self.assertEqual(4, self.ai.minWin)

    def testShouldReturnNextLevelWhenNoMoveInCurrentLevel(self):
        currentStones = StoneBuilder(
            '''01.        ''')
        val = self.ai.negamax(currentStones, 1, -100, 100, 0)
        self.assertEqual(0, val)

    def testShouldReturnMoreLevelsWhenNoMoveInCurrentLevel(self):
        currentStones = StoneBuilder(
            '''01.        ''')
        val = self.ai.negamax(currentStones, 2, -100, 100, 0)
        self.assertEqual(4, val)

    def testCornerShouldGetMoreScores(self):
        self.ai.depth = 3
        currentStones = StoneBuilder(
            '''.01
               
               . 01.''')
        self.ai.makeChoice(currentStones, 0)
        self.assertEqual(-4, self.ai.minWin)

