import unittest
from mock import Mock, call
from src.othello import game

class Test(unittest.TestCase):
    
    def setUp(self):
        self.board = Mock()
        self.human = Mock()
        self.ai = Mock()
        self.g = game(self.board, self.human, self.ai).start()
    def testGameRegisterEvent(self):
        self.human.registerPutEvent.assert_called_with(self.g.onPutWhite)
        self.ai.registerPutEvent.assert_called_with(self.g.onPutBlack)
        self.board.eventLoop.assert_called_with()

    def testGamePutWillDrawOnBoard(self):
        self.g.onPutWhite((1, 2))
        self.board.drawWhite.assert_called_with((1, 2))

    def testGamePutBlackWillDrawOnBoard(self):
        self.g.onPutBlack((1, 2))
        self.board.drawBlack.assert_called_with((1, 2))

    def testWhenStartPutThe4Stones(self):
        self.board.drawWhite.assert_has_calls([call((3,3)), call((4,4))], any_order = True)
        self.board.drawBlack.assert_has_calls([call((3,4)), call((4,3))], any_order = True)

    def testWhenStartBlackGotChanceToThink(self):
        self.ai.think.assert_called_with()

    def testWhenBlackPutsTheWhiteGotChanceToThink(self):
        self.human.reset_mock()
        self.g.onPutBlack((2, 3))
        self.human.think.assert_called_with()

    def testWhenWhitePutsTheBlackGotChanceToThink(self):
        self.ai.reset_mock()
        self.g.onPutWhite((3, 5))
        self.ai.think.assert_called_with()

    def testCanNotPutOnTakenCell(self):
        self.ai.reset_mock()
        self.g.onPutWhite((3, 3))
        self.assertEqual(1, self.ai.think.call_count)

