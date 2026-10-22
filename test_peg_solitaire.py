import unittest
from board import Board


class TestPegSolitaire(unittest.TestCase):

    def setUp(self):
        # Initialize a standard board before each test
        self.board = Board()

    def test_initial_board_state(self):
        center = self.board.size // 2
        self.assertEqual(self.board.board[center][center], "EMPTY")
        self.assertEqual(self.board.board[center][center - 1], "PEG")
        self.assertEqual(self.board.board[center][center + 1], "PEG")
        self.assertEqual(self.board.board[center - 1][center], "PEG")
        self.assertEqual(self.board.board[center + 1][center], "PEG")

    def test_illegal_move(self):
        center = self.board.size // 2
        # Move with too large of a gap
        self.assertFalse(
            self.board.is_valid_move((center - 3, center), (center, center))
        )
        # Move with out of bounds initial position
        self.assertFalse(self.board.is_valid_move((-1, 0), (1, 0)))
        # Move with out of bounds final position
        self.assertFalse(self.board.is_valid_move((1, 0), (-1, 0)))


if __name__ == "__main__":
    unittest.main()
