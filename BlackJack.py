from random import shuffle


def shuffle_deck(deck_to_shuffle, num):
    for i in range(num):
        shuffle(deck_to_shuffle)
    return deck_to_shuffle


def new_deck():
    values = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']
    suits = ['diamonds', 'spades', 'hearts', 'clubs']
    a_new_deck = []
    for i in range(len(values)):
        for j in range(len(suits)):
            a_new_deck.append([values[i], suits[j]])
            j += 1
        i += 1
    shuffle_deck(a_new_deck, 3)
    return a_new_deck


def new_hand(deck_to_deal):
    hand = []
    for i in range(2):
        card = deck_to_deal.pop()
        hand.append(card)
    return hand


def keep_deck_random(deck_to_deal):
    if len(deck_to_deal) < 30:
        deck_to_add = new_deck()
        deck_to_deal.extend(deck_to_add)
        shuffle_deck(deck_to_deal, 3)
    return deck_to_deal


def make_hands(num, starting_deck):
    hands = []
    if num > 1:
        for i in range(num):
            keep_deck_random(starting_deck)
            hands.append(new_hand(starting_deck))
        return hands
    else:
        return new_hand(starting_deck)


def hit(deck_to_deal):
    keep_deck_random(deck_to_deal)
    return deck_to_deal.pop()


# new_hands = make_hands(50, deck)

# print(dealer_hand, 'arg', len(new_hands), len(deck))

def get_card_values(cards):
    print(cards[0], cards[1])

while True:
    user_number = input("Enter the number of hands you'd like to play against the house: ")
    if user_number == "quit":
        break
    else:
        try:
            deck = new_deck()
            new_hands = make_hands(int(user_number), deck)
            dealer_hand = new_hand(deck)
            print("the dealer's hand is: ", get_card_values(dealer_hand))
        except ValueError:
            print("Invalid integer '%s', try again" % (user_number,))
