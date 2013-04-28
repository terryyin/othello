import unittest
from .mock import Mock
from src.othello import game

class TestGameInitialization(unittest.TestCase):
    
    def setUp(self):
        self.board = Mock()
        self.white = Mock()
        self.black = Mock()
        self.g = game(self.board, self.white, self.black).start()

    def testGameRegisterEvent(self):
        self.white.registerPutEvent.assert_called_with(self.g.onPutWhite)
        self.black.registerPutEvent.assert_called_with(self.g.onPutBlack)
        self.board.eventLoop.assert_called_with()

    def testWhenStartPutThe4Stones(self):
        stones = self.board.drawStones.call_args[0][0]
        self.assertTrue(stones[(3, 3)])
        self.assertTrue(stones[(4, 4)])
        self.assertFalse(stones[(4, 3)])
        self.assertFalse(stones[(3, 4)])

    def testWhenStartBlackGotChanceToThink(self):
        self.black.think.assert_called_with(self.g.stones, 1)

class TestGame(unittest.TestCase):
        
    def setUp(self):
        self.board = Mock()
        self.white = Mock()
        self.black = Mock()
        self.g = game(self.board, self.white, self.black).start()
        self.white.reset_mock()
        self.black.reset_mock()
        self.board.reset_mock()

    def testWhenBlackPutsTheWhiteGotChanceToThink(self):
        self.g.onPutBlack((3, 5))
        stones = self.board.drawStones.call_args[0][0]
        self.assertTrue(stones[(3, 5)])
        self.white.think.assert_called_with(self.g.stones, 0)

    def testCanNotPutOnTakenCell(self):
        self.g.onPutWhite((3, 3))
        self.white.deny.assert_called_with()
        self.assertEqual(0, self.black.think.call_count)


