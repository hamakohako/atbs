#!/usr/bin/env python
import random

def headsOrTails():
    if random.randint(0, 1) == 1:
        return 'heads'
    else:
        return 'tails'

while True:
    start = input('press enter to flip, number of flips, or (Q)uit: ')
    if start.lower() in ['q', 'quit']:
        print('Thanks for playing...')
        break
    elif start.isdigit():
        headcount = 0
        tailcount = 0
        for i in range(int(start)):
            flip = headsOrTails()
            if flip == 'heads':
                headcount += 1
            else:
                tailcount += 1
        print(f'HEADS: {headcount}')
        print(f'TAILS: {tailcount}')
    else:
        print(headsOrTails().upper())