from random import shuffle
from operator import itemgetter


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
    fresh_hand = []
    for i in range(2):
        card = deck_to_deal.pop()
        fresh_hand.append(card)
    return fresh_hand


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


def get_card_details(cards):
    print("The player is holding", len(cards), "cards of value", get_hand_value(cards))
    for i in range(len(cards)):
        print(cards[i][0], ' of ', cards[i][1])
    return get_hand_value(cards)


def one_card_down(cards):
    for i in range(len(cards)):
        if i == 0:
            print('Facedown Card')
        else:
            print(cards[i][0], ' of ', cards[i][1])


def hit(deck_to_deal):
    keep_deck_random(deck_to_deal)
    return [deck_to_deal.pop()]


def get_hand_value(cards):
    cv = 0
    has_ace = []
    for i in range(len(cards)):
        n = cards[i][0]
        if n == 'Ace':
            user_decision = int(input('Do you want your Ace to be worth 1 or 11?'))
            while user_decision not in (1, 11):
                user_decision = int(input('Do you want your Ace to be worth 1 or 11?'))
            if user_decision == 1:
                cv += 1
                has_ace.append(1)
            elif user_decision == 11:
                cv += 11
                has_ace.append(11)
        elif n in ('King', 'Queen', 'Jack'):
            cv += 10
        else:
            cv += n
        if cv > 21:
            if 11 in has_ace:
                print('value of ace has been reduced from 11 to 1 - be careful of bustin out there!')
                cv -= 10
            else:
                break
    return cv


while True:
    user_number = input("Enter the number of hands you'd like to play against the house: ")
    if user_number == "quit":
        break
    else:
        try:
            deck = new_deck()
            player_hands = make_hands(int(user_number), deck)
            dealer_hand = new_hand(deck)
            one_card_down(dealer_hand)
            for index in range(int(user_number)):
                hand = player_hands[index]
                get_card_details(hand)
                while True:
                    user_hit = input("Hit me? (y/n)")
                    while user_hit not in ('n', 'no', 'y', 'yes', 'ys', 'ye'):
                        user_hit = input("Hit me? (y/n)")
                    if user_hit in("n", "no"):
                        break
                    elif user_hit in('y', 'yes', 'ys', 'ye'):
                        hand.extend(hit(deck))
                        check_value = get_card_details(hand)
                        if check_value > 21:
                            print('You busted, buster! Watch out for loose seals!')
                            break
                    else:
                        break
        except ValueError:
            print("Invalid integer '%s', try again" % (user_number,))
