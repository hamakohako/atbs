#!/usr/bin/env python
# author: hk0
# title: birthday paradox

import datetime, random

def getBirthdays(numberofbirthdays):
    # Generate random birthdays
    # initialize a list
    birthdays = []
    for i in range(numberofbirthdays):
        # reference day, start of year. Does not matter really, we are getting random day
        startOfYear = datetime.date(2001, 1, 1)
        # generate random number from 0 to 364, make it a delta datetime object
        randomday = datetime.timedelta((random.randint(0,364)))
        # add the randomday to the startofyear to get your random bday
        birthday = startOfYear + randomday
        # append each birthday object generated to the list
        birthdays.append(birthday)
    return birthdays

def getMatch(birthdays):
    # Checks the set of birthdays generated, if there is a match (not unique)
    # 'set' returns unique values in a list (de-duplicates).
    # so if len values are not same, it means there is duplicate in the set
    if len(birthdays) == len(set(birthdays)):
        return None # all bdays are unique
    # Check which birthdays are the same. enumerate assigns an iterable counter
    # which can be used to track easier
    for a, birthdayA in enumerate(birthdays):
        # compare birthdayA with next bday on list.
        # avoids unnecessary checks like comparison to self, and already compared
        for b, birthdayB in enumerate(birthdays[a + 1:]):
            if birthdayA == birthdayB:
                return birthdayA


def main():
    print('''Birthday Paradox, by Al Sweigart al@inventwithpython.com
The Birthday Paradox shows us that in a group of N people, the odds
that two of them have matching birthdays is surprisingly large.
This program does a Monte Carlo simulation (that is, repeated random
simulations) to explore this concept.
(It's not actually a paradox, it's just a surprising result.)
''')

    # Create a tuple, containing month names in order.
    MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

    # Get from user, the number of bdays to generate. Loop. Break out if valid,
    while True:
        response = input('How many bdays to generate? (Max 100): ')
        if response.isdecimal() and (0 < int(response) <= 100):
            numBdays = int(response)
            break
    
    print(f'getting {numBdays} birthdays...')
    birthdays  = getBirthdays(numBdays)

    # this is to detect if the iteration is first. 
    # For presentation only, used for the commas
    first = True
    for i in birthdays:
        if first:
            print(MONTHS[i.month - 1], i.day, end='')
            first = False
        # If not the first iteration, we are adding comma, before the values
        else:
            print(f', {MONTHS[i.month - 1]} {i.day}', end='')
    
    print()
    print()

    # check if there are 2 bdays that match
    match = getMatch(birthdays)
    print('IN this simulation')
    if match != None:
        print(f'multyiple people have same bday on {MONTHS[match.month]} {match.day}')
    else:
        print('no matching bdays')

    print()
    print()

    # Run through 100,000 simulations:
    print('Generating', numBdays, 'random birthdays 100,000 times...')
    input('Press Enter to begin...')
    print('Let\'s run another 100,000 simulations.')
    simMatch = 0
    # 100_000 = 100000. underscore just makes it easier to read large numbers
    for i in range(100_000):
        if i % 10_000 == 0:
            print(i, 'simulations run...')
        birthdays = getBirthdays(numBdays)
        if getMatch(birthdays) != None:
            simMatch += 1
    print('100,000 simulations done')

    # Display results
    # percentage formula, round off to 2 decimals
    probability = round(simMatch / 100_000 * 100, 2)
    print(f'Out of 100K sims of {numBdays} people, there was a')
    print(f'matching birthday in that group, {simMatch} times. This means')
    print(f'that, {numBdays} people have a {probability}% chance of')
    print('having a matching birthday in their group')
    print('bla bla bla')


if __name__ == '__main__':
    main()
