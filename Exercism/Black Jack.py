"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):

    if card in {'K', 'Q', 'J'}:
        return 10
    if card == 'A':
        return 1
    return int(card)



def higher_card(card_one, card_two):

    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)
    if value_one > value_two:
        return card_one
    if value_two > value_one: 
        return card_two
    return (card_one, card_two)


def value_of_ace(card_one, card_two):

    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)
    if card_one == 'A':
        value_one = 11
    if card_two == 'A':
        value_two = 11

    total = value_one + value_two
    if total<= 10:
        return 11
    return 1


def is_blackjack(card_one, card_two):

    if card_one =='A' or card_two == 'A':
        if card_one in {'10', 'K', 'Q', 'J'} or card_two in {'10', 'K', 'Q', 'J'}:
            return True
    return False


def can_split_pairs(card_one, card_two):

    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)
    if value_one == value_two:
        return True
    return False


def can_double_down(card_one, card_two):

    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)
    if value_one + value_two in {9,10,11}:
        return True

    return False