# Imports.
from pyautogui import hotkey

from pydirectinput import keyDown, keyUp

from keyboard import is_pressed

from time import sleep

from random import choice


# Data.
operations = ['forward', 'backward', 'right', 'left', 'jump']

keys = {operations[0]: 'w', operations[1]: 's', operations[2]: 'd', operations[3]: 'a', operations[4]: 'space'}

switch_windows = ('alt', 'tab')

max_actions_per_interval = 30
interval = 10

hold_time = 2

running = True
paused = False

# Hold key function.
def hold(key, hold_time):
    keyDown(key)

    sleep(hold_time)

    keyUp(key)

# Start.
input('Press enter to start...')
print('Starting...')

sleep(3)

# Main.
while running:
    # Pause/unpause.
    if paused:
        if is_pressed('g'):
            paused = False

            print('Unpaused.')

    elif not paused:
        if is_pressed('g'):
            paused = True

            print('Paused.')

    # Actions that bot will do.
    actions = []

    # Fill action list with random actions.
    for _ in range(max_actions_per_interval): actions.append(choice(operations))

    # If not paused start performing actions.
    if not paused:
        for action in actions:
            print(f'Performing action: `{action}` (#1).')

            key = keys[action]

            if key == keys[operations[4]]:
                sleep(1)

            hold(key, hold_time)

            sleep(.30)

        sleep(1)

        hotkey(*switch_windows)

        for action in actions:
            print(f'Performing action: `{action}` (#2).')

            key = keys[action]

            if key == keys[operations[4]]:
                sleep(1)

            hold(key, hold_time)

            sleep(.30)

        # Log.
        print('Done all actions. Starting interval...')

        # Interval.
        sleep(interval)
