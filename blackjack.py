#!/usr/bin/env python

import random, sys

# card symbols
HEARTS   = chr(9829) # Character 9829 is '♥'.
DIAMONDS = chr(9830) # Character 9830 is '♦'.
SPADES   = chr(9824) # Character 9824 is '♠'.
CLUBS    = chr(9827) # Character 9827 is '♣'.

BACKSIDE = 'backside'

def main():
    print('''
    Blackjack
    Rules:
      Try to get as close to 21 without going over.
      Kings, Queens, and Jacks are worth 10 points.
      Aces are worth 1 or 11 points.
      Cards 2 through 10 are worth their face value.
      (H)it to take another card.
      (S)tand to stop taking cards.
      On your first play, you can (D)ouble down to increase your bet
      but must hit exactly one more time before standing.
      In case of a tie, the bet is returned to the player.
      The dealer stops hitting at 17.
    ''')
    money = 5000
    # main game loop
    while True:
        # quit if no money left
        if money <=0:
            print("you're broke! do not gamble")
            print('thanks for playing')
            sys.exit()
        print(f'Money: {money}')
        bet = getBet(money)
        # get new deck, give dealer and palyer 2 cards each from deck
        deck = getDeck()
        dealerHand = [deck.pop(), deck.pop()]
        playerHand = [deck.pop(), deck.pop()]
        print(f'Bet: {bet}')

        # Player actions:
        # Loop until player stands or busts
        while True:
            displayHands(playerHand, dealerHand, False)
            print()
            # busted, break this loop. get new bet
            if getHandValue(playerHand) > 21:
                break
            # get players move:
            move = getMove(playerHand, money - bet)
            # Double down move. max is your current bet, or remaining money (if lower)
            if move == 'd':            
                additionalBet = getBet(min(bet, (money - bet)))
                bet += additionalBet
                print(f'Bet increased to {bet}')
                print(f'Bet: {bet}')
            # hit or double, draws a card
            if move in ['h', 'd']:
                newCard = deck.pop()
                rank, suit = newCard
                print(f'You drew a {rank} of {suit}')
                playerHand.append(newCard)
                # busted. get new bet. Money not returned
                if getHandValue(playerHand) > 21:
                    continue
            # stand or hit, ends players turn
            if move in ['s', 'd']:
                break

            # Dealer actions
        if getHandValue(dealerHand) <= 21:
            while getHandValue(dealerHand) < 17:
                print('dealer hits...')
                dealerHand.append(deck.pop())
                displayHands(playerHand, dealerHand, False)
                if getHandValue(dealerHand) > 21:
                    break
                input('Press enter to continue... ')
                print('\n\n')

        displayHands(playerHand, dealerHand, True)
        playerValue = getHandValue(playerHand)
        dealerValue = getHandValue(dealerHand)

        if dealerValue > 21:
            print(f'Dealer busts. You win {bet}')
            money += bet
        elif (playerValue > 21) or (playerValue < dealerValue):
            print(f'You lost {bet}')
            money -= bet
        elif playerValue > dealerValue:
            print(f'you won {bet}')
            money += bet
        elif playerValue == dealerValue:
            print("it's a tie, bet returned")
        input('Press enter to continue... ')
        print('\n\n')       

def getBet(maxBet):
    # ask player how much they want to bet
    # keep asking valid amount, integer or q/quit
    while True:
        bet = input(f'how much do you want to bet ? min=1, max={maxBet}, or (Q)uit: ')
        # if bet is string, and if q/quit
        if isinstance(bet, str) and bet.lower() in ['q', 'quit']:
            print('Quitting... Thanks for playing!')
            sys.exit()
        # if bet is string, 'not' will make it true therefore 'continue'
        #  skips rest of code of current loop 
        if not bet.isdecimal():
            continue
        bet = int(bet)
        if 1 <= bet <= maxBet:
            return bet

def getDeck():
    # generate deck
    deck = []
    for suit in (HEARTS, SPADES, DIAMONDS, CLUBS):
        for rank in range(2, 11):
            # for each symbol/suit, add numbered cards. append tuple
            deck.append((str(rank), suit))
        for rank in ('J', 'Q', 'K', 'A'):
            # for each symbol/suit, add face/ace cards. append tuple
            deck.append((rank, suit))    
    random.shuffle(deck)
    return deck

def displayHands(playerHand, dealerHand, showDealerHand=False):
    # show player and dealer card.
    # hide dealerhand by default
    print()
    if showDealerHand:
        # print score value of dealer hands
        print(f'DEALER: {getHandValue(dealerHand)}')
        displayCards(dealerHand)
    else:
        print('DEALER: ???')
        # hides dealers first card. 
        displayCards([BACKSIDE] + dealerHand[1:])
    print(f'PLAYER: {getHandValue(playerHand)}')
    displayCards(playerHand)

def getHandValue(cards):
    # returns value of cards, face=10, ace=11/1
    value = 0
    numberOfAces = 0
    for card in cards:
        # each card is a tuple (rank, suit)
        rank = card[0]
        # Ace will be counted for use later (will pick best value 1 or 11)
        if rank == 'A':
            numberOfAces += 1
        # face cards = 10
        elif rank in ('K', 'Q', 'J'):
            value += 10
        # all other numbered cards, worth their number
        else:
            value += int(rank)
    # add 1 value for each ace
    value += numberOfAces
    # adds 10 if current total value less than 21
    for i in range(numberOfAces):
        if value + 10 <= 21:
            value += 10
    return value

def displayCards(cards):
    rows = ['', '', '', '', '']
    for i, card in enumerate(cards):
        rows[0] += ' ___  '
        if card == BACKSIDE:
            rows[1] += '|## | '
            rows[2] += '|###| '
            rows[3] += '|_##| '
        else:
            # eahc card is a tuple
            rank, suit = card
            # format is to align/justify presentation of cards/lines/spaces
            rows[1] += '|{} | '.format(rank.ljust(2))
            rows[2] += '| {} | '.format(suit)
            rows[3] += '|_{}| '.format(rank.rjust(2, '_'))
    for row in rows:
        print(row)

def getMove(playerHand, money):
    # ask players move. H, S, D for hit, stand and double down respectively
    # keep looping til player provides valid value
    while True:
        moves = ['(H)it', '(S)tand']
        # add Double down on first move. indicated by having exactly 2 cards (did not hit yet)
        if len(playerHand) == 2 and money > 0:
            moves.append('(D)ouble down')
        # present list of available moves, separated by , and space
        move = input(f"{', '.join(moves).upper()} > ")
        if move.lower() in ('h', 's'):
            return move.lower()
        if '(D)ouble down' in moves and move.lower() in ['d']:
            return move.lower()

if __name__ == '__main__':
    main()