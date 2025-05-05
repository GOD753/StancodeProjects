"""
File: Steeplechase.py
Name: Anthony
---------------------------------
Anthony
"""

from karel.stanfordkarel import *


def main():
    """
    Karel crosses hurdles in a 12x12 world
    with a for loop 
    """
    for i in range(11):
        if front_is_clear():
            move()
        else:
            jump()


def jump():
    """
    Pre-condition: Karel is on the left side of the wall, facing east
    Post-condition: Karel is on the right side of the wall, facing east
    """
    up()
    cross()
    down()


def up():
    """
    Pre-condition: Karel is on the left side of the wall, facing east
    Post-condition: Karel is on the upper left of the wall, facing north
    """
    turn_left()
    while not right_is_clear():
        move()
    # alternative
    # while not front_is_clear():
    #     turn_left()
    #     move()
    #     turn_right()


def cross():
    """
    Pre-condition: Karel is on the upper left of the wall, facing north
    Post-condition: Karel is on the upper right of the wall, facing south
    """
    turn_right()
    move()
    turn_right()


def down():
    """
    Pre-condition: Karel is on the upper right of the wall, facing south
    Post-condition: Karel is on the left side of the wall, facing south
    """
    while front_is_clear():
        move()
    turn_left()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
