import unittest
from board import Board


class TestBoardSize(unittest.TestCase):

    # Successful pick of a valid board size (5, 7, 9)
    def test_valid_board_size(self):

        # English
        for size in [5, 7, 9]:
            board1 = Board("English", size=size)
            self.assertEqual(
                board1.size, size, f"Board size should be 5, 7, or 9 (English)"
            )

        # Diamond
        for size in [5, 7, 9]:
            board2 = Board("Diamond", size=size)
            self.assertEqual(
                board2.size, size, f"Board size should be 5, 7, or 9 (Diamond)"
            )

        # Hexagon
        for size in [5, 7, 9]:
            board3 = Board("Hexagon", size=size)
            self.assertEqual(
                board3.size, size, f"Board size should be 5, 7, or 9 (Diamond)"
            )

    # Rejection fo an Even Board Size
    def test_invalid_board_size(self):
        # English
        board = Board("English", size=6)
        self.assertEqual(
            board.size, 7, "Even board size should be rejected and default to 7"
        )
        # Diamond
        board = Board("Diamond", size=6)
        self.assertEqual(
            board.size, 7, "Even board size should be rejected and default to 7"
        )
        # Hexagon
        board = Board("hexagon", size=6)
        self.assertEqual(
            board.size, 7, "Even board size should be rejected and default to 7"
        )


if __name__ == "__main__":
    unittest.main()
