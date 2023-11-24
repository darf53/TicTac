from TicTac import *

import unittest

class TestBoard(unittest.TestCase):

    def test_board(self):
        self.assertEqual(print_board([["","",""],["","",""],["","",""]]), " | | \n-+-+-\n | | \n-+-+-\n | | \n", "Should be an empty TicTacToe board")

    def test_XwonVert(self):
        self.assertTrue(test_board([["X","",""],["X","O",""],["X","","O"]]))


if __name__ == '__main__':
    unittest.main()