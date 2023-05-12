from os import system
from colorama import Fore, init
from pytimedinput import timedKey


GAME_WIDTH = 16
GAME_HEIGHT = 32


####################
# GAME BOARD STUFF #
####################
board = [(col, row) for col in range(GAME_WIDTH)
         for row in range(GAME_HEIGHT)]

wall_sign = Fore.YELLOW + '#'


def draw_board():
    for cell in board:
        if cell[1] == GAME_HEIGHT - 1:
            print('')
        elif cell[0] == 0 or cell[0] == GAME_WIDTH - 1 or cell[1] == 0 or cell[1] == GAME_HEIGHT - 2:
            print(wall_sign, end='')
        else:
            print(' ', end='')


##########################


#############
# GAME LOOP #
#############


def main():
    # Initialization
    init(autoreset=True)
    should_close = False
    pressed_key = ''

    while not should_close:
        # Get all current inputs
        # Reset the console on timeout
        # Only register accepted keys
        pressed_key, _ = timedKey(
            f'Q - quit\nWASD - Up/Left/Down/Right\nPressed key: {pressed_key}', timeout=0.3, resetOnInput=True, allowCharacters="qwasd")

        # Stops the game loop if escape character is pressed
        if pressed_key == 'q':
            should_close = True
        # Redraws the screen on every timeout
        else:
            system("\033[H")
            draw_board()


if __name__ == "__main__":
    main()
