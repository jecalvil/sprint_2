class Board:
    def __init__(self, board_type="English", size=7):  # English and size 7 default
        self.board_type = board_type
        self.size = size

        # create a board as 2D array, with size as dimensions
        self.board = []
        for row in range(size):
            row_list = []  # create a row
            for col in range(size):  # fill out the columns for that row
                if self.board_type == "English" and self.is_english_corner(row, col):
                    row_list.append("INVALID")
                elif self.board_type == "Diamond" and self.is_diamond_corner(row, col):
                    row_list.append("INVALID")
                elif self.board_type == "Hexagon" and self.is_hexagon_corner(row, col):
                    row_list.append("INVALID")
                else:
                    row_list.append("PEG")
            # add new row array into board, making it 2D
            self.board.append(row_list)

        # make the center empty (sizes are 5, 7, and 9)
        center_pos = size // 2
        self.board[center_pos][center_pos] = "EMPTY"

    def is_english_corner(self, row, col):
        corner_depth = (self.size - 3) // 2

        # check to see if a position is part of the corner boundary
        is_corner_row = (row < corner_depth) or (row >= self.size - corner_depth)
        is_corner_col = (col < corner_depth) or (col >= self.size - corner_depth)

        # return whether the position is determined to be an invalid position (corner)
        return is_corner_row and is_corner_col

    def is_diamond_corner(self, row, col):
        center = self.size // 2
        # if the combined row and colum exceeds the center radius
        return abs(row - center) + abs(col - center) > center

    def is_hexagon_corner(self, row, col):
        corner_depth = (self.size - 3) // 2

        # Mark out the corners
        top_left = (row + col) < corner_depth
        top_right = row + (self.size - 1 - col) < corner_depth
        bottom_left = ((self.size - 1 - row) + col) < corner_depth
        bottom_right = ((self.size - 1 - row) + (self.size - 1 - col)) < corner_depth

        return top_left or top_right or bottom_left or bottom_right

    def is_valid_move(self, start_pos, end_pos):  # pos parameters are tuples
        # unpack coordinates
        r1, c1 = start_pos
        r2, c2 = end_pos

        # check to see whether positions are within the bounds
        if (
            (r1 >= self.size or r1 < 0)
            or (c1 >= self.size or c1 < 0)
            or (r2 >= self.size or r2 < 0)
            or (c2 >= self.size or c2 < 0)
        ):
            return False

        # check if selected position contains peg and destination is empty
        if self.board[r1][c1] != "PEG" or self.board[r2][c2] != "EMPTY":
            return False

        # check their distance, must be exactly a distance of 2 spaces
        row_diff = r2 - r1
        col_diff = c2 - c1

        # valid horizontal, row stays the same (0 distance), while column difference is 2
        is_horizontal = row_diff == 0 and abs(col_diff) == 2
        # valid vertical, row difference is 2, while row distance is the same (0 distance)
        is_vertical = col_diff == 0 and abs(row_diff) == 2

        # if neither are met then return false
        if not (is_vertical or is_horizontal):
            return False

        # check if jumped over position contains peg
        mid_r = r1 + row_diff // 2
        mid_c = c1 + col_diff // 2

        # returns true if it conatins peg, false otherwise
        return self.board[mid_r][mid_c] == "PEG"

    def make_move(self, start_pos, end_pos):
        # Check for valid move
        if not self.is_valid_move(start_pos, end_pos):
            return False

        # Unpack coordinates
        r1, c1 = start_pos
        r2, c2 = end_pos

        # Find peg that is being jumped over
        target_pos_r = r1 + ((r2 - r1) // 2)
        target_pos_c = c1 + ((c2 - c1) // 2)

        # === Update Board ===
        # Change starting position to empty
        self.board[r1][c1] = "EMPTY"
        # Change middle position to empty
        self.board[target_pos_r][target_pos_c] = "EMPTY"
        # Change destination to Peg
        self.board[r2][c2] = "PEG"

        return True

    def game_over_check(self):
        # Go through each position, if there is a peg, check if there is a valid move
        for row in range(self.size):
            for col in range(self.size):
                current_value = self.board[row][col]
                current_pos = (row, col)
                # if it has a peg, check for a valid move
                if current_value == "PEG":
                    if (
                        self.is_valid_move((current_pos), (row - 2, col))  # down
                        or self.is_valid_move((current_pos), (row + 2, col))  # up
                        or self.is_valid_move((current_pos), (row, col - 2))  # left
                        or self.is_valid_move((current_pos), (row, col + 2))  # right
                    ):
                        return True
        return False

    def check_win(self):
        # Count the total number of pegs currently on the board
        peg_count = 0
        for row in range(self.size):
            for col in range(self.size):
                if self.board[row][col] == "PEG":
                    peg_count += 1

        # A win is achieved when exactly 1 peg remains
        return peg_count == 1
