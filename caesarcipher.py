#!/usr/bin/env python

try:
    import pyperclip
except ImportError:
    print('pyperclip not installed')

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890!@#$%^&*()abcdefghijklmnopqrstuvwxyz'
print('''
Caesar Cipher
The Caesar cipher encrypts letters by shifting them over by a
key number. For example, a key of 2 means the letter A is
encrypted into C, the letter B encrypted into D, and so on.
''')

# Ask mode loop
while True:
    response = input('Do you want to (e)ncrypt or (d)ecrypt ? ').lower()
    if response.startswith('e'):
        mode = 'encrypt'
        break
    if response.startswith('d'):
        mode = 'decrypt'
        break

# Ask key (how many keys to shift) loop
while True:
    # minus 1 (self)
    maxKey = len(SYMBOLS) - 1
    response = input(f'How many keys to use ? (0 to {maxKey}) ')
    if not response.isdecimal():
        continue
    if 0 <= int(response) < len(SYMBOLS):
        key = int(response)
        break

message = input(f'Enter the message to {mode}: ')

translated = ''

for symbol in message:
    if symbol in SYMBOLS:
        # find index of each character in the message.
        num = SYMBOLS.find(symbol)
        if mode == 'encrypt':
            # shift by adding key
            num = num + key
        elif mode == 'decrypt':
            # opssite of encryptm shift back by decreasing key
            num = num - key
        
        # for wrap around. if num goes over length of SYMBOLS
        # or less than 0, for decrypt.
        if num >= len(SYMBOLS):
            num = num - len(SYMBOLS)
        elif num < 0:
            num = num + len(SYMBOLS)
        
        # for all other characters, not in SYMBOLS. no encrpytion
        translated = translated + SYMBOLS[num]

    else:
        translated = translated + symbol

print(translated)

try:
    pyperclip.copy(translated)
    print(f'{mode}ed text copied to clipboard')
except:
    print('piper clep feyld')
    pass


