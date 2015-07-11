__author__ = 'user'

import pygame
from pygame.locals import *
pygame.init()


controls = {
    "ACCEPT": K_z,
    "CANCEL": K_x,
    "START": K_RETURN,
    "SELECT": K_BACKSPACE,
    "UP": K_UP,
    "DOWN": K_DOWN,
    "LEFT": K_LEFT,
    "RIGHT": K_RIGHT
}

system = {
    "MUTE": K_m,
    "=": K_EQUALS,
    "K+": K_KP_PLUS,
    "-": K_MINUS,
    "K-": K_KP_MINUS,
    "ESCAPE": K_ESCAPE
}

directions = {
    "NONE": (0, 0),
    "UP": (0, -1),
    "DOWN": (0, 1),
    "LEFT": (-1, 0),
    "RIGHT": (1, 0),
    "UP_LEFT": (-1, -1),
    "UP_RIGHT": (1, -1),
    "DOWN_LEFT": (-1, 1),
    "DOWN_RIGHT": (1, 1)
}


def start(event):
    """
    Whether or not return was pressed
    """
    return event.type == KEYDOWN and event.key == system["ENTER"]


def escape_prompt(event, gameover=False):
    """
    True if escape or red x is pressed, also true if n is pressed during a continue prompt
    """
    red_x_pressed = event.type == QUIT
    escape_pressed = event.type == KEYDOWN and event.key == system["ESCAPE"]
    #negative_answer = event.type == KEYDOWN and event.key == question["NO"]

    if not gameover:
        return red_x_pressed or escape_pressed
    else:
        pass
     #return red_x_pressed or escape_pressed or negative_answer


def music_prompt(keys):
    """
    Returns true if 'm' was pressed
    """
    return keys[system["MUTE"]]


def increase_prompt(keys):
    """
    Returns true if keypad '+' or '=' was pressed
    """
    return keys[system["K+"]] or keys[system["="]]


def decrease_prompt(keys):
    """
    Returns true if '-' or keypad '-' was pressed
    """
    return keys[system["-"]] or keys[system["K-"]]


def movement(keys):
    """
     Returns direction as a tuple based on arrow keys
    """
    up = keys[controls["UP"]]
    left = keys[controls["LEFT"]]
    right = keys[controls["RIGHT"]]
    down = keys[controls["DOWN"]]
    direction = directions["NONE"]
    for d in controls:
        if keys[controls[d]]:
            direction = directions[d]
    #Diagonals
    if up and left:
        direction = directions["UP_LEFT"]
    if up and right:
        direction = directions["UP_RIGHT"]
    if down and left:
        direction = directions["DOWN_LEFT"]
    if down and right:
        direction = directions["DOWN_RIGHT"]

    return direction
