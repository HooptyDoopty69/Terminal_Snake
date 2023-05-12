from os import system
from colorama import Fore, init
from pytimedinput import timedKey
from random import randint

GAME_HEIGHT = 32
GAME_WIDTH = 16
board = [(col, row) for col in range(GAME_WIDTH)
         for row in range(GAME_HEIGHT)]
pressed_key = ''


###############
# SNAKE STUFF #
###############

snake_body = [(GAME_WIDTH//2, GAME_HEIGHT//2),
              (GAME_WIDTH//2 - 1, GAME_HEIGHT//2),
              (GAME_WIDTH//2 - 2, GAME_HEIGHT//2)]
directions = {
    'up':       (0, -1),
    'down':     (0, 1),
    'left':     (-1, 0),
    'right':    (1, 0)
}
move_dir = directions['right']


###############
# APPLE STUFF #
###############

valid_spawn_cells = []
apple_on_board = False
apple_pos = ()


def get_random_spawn_cell():
    random_x = []
    random_y = []

    for i in range(len(valid_spawn_cells)):
        if valid_spawn_cells[i][0] not in random_x:
            random_x.append(valid_spawn_cells[i][0])
        if valid_spawn_cells[i][1] not in random_y:
            random_y.append(valid_spawn_cells[i][1])

    return (random_x[randint(0, len(random_x) - 1)], random_y[randint(0, len(random_y) - 1)], )


####################
# GAME BOARD STUFF #
####################


def draw_game():
    global apple_pos, apple_on_board

    # Loops through every tuple in the board
    for cell in board:
        valid_spawn_cells.append(cell)

        if cell in snake_body:
            valid_spawn_cells.remove(cell)
            print(Fore.GREEN + 's', end='')
        elif cell == apple_pos:
            print(Fore.RED + 'a', end='')
        # If it's a last board, start a new line
        elif cell[1] == GAME_HEIGHT - 1:
            valid_spawn_cells.remove(cell)
            print('')
        # If it's a wall, print a # symbol
        elif cell[0] == 0 or cell[0] == GAME_WIDTH - 1 or cell[1] == 0 or cell[1] == GAME_HEIGHT - 2:
            valid_spawn_cells.remove(cell)
            print(Fore.YELLOW + '#', end='')
        # Othervise, add a whitespace
        else:
            print(' ', end='')

    if pressed_key == 'r':
        apple_on_board = False

    while apple_on_board == False:
        apple_pos = get_random_spawn_cell()
        apple_on_board = True
        if apple_on_board == True:
            break


#############
# GAME LOOP #
#############


def main():
    global pressed_key

    # Initialization
    init(autoreset=True)
    should_close = False

    while not should_close:
        # Get all current inputs
        # Reset the console on timeout
        # Only register accepted keys
        pressed_key, _ = timedKey(
            f'Q - quit\nWASD - Up/Left/Down/Right\nPressed key: {pressed_key}', timeout=0.3, resetOnInput=True, allowCharacters="qwasdr")

        # Stops the game loop if escape character is pressed
        if pressed_key == 'q':
            should_close = True
        # Redraws the screen on every timeout
        else:
            system("\033[H")
            draw_game()


if __name__ == "__main__":
    main()
