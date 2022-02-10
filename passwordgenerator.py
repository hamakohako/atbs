#!/usr/bin/env python
# title:    password generator
# author:   hko
# created:  2022-02-10

import random
import string
import argparse

# constants
UPPERC = string.ascii_uppercase
LOWERC = string.ascii_lowercase
DIGITS = string.digits
PUNC = string.punctuation
SYMBOLS = '!@#$%^&*-+'
DEFAULT = UPPERC+LOWERC+DIGITS+SYMBOLS
ALL = UPPERC+LOWERC+DIGITS+PUNC

# parser = argparse.ArgumentParser(description='Random password generator, by hko')
# parser.add_argument('length', help='Password length')
# parser.add_argument('count', '-c', type=int, help='Number of passwords to generate')

def generatePass(length, count, keys=DEFAULT):
    for i in range(count):
        password = []
        for char in range(length):
            password.append(random.choice(keys))
        password = ''.join(password)
        print(password)

def wizGeneratePass():
    while True:
        pwlength = input(f'Enter desired password length. Min: 6, Max: 4096. [32]: ')
        if pwlength.isdigit():
            if not (6 <= int(pwlength) <= 4096):
                print('Error [LENGTH]: minimum: 6, maximum: 4096, please try again. \n')
                continue
            else:
                pwlength = int(pwlength)
                break
        else:
            pwlength = 32
            print('Using default length: 32')
            break
    print(pwlength)
    while True:
        pwcount = input('How many passwords do you want to generate? Min: 1, Max: 1000. [5]: ')
        if pwcount.isdigit():
            if not (1 <= int(pwcount) <= 1000):
                print('Error [COUNT]: minimum: 1, maximum: 1000, please try again. \n')
                continue
            else:
                pwcount = int(pwcount)
                break
        else:
            pwcount = 5
            print('Using default count: 5')
            break
    print(pwcount)
    generatePass(pwlength, pwcount)

