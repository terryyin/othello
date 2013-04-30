import unittest
from src.othello.stones import stones

class TestStones(unittest.TestCase):
    
    def testShouldCountBlackForBlackVsWhite(self):
        s = stones({(0,0):1})
        self.assertEqual(1, s.blackVsWhite)

    def testShouldCountWhiteForBlackVsWhite(self):
        s = stones({(0,0):0})
        self.assertEqual(-1, s.blackVsWhite)

    def testShouldRevertTheStones(self):
        s = stones({(0,0):1, (0,1):0})
        self.assertTrue(s.put((0, 2), 1))
        self.assertEqual(1, s.stones[(0, 2)])
        self.assertEqual(1, s.stones[(0, 1)])
        self.assertEqual(4, s.blackVsWhite)
        
    def testShouldNotAllowToPutWhenThereIsOnlyEmptyNeighbors(self):
        s = stones({(0,0):1})
        self.assertFalse(s.put((0, 2), 1))
        self.assertNotIn((0, 2), s.stones)
        self.assertNotIn((0, 1), s.stones)
        
    def testShouldNotAllowToPutWhenThereIsOnlyBuddyAndEmptyNeighbors(self):
        s = stones({(0,0):1, (0,1):1})
        self.assertFalse(s.put((0, 2), 1))
        self.assertNotIn((0, 2), s.stones)
        
    def testShouldNotAllowToPutWhenThereIsNoBuddyOnTheOtherSide(self):
        s = stones({(0,0):0, (0,1):0})
        self.assertFalse(s.put((0, 2), 1))
        self.assertNotIn((0, 2), s.stones)
        
    def testShouldWorkWithAllDirections(self):
        s = stones({(0,0):0, (0,2):0, (0,4):0,
                    (1, 1):1, (1,2):1,(1,3):1,
                    (2,0):0, (2, 1):1, (2, 3):1, (2,4):0,
                    (3, 1):1, (3, 2):1, (3, 3):1,
                    (4, 0):0, (4, 2):0, (4, 4):0})
        self.assertTrue(s.put((2, 2), 0))
        self.assertEqual(0, s.stones[(1, 1)])
        self.assertEqual(0, s.stones[(1, 2)])
        self.assertEqual(0, s.stones[(1, 3)])
        self.assertEqual(0, s.stones[(2, 1)])
        self.assertEqual(0, s.stones[(2, 3)])
        self.assertEqual(0, s.stones[(3, 1)])
        self.assertEqual(0, s.stones[(3, 2)])
        self.assertEqual(0, s.stones[(3, 3)])
                