import pygame
import os
import sys

import components
import board

pygame.init()

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# Theme Paths
# Future Implementation

# Font Paths
FONT_PATH = os.path.join(SCRIPT_DIR, "PressStart2P-Regular.ttf")

# Create screen
SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Peg Solitaire - Menu")

# Load Themes

# Scale Background Images

# Fonts
font = pygame.font.Font(FONT_PATH, 40)
title_font = pygame.font.Font(FONT_PATH, 70)
small_font = pygame.font.Font(FONT_PATH, 20)


def menu_screen():
    clock = pygame.time.Clock()

    # Menu buttons
    play_button = components.MenuButton("PLAY", font, "White", "Yellow", (640, 300))
    close_button = components.MenuButton(
        "CLOSE GAME", font, "White", "Yellow", (640, 420)
    )

    while True:

        # Draw background
        SCREEN.fill((30, 30, 30))

        # Current Mouse Position
        mouse_pos = pygame.mouse.get_pos()

        # Title Text
        title_surface = title_font.render("PEG SOLITIARE", True, "White")
        title_rect = title_surface.get_rect(center=(640, 150))
        SCREEN.blit(title_surface, title_rect)

        # Draw buttons
        play_button.draw(SCREEN, mouse_pos)
        close_button.draw(SCREEN, mouse_pos)

        # Event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Check if the mouse click collided with the play button
                if play_button.check_click(event.pos):
                    options_screen()
                elif close_button.check_click(event.pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
        clock.tick(60)


def options_screen():
    clock = pygame.time.Clock()

    # Create settings buttons
    back_button = components.MenuButton("BACK", font, "White", "Yellow", (200, 600))
    start_game_button = components.MenuButton(
        "START", font, "White", "Yellow", (1080, 600)
    )

    # Track current selections
    selected_board_type = "English"
    selected_board_size = 7

    # Create buttons for board type
    board_type_buttons = [
        components.RadioButton(250, 380, 10, "English", "English", small_font),
        components.RadioButton(250, 440, 10, "Hexagon", "Hexagon", small_font),
        components.RadioButton(250, 500, 10, "Diamond", "Diamond", small_font),
    ]

    # Create buttons for board size
    board_size_buttons = [
        components.RadioButton(770, 380, 10, "Small (5x5)", 5, small_font),
        components.RadioButton(770, 440, 10, "Standard (7x7)", 7, small_font),
        components.RadioButton(770, 500, 10, "Large (9x9)", 9, small_font),
    ]

    while True:
        # Fill screen and mouse pos
        SCREEN.fill((30, 30, 30))
        mouse_pos = pygame.mouse.get_pos()

        # Draw curent settings title
        current_settings_surface = title_font.render("CURRENT SETTINGS", True, "White")
        SCREEN.blit(
            current_settings_surface,
            current_settings_surface.get_rect(center=(640, 150)),
        )

        # Board Type Title
        board_type_surface = font.render("BOARD TYPE", True, "White")
        SCREEN.blit(board_type_surface, board_type_surface.get_rect(center=(380, 300)))
        # Board Size Title
        board_size_surface = font.render("BOARD SIZE", True, "White")
        SCREEN.blit(board_size_surface, board_size_surface.get_rect(center=(900, 300)))

        # Draw Settings Radio Buttons
        for btn in board_type_buttons:
            btn.draw(SCREEN, selected_board_type)

        for btn in board_size_buttons:
            btn.draw(SCREEN, selected_board_size)

        # Draw Navigation Buttons
        back_button.draw(SCREEN, mouse_pos)
        start_game_button.draw(SCREEN, mouse_pos)

        # Event Loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:

                # Back Buttons
                if back_button.check_click(mouse_pos):
                    return  # Exit and go back to main screen

                # Star Game Button
                elif start_game_button.check_click(mouse_pos):
                    game_screen(selected_board_type, selected_board_size)

                # Check for clicks on board type buttons
                for btn in board_type_buttons:
                    if btn.check_click(event.pos):
                        selected_board_type = btn.value

                # Check for clicks onboard size buttons
                for btn in board_size_buttons:
                    if btn.check_click(event.pos):
                        selected_board_size = btn.value

        pygame.display.update()
        clock.tick(60)


def game_screen(board_type, size):
    clock = pygame.time.Clock()
    game_board = board.Board(board_type, size)
    selected_peg = None
    game_over_text = None

    # Back Button
    back_button = components.MenuButton(
        "BACK", small_font, "White", "Yellow", (100, 50)
    )
    # Play Again Button

    while True:
        SCREEN.fill((30, 30, 30))
        mouse_pos = pygame.mouse.get_pos()

        box_size = 500  # fixeed box size play area
        cell_size = box_size // size
        grid_width = size * cell_size
        grid_height = size * cell_size

        # Center grid on 1280x720 screen
        start_x = (1280 - grid_width) // 2
        start_y = (720 - grid_height) // 2

        # Check for win/loss each fram
        if game_over_text is None:
            if game_board.check_win():
                game_over_text = "YOU WON!"
            elif not game_board.game_over_check():
                game_over_text = "GAME OVER"

        # Determine title text based on state
        title_text = game_over_text if game_over_text else "PEG SOLITAIRE"

        # Title Text
        title_surface = title_font.render(title_text, True, "White")
        title_rect = title_surface.get_rect(center=(640, 50))
        SCREEN.blit(title_surface, title_rect)

        # Display Board Type Title
        mode_surface = small_font.render("BOARD TYPE:", True, "White")
        mode_rect = mode_surface.get_rect(center=(start_x // 2, 360))
        SCREEN.blit(mode_surface, mode_rect)

        # Display Board Value
        type_surface = small_font.render(f"{board_type}", True, "White")
        type_rect = type_surface.get_rect(center=(start_x // 2, 390))
        SCREEN.blit(type_surface, type_rect)

        # Display Board Size Title
        size_title_surface = small_font.render("BOARD SIZE:", True, "White")
        size_title_rect = size_title_surface.get_rect(center=(start_x // 2, 420))
        SCREEN.blit(size_title_surface, size_title_rect)

        # Display Board Size Value
        size_value_surface = small_font.render(f"{size}", True, "White")
        size_value_rect = size_value_surface.get_rect(center=(start_x // 2, 450))
        SCREEN.blit(size_value_surface, size_value_rect)

        # Draw Board Grid
        for row in range(size):
            for col in range(size):
                cell_type = game_board.board[row][col]

                # Box for each cell
                rect = pygame.Rect(
                    start_x + col * cell_size,
                    start_y + row * cell_size,
                    cell_size - 4,
                    cell_size - 4,
                )

                # Skip if an invalid corner space
                if cell_type == "INVALID":
                    continue
                # Draw Valid Pegs
                elif cell_type == "PEG":
                    # Selected Peg Color
                    if selected_peg == (row, col):
                        color = (255, 255, 0)
                    # Non Selected Peg Color
                    else:
                        color = (200, 200, 200)
                    # Set Color
                    pygame.draw.circle(SCREEN, color, rect.center, cell_size // 3)
                # Empty Placeholders
                elif cell_type == "EMPTY":
                    pygame.draw.circle(
                        SCREEN, (70, 70, 70), rect.center, cell_size // 4, 2
                    )

        # Draw the Navigation buttons
        back_button.draw(SCREEN, mouse_pos)

        # Event Loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # quit button
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:  # Button clicks
                # Back button
                if back_button.check_click(event.pos):
                    return

                # Grid click
                mouse_x, mouse_y = event.pos
                if (start_x <= mouse_x and mouse_x < start_x + grid_width) and (
                    start_y <= mouse_y and mouse_y < start_y + grid_height
                ):
                    # Find the clicked column
                    clicked_col = (mouse_x - start_x) // cell_size
                    clicked_row = (mouse_y - start_y) // cell_size

                    # Check to make sure clicked col and row are within the size
                    if (clicked_col >= 0 or clicked_col < size) and (
                        clicked_row >= 0 or clicked_row < size
                    ):
                        # Select our corresponding gui cell to logi
                        cell_value = game_board.board[clicked_row][clicked_col]

                        # Selection and De-selection
                        if cell_value == "PEG":
                            if selected_peg == (
                                clicked_row,
                                clicked_col,
                            ):  # re-selected, so should deselect
                                selected_peg = None
                            else:
                                selected_peg = (
                                    clicked_row,
                                    clicked_col,
                                )  # new peg, select it

                        # Making a move
                        elif cell_value == "EMPTY":
                            if game_board.make_move(
                                selected_peg, (clicked_row, clicked_col)
                            ):
                                selected_peg = None  # Deselect peg after move is made

                        else:
                            selected_peg = None  # reset on
        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    menu_screen()
