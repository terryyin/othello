import unittest
from src.othello.stones import stones

class TestStones(unittest.TestCase):
    
    def testShouldRevertTheStones(self):
        s = stones({(0,0):1, (0,1):0})
        self.assertTrue(s.put((0, 2), 1))
        self.assertEqual(1, s.stones[(0, 2)])
        self.assertEqual(1, s.stones[(0, 1)])
        
    def testShouldNotAllowToPutWhenThereIsOnlyEmptyNeighbors(self):
        s = stones({(0,0):1})
        self.assertFalse(s.put((0, 2), 1))
        self.assertNotIn((0, 2), s.stones)
        self.assertNotIn((0, 1), s.stones)
        
        