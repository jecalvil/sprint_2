import unittest
from board import Board


# Helper funcitons
def make_custom_board(size, peg_positions, board_type="English"):
    """Creates a custom board of a certain side with defined positions, used
    to set up specific board situations"""

    # create the board
    game = Board(board_type, size)

    # actually make sure that the pegs asked for are valid and that they exist just in case
    for row, col in peg_positions:
        on_board = (
            row >= 0 and row < size and col >= 0 and col < size
        )  # within the space
        if not on_board or game.board[row][col] == "INVALID":
            raise ValueError(
                f"{(row, col)} is not a playable spot on {board_type} {size}"
            )

    # go through each position and if it is not marked as a specific peg then make it empty
    for row in range(size):
        for col in range(size):
            if game.board[row][col] == "INVALID":
                continue
            if (row, col) in peg_positions:
                game.board[row][col] = "PEG"
            else:
                game.board[row][col] = "EMPTY"
    return game


def count_cells(game, cell_value):
    """Count the number of game cells equal to either EMPTY, PEG, or INVALID"""
    total = 0
    for row in game.board:
        for cell in row:
            if cell == cell_value:
                total += 1
    return total


def count_playable_cells(game):
    """Playable cells are ones with a peg or empty hole"""
    return count_cells(game, "PEG") + count_cells(game, "EMPTY")


def make_board_with_peg_count(peg_count):
    """Makes English board size 9 with specific number of pegs, filling the first playable spots, top to bottom"""
    layout = Board("English", 9)
    positions = []
    for row in range(9):
        for col in range(9):
            if layout.board[row][col] != "INVALID" and len(positions) < peg_count:
                positions.append((row, col))
    return make_custom_board(9, positions)


# Story 1 - Choose board size ==================================
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

    # Rejection fo an Even Board Size - 6
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
        board = Board("Hexagon", size=6)
        self.assertEqual(
            board.size, 7, "Even board size should be rejected and default to 7"
        )

    # Rejection of other even board sizes, default to 7
    def test_other_even_sizes_rejected(self):
        for bad_size in [4, 8, 10]:
            self.assertFalse(Board.is_valid_size(bad_size), f"{bad_size} is even")
            self.assertEqual(Board("English", bad_size).size, 7)

    # Out of range (negative, small, 0, too large)
    def test_out_of_range_rejected(self):
        for bad_size in [3, 1, 0, -7, 11, 100]:
            self.assertFalse(Board.is_valid_size(bad_size), f"{bad_size} out of range")
            self.assertEqual(Board("English", bad_size).size, 7)

    # other symbols, decimals, and values
    def test_non_numeric_rejected(self):
        for bad_size in ["", " ", "abc", "#", "7.1", "-7", 7.1, None, True]:
            self.assertFalse(Board.is_valid_size(bad_size), f"{bad_size!r} not a size")
            self.assertEqual(Board("English", bad_size).size, 7)

    # I have radio buttons, so text doesn't matter, but added implementation to still work just in case
    # sizes typed as text should still work
    def test_valid_sizes_accepted_as_text(self):
        for text_size in ["5", "7", "9", " 7 "]:
            self.assertTrue(Board.is_valid_size(text_size))
            self.assertEqual(Board("English", text_size).size, int(text_size))

    # test unknown/unspecified board types
    def test_unknown_board_type_raises(self):
        with self.assertRaises(ValueError):
            Board("Triangle", 7)
            Board("Banana", 7)
            Board("Prism", 7)


# Story 3 - start a new game
class TestNewGame(unittest.TestCase):
    # 3.1, English 7 with 33 spots, 32 pegs and one mepty hole
    def test_english_7_counts(self):
        game = Board("English", 7)
        self.assertEqual(count_playable_cells(game), 33)
        self.assertEqual(count_cells(game, "PEG"), 32)
        self.assertEqual(count_cells(game, "EMPTY"), 1)

    # test other english sizes
    def test_english_other_sizes(self):
        sizes_and_cells = {5: 21, 9: 45}
        for size, expected_cells in sizes_and_cells.items():
            game = Board("English", size)
            self.assertEqual(
                count_playable_cells(game), expected_cells
            )  # peg plus hole
            self.assertEqual(
                count_cells(game, "PEG"), expected_cells - 1
            )  # -1 for the open space

    # 3.2 Creating game of a different board size and type (Diamond and hexagon for testing)
    def test_diamond_counts(self):
        sizes_and_cells = {5: 13, 7: 25, 9: 41}
        for size, expected_cells in sizes_and_cells.items():
            game = Board("Diamond", size)
            self.assertEqual(
                count_playable_cells(game), expected_cells
            )  # counts playable cells
            self.assertEqual(
                count_cells(game, "PEG"), expected_cells - 1
            )  # counts pegs
            self.assertEqual(
                count_cells(game, "EMPTY"), 1
            )  # counts empty (should just be 1 at start)

    def test_hexagon_counts(self):
        sizes_and_cells = {5: 21, 7: 37, 9: 57}
        for size, expected_cells in sizes_and_cells.items():
            game = Board("Hexagon", size)
            self.assertEqual(count_playable_cells(game), expected_cells)
            self.assertEqual(count_cells(game, "PEG"), expected_cells - 1)
            self.assertEqual(count_cells(game, "EMPTY"), 1)

    def test_center_only_empty(
        self,
    ):  # check and see center is empty for all possibilities
        for board_type in ["English", "Diamond", "Hexagon"]:
            for size in [5, 7, 9]:
                game = Board(board_type, size)
                center = size // 2
                self.assertEqual(game.board[center][center], "EMPTY")
                self.assertEqual(count_cells(game, "EMPTY"), 1)

    # 3.3 Rejecting ability to start new game of invalid board size (out of range   )


# =========== Run the tests=================
if __name__ == "__main__":
    unittest.main()
