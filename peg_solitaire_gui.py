import pygame
import os
import sys

import components

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
        SCREEN.blit(board_size_surface, board_type_surface.get_rect(center=(900, 300)))

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
                    print("Starting Game")  # TODO

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


if __name__ == "__main__":
    menu_screen()
