from TicTac import *

import unittest

class TestBoard(unittest.TestCase):

    def test_board(self):
        self.assertEqual(print_board([["","",""],["","",""],["","",""]]), " | | \n-+-+-\n | | \n-+-+-\n | | \n", "Should be an empty TicTacToe board")

    def test_XwonVert(self):
        self.assertEqual(test_board([["X","",""],["X","O",""],["X","","O"]]), "Player X won!", "Should declare player X won the game")

    def test_OwonHoriz(self):
        self.assertEqual(test_board([["X","","X"],["O","O","O"],["X","",""]]), "Player O won!", "Should declare player O won the game")

    def test_XwonDiagonal(self):
        self.assertEqual(test_board([["X","",""],["O","X",""],["O","","X"]]), "Player X won!", "Should declare player X won the game with a diagonal line")

    def test_OwonDiagonal(self):
        self.assertEqual(test_board([["","","O"],["X","O",""],["O","","X"]]), "Player O won!", "Should declare player O won the game with a diagonal line")

    def test_BoardFullDraw(self):
        self.assertTrue(board_full([["X","O","X"],["O","O","X"],["X","X","O"]]), "Should declare a draw, no winner.")

    def test_BoardnotFull(self):
        self.assertFalse(board_full([["X","","X"],["O","O","X"],["X","X","O"]]), "Board not full yet")


if __name__ == '__main__':
    unittest.main()