#blackjack
from random import shuffle


#cards



def new_deck():
    values = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']
    suits = ['diamonds', 'spades', 'hearts', 'clubs']
    a_new_deck = []
    for i in range(len(values)):
        for j in range(len(suits)):
            a_new_deck.append([values[i], suits[j]])
            j += 1
        i += 1
    return a_new_deck


def shuffle_deck(deck_to_shuffle):
    for i in range(3):
        shuffle(deck_to_shuffle)
    return deck_to_shuffle


deck = new_deck()

shuffle_deck(deck)


def deal_cards(deck_to_deal):
    return deck_to_deal[-5:]


hand = deal_cards(deck)


print(hand)

