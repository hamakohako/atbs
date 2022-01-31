#!/usr/bin/env python
from ast import Import
from distutils.command.build_ext import build_ext
import sys, random, time

try:
    import bext
except ImportError:
    print('please install bext module')
    print('pip install bext')
    sys.exit()

WIDTH, HEIGHT = bext.size()

WIDTH -= 1
NUMBER_OF_LOGOS = 5
PAUSE_AMOUNT = 0.2
COLORS = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
UP_RIGHT = 'ur'
UP_LEFT = 'ul'
DOWN_RIGHT = 'dr'
DOWN_LEFT = 'dl'
DIRECTIONS = (UP_RIGHT, UP_LEFT, DOWN_RIGHT, DOWN_LEFT)
COLOR = 'color'

X = 'x'
Y = 'y'
DIR = 'direction'

def main():
    bext.clear()

    logos = []
    for i in range(NUMBER_OF_LOGOS):
        logos.append({COLOR: random.choice(COLORS),
        X: random.randint(1, WIDTH - 4),
        Y: random.randint(1, HEIGHT -4),
        DIR: random.choice(DIRECTIONS)})
        if logos[-1][X] %2 == 1:
            logos[-1][X] -= 1

    cornerBounces = 0
    while True:
        for logo in logos:
            bext.goto(logo[X], logo[Y])
            originalDirection = logo[DIR]

            if logo[X] == 0 and logo[Y] == 0:
                logo[DIR] = DOWN_RIGHT
                cornerBounces += 1
            elif logo[X] == 0 and logo[Y] == HEIGHT - 1