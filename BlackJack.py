#blackjack

#cards
values = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']
suits = ['diamonds', 'spades', 'hearts', 'clubs']

deck = []


for i in range(len(values)):
    for j in range(len(suits)):
        print('i', i, 'ai', values[i], 'j', j, 'suits', suits[j])
        j += 1
    i += 1

