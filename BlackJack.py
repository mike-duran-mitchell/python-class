from random import shuffle


def shuffle_deck(deck_to_shuffle, num):
    for i in range(num):
        shuffle(deck_to_shuffle)
    return deck_to_shuffle


def new_deck():
    values = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']
    suits = ['Diamonds', 'Spades', 'Hearts', 'Clubs']
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


def one_card_down(cards):
    for i in range(len(cards)):
        if i != 0:
            ""
        else:
            print('\n############################################################################################## \n The dealer is holding a facedown card and a', cards[i][0], 'of', cards[i][1], '\n############################################################################################## \n')


def hit(deck_to_deal):
    keep_deck_random(deck_to_deal)
    return [deck_to_deal.pop()]


def print_hand(hand):
    hand_as_string = ""
    for i in range(len(hand)):
        hand_as_string = hand_as_string + str(hand[i][0]) + "of" + hand[i][1] + "\n"
    return hand_as_string


def get_hand_value(cards, user=True):
    cv = 0
    has_ace = False
    hand_as_string = ""
    for i in range(len(cards)):
        n = cards[i][0]
        hand_as_string = hand_as_string + "\n" + str(n) + " of " + cards[i][1]
        if n in ('King', 'Queen', 'Jack'):
            cv += 10
        elif n == 'Ace':
            cv += 1
            has_ace = True
        else:
            cv += n
    if user and has_ace:
        if cv + 10 == 21:
            cv = 21
        elif cv + 10 < 21:
            user_ace_value = input("You've got an ace! Default value is 1. Would you like that to be worth 11? y/n")
            if user_ace_value == 'y':
                cv += 11
    if not user and has_ace and cv + 10 < 21:
        cv += 10
    if user and cv == 21:
        print("One of your hands hit 21!")
    print_hand(cards)
    if user:
        print('################################# Your Cards ########################################')
        print("You are holding", len(cards), "cards of value", cv, ":", hand_as_string)
        print('################################# Your Cards ########################################\n' )
    elif not user:
        print('################################# Dealer Cards ########################################')
        print("Dealer is holding", len(cards), "cards of value", cv, ":", hand_as_string)
        print('################################# Dealer Cards ########################################\n')
    return cv


def play_another_game():
    user_plays_another = input("Do you want to play again? (y/n) : ")
    if user_plays_another == "y":
        start_game()
    else:
        print("Hasta luego!")
        exit()


def start_game():
    deck = new_deck()
    dealer_hand = new_hand(deck)
    one_card_down(dealer_hand)
    hands_value = []
    winning_hand_count = 0
    losing_hand_count = 0
    while True:
        user_number = input("Enter the number of hands you'd like to play against the house or type 'quit': ")
        if user_number == "quit":
            print("Hasta luego")
            exit()
        try:
            player_hands = make_hands(int(user_number), deck)
            for index in range(int(user_number)):
                hand = player_hands[index] if int(user_number) > 1 else player_hands
                initial_cards_value = get_hand_value(hand)
                print_hand(hand)
                if initial_cards_value == 21:
                    print("###############################################")
                    print("Natural blackjack!")
                    print("###############################################\n")
                    hands_value.append(99)
                else:
                    while True:
                        user_hit = input("Hit me? (y/n)")
                        while user_hit not in ('n', 'y'):
                            user_hit = input("Hit me? (y/n)")
                        if user_hit in "n":
                            hand_value = get_hand_value(hand)
                            hands_value.append(hand_value)
                            break
                        elif user_hit in 'y':
                            hand.extend(hit(deck))
                            hand_value = get_hand_value(hand)
                            if hand_value > 21:
                                print("###############################################")
                                print("### you busted, bronco! Onto the next hand! ###")
                                print("###############################################\n")
                                hands_value.append(0)
                                if int(user_number) == 1:
                                    play_another_game()
                                else:
                                    break
                            else:
                                continue
            dealer_hand_value = get_hand_value(dealer_hand, False)
            while dealer_hand_value < 17:
                print("Dealer takes a hit!")
                dealer_hand.extend(hit(deck))
                dealer_hand_value = get_hand_value(dealer_hand, False)
            if dealer_hand_value > 21:
                print('all hands win! dealer busts!')
                winning_hand_count = len(hands_value)
            else:
                for i in range(len(hands_value)):
                    if dealer_hand_value <= hands_value[i]:
                        winning_hand_count += 1
                    else:
                        losing_hand_count += 1
            print('You won', winning_hand_count, 'games, and lost', losing_hand_count, 'games!')
            play_another_game()
        except ValueError:
            print("Invalid integer '%s', try again" % (user_number,))


start_game()
