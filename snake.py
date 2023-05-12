from os import system
from colorama import Fore, init
from pytimedinput import timedKey



####################
# GAME BOARD STUFF #
####################




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
        pressed_key, _ = timedKey(f'Q - quit\nWASD - Up/Left/Down/Right\nPressed key: {pressed_key}', timeout=0.3, resetOnInput=True, allowCharacters="qwasd")
        
        # Stops the game loop if escape character is pressed
        if pressed_key == 'q':
            should_close = True
        # Redraws the screen on every timeout
        else:
            system("\033[H")
            print('hello')

if __name__ == "__main__":
    main()