Peg Solitaire (Sprint 2)

A Peg Solitaire game written in Python with pygame.

Features (Sprint 2)
Choose a board type (English, Hexagon, or Diamond) and a size (5, 7, or 9)
Start a new game with every hole filled except the center
Click a peg to select it. It turns yellow and the holes it can jump to get a green ring. Click one of those holes to make the jump
Click the selected peg again to deselect it, or click a different peg to switch
Jumps can be orthogonal or diagonal on every board, since that's what the project description says
Illegal clicks show a short message instead of doing anything
The game ends when no jumps are left or only one peg remains, then shows a rating: Outstanding (1 peg left), Very Good (2), Good (3), or Average (4 or more)
RESTART starts a fresh board of the same type and size (essentially the "Play Again" feature), and BACK returns to the previous screen
Running it

You need Python 3 and pygame:

pip install pygame
python peg_solitaire_gui.py

Keep PressStart2P-Regular.ttf in the same folder as the script, because the game loads its font from there.

Running the tests
python -m unittest test_peg_solitaire -v

The tests only cover board.py, so they don't need pygame.

Files
board.py: all the game logic (building each board type, checking and making moves, game over, rating). Nothing in it touches pygame.
peg_solitaire_gui.py: the pygame screens (main menu, options, and the game itself).
components.py: the button classes the GUI uses.
test_peg_solitaire.py: unit tests for board.py.
PressStart2P-Regular.ttf: the font.
docs/: sprint write-ups and user stories.
