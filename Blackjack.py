import random
import easygui

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

def give_card(cards, hand):
    hand.append(random.choice(cards))
    cards.remove(hand[-1])
    return hand, cards

def count_bot_cards(bots):
    c = 0
    for i in bots:
        i = i[0]
        if i.isnumeric() == True:
            c += int(i)
        else:
            if i == 'J':
                c += 2
            elif i == 'Q':
                c += 3
            elif i == 'K':
                c += 4
            elif i == 'T':
                c += 11
    return c

def count_play_cards(bots):
    c = 0
    for i in bots:
        i = i[0]
        if i.isnumeric() == True:
            c += int(i)
        else:
            if i == 'J':
                c += 2
            elif i == 'Q':
                c += 3
            elif i == 'K':
                c += 4
            elif i == 'T':
                c += 11
    return c

cards = create_cards()
hand = []
hand, cards = start_cards(cards)
bot_cards = []
bot_cards, cards = start_cards(cards)
easygui.msgbox(f'Ya\'ve {count_play_cards(hand)} cards. \n Bot have {count_bot_cards(bot_cards)} cards.', 'Values', 'Continue')
while True:
    res = easygui.enterbox('Ya will take one more card, innit? ', 'Innit?')
    if res == 'yes' or res == 'yeah':
        hand, cards = give_card(cards, hand)
    elif res == 'no' or res == 'nah':
        p = None
        del p
    else:
        easygui.msgbox('Sawy, I don\'ea understand ya. Write again.', 'error', 'Try again')
        continue

    bots = count_bot_cards(bot_cards)
    if bots >= 16:
        l = None
        del l
    else:
        bot_cards, cards = give_card(cards, bot_cards)

    easygui.msgbox(f'Ya\'ve {count_play_cards(hand)} cards \n Bot have {count_bot_cards(bot_cards)} cards', 'Values', 'Continue')

    if (res == 'no' or res == 'nah') and bots >= 16:
        player = count_play_cards(hand)
        bot = count_bot_cards(bot_cards)
        if player > 21 and bot <= 21:
            easygui.msgbox('Ya\'ve defeated', 'defeat', 'Close the game')
            break
        elif bot > 21 and player <= 21:
            easygui.msgbox('Ya\'ve won', 'Win', 'Close the game')
            break
        elif bot > 21 and player > 21:
            easygui.msgbox('Default', 'Default', 'Close the game')
            break
        elif bot > player:
            easygui.msgbox('Ya\'ve defeated', 'defeat', 'Close the game')
            break
        elif player > bot:
            easygui.msgbox('Ya\'ve won', 'Win', 'Close the game')
            break
    else:
        continue
