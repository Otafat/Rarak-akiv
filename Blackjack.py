import random

def create_cards():
    cards = []
    for i in range(2, 11):
        for j in ('C', 'P', 'B', 'K'):
            cards.append(str(i) + j)
    for i in ('J', 'Q', 'K', 'T'):
        for j in ('C', 'P', 'B', 'K'):
            cards.append(i + j)
    return cards

def start_cards(cards):
    hand = []
    for i in range(2):
        hand.append(random.choice(cards))
        cards.remove(hand[-1])
    return hand, cards

def start_game():
    cards = create_cards()
    hand = []
    hand, cards = start_cards(cards)

start_game()
