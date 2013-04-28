import unittest
from .mock import Mock
from src.othello import ai
from src.othello.stones import stones

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


