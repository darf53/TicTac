from TicTac import *

import unittest

class TestBoard(unittest.TestCase):

    def test_board(self):
        self.assertEqual(print_board([["","",""],["","",""],["","",""]]), " | | \n-+-+-\n | | \n-+-+-\n | | \n", "Should be an empty TicTacToe board")

if __name__ == '__main__':
    unittest.main()