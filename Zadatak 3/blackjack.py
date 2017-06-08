import sys
import numpy as np
import random

SUITS = ['Clubs', 'Spades', 'Hearts', 'Diamonds']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']


def cmp(a, b) :
    if(a > b) :
        return 1
    elif(b > a) :
        return -1
    else :
        return 0

player = 0
dealer = 0

cards = list()

for i in range(2,12):
    for j in range(0,3):
        cards.append(i)

np.random.shuffle(cards)
NUMBER_OF_CARDS = len(cards)

def game_play(i):
    global NUMBER_OF_CARDS
    options = [0]
    if NUMBER_OF_CARDS - 1 < 4:
        print("Not enough cards")
        return 0
    for p in range(2 , NUMBER_OF_CARDS - i - 2):
        player = cards[i] + cards[i+2] + sum(cards[i+4:i+p+2])
        if player > 21:
            print("Player is bust")
            options.append(-1 + game_play(i+p+2))
            break
        for d in range(2 , NUMBER_OF_CARDS-i-p):
            dealer = cards[i+1] + cards[i+3] + sum(cards[i+p+2:i+p+d])
            if dealer >= 17:
                break
        if dealer > 21:
            print("Dealer bust")
            dealer = 0

        print("End of hand")
        print("Player = ", player, " : Dealer = ", dealer)
        #NUMBER_OF_CARDS -= cards_drawn
        options.append(cmp(player ,dealer) + game_play(i+p+d))
    return max(options)

print("Money to be won: " , game_play(0))


