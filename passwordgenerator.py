#!/usr/bin/env python
# title:    password generator v0.1
# author:   hko
# created:  2022-02-10
# updated:  2022-02-11

import random
import string
import argparse

# constants
UPPERC = string.ascii_uppercase
LOWERC = string.ascii_lowercase
DIGITS = string.digits
PUNC = string.punctuation
SYMBOLS = '!@#$%^&*-+'

# key combinations
DEFAULT = UPPERC+LOWERC+DIGITS+SYMBOLS
ALL = UPPERC+LOWERC+DIGITS+PUNC

# argument parser
parser = argparse.ArgumentParser(description='Random password generator, by hko')
parser.add_argument('length', type=int, nargs='?', help='Password length', default=32)
parser.add_argument('count', type=int, nargs='?', help='Number of passwords to generate', default=5)
parser.add_argument('-b', choices=['yes', 'no'], help="Passwords must begin with a letter, default is yes", default='yes')
parser.add_argument('--wizard', '-w', action='store_true', help='Run the password generator wizard')
parser.add_argument('--allkeys', '-a', action='store_true', help='Use all possible characters, including special characters')
parser.add_argument('--output', '-o', nargs='?', help='Save passwords to file')
args = parser.parse_args()

# generate password function
def generatePass(length, count, keys=DEFAULT):
    for i in range(count):
        password = []
        for char in range(length):
            # begin password with letter, and not using only upper or lower (wizard)
            if args.b == 'yes' and char == 0 and (keys != UPPERC and keys != LOWERC):
                password.append(random.choice(string.ascii_letters))
            else:
                password.append(random.choice(keys))
        password = ''.join(password)
        # saving to file
        if args.output:
            with open(args.output, 'a') as file:
                file.write(password + '\n')
        # default, print passwords to stdout
        else:
            print(password)

# wizard, if using -w or --wizard option
def wizGeneratePass():
    # Length loop
    while True:
        pwlength = input(f'Enter desired password length. (6-4096) [default=32]: ')
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
    # Count loop
    while True:
        pwcount = input('How many passwords do you want to generate? (1-1000) [default=5]: ')
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
    # character sets loop
    while True:
        customize = input('Do you want to customize the character sets used ? (y/n): ')
        if customize.lower().startswith('y'):
            characters=''
            lowercase = input('Do you wnat to use lowercase letters? (y/n): ')
            if lowercase.lower().startswith('y'):
                characters += LOWERC
            uppercase = input('Do you want to use uppercase letters? (y/n): ')
            if uppercase.lower().startswith('y'):
                characters += UPPERC
            digits = input('Do you want to use numbers/digits (y/n): ')
            if digits.lower().startswith('y'):
                characters += DIGITS
            symbols = input('Do you want to use basic symbols or ALL special characters? (y/n/all): ')
            if symbols.lower().startswith('y'):
                characters += SYMBOLS
            elif symbols.lower().startswith('a'):
                characters += PUNC
            if characters == '':
                print('You have not selected any character sets. Please select at least one...')
                continue
            else:
                print(characters)
                break            
        else:
            characters=DEFAULT
            break
    # save to file loop
    while True:
        savetofile = input('Do you want to save the passwords to a file? (y/n): ')
        if savetofile.lower().startswith('y'):
            args.output = input('Please enter filename: ')
            if args.output:
                break
            else:
                print('Please enter a valid filename...')
                continue
        else:
            break
    generatePass(pwlength, pwcount, characters)

if args.wizard:
    wizGeneratePass()
else:
    if args.allkeys:
        generatePass(args.length, args.count, keys=ALL)
    else:
        generatePass(args.length, args.count)