#!/usr/bin/env python
# author: hk0

# Bagels game, by Al Sweigart

import random
from tokenize import Number

DIGITS = 3
MAX_GUESS = 10


def main():
    # Main function
    print('''
    Bagels game, by Al Sweigart
    
    I am thinking of a 3-digit number. Try to guess what it is.
    Here are some clues:
    When I say:    That means:
    Pico         One digit is correct but in the wrong position.
    Fermi        One digit is correct and in the right position.
    Bagels       No digit is correct.
  '''
          )
    NumberList = secretNum()
    print('I have thought up a number.', end='')
    print(f' You have {MAX_GUESS} guesses to get it \n {"*" * 10}')
    
    guesses = 1
    while guesses <= MAX_GUESS:
        answer = ''
        while len(answer) != DIGITS:
            print(f'You have {MAX_GUESS - guesses + 1} guess/es left \n {"*" * (MAX_GUESS - guesses + 1)}')
            answer = list(input('Is it: '))
            # print(answer)
            # print(NumberList)
        guesses += 1

        if answer == NumberList:
            print('You got it ! ! !')
            break
        else:
            checkAnswer(answer, NumberList)
    print(f'Noob! The answer was {"".join(NumberList)}')

def checkAnswer(answer, NumberList):
    clues = []

    for i in range(len(answer)):
        if answer[i] == NumberList[i]:
            clues.append('Fermi')
        elif answer[i] in NumberList:
            clues.append('Pico')
    if len(clues) == 0:
        clues.append('Bagels')
    print(', '.join(clues))
    
        



def secretNum():
    # Create secret number
    secret = []
    for i in range(DIGITS):
        secret.append(str(random.randrange(10)))
    return secret


if __name__ == '__main__':
    gameon = 1
    while gameon != 0:
        main()
        gameon = 2
        while gameon == 2:
            play = input('Do you want to play again ? (y / n): ')
            if play.lower() in ['n', 'no']:
                print('thanks for playing')
                gameon = 0
            elif play.lower() in ['y', 'ye', 'yes']:
                gameon = 1
            else:
                print('stupid shit. y / n !')
                gameon = 2