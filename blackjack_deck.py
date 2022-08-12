import random
from constants import *

class Deck:
    def __init__(self):
        self.deck_cards = []
        self.build()

    def build(self):
        for value in RANKS:
            for suit in SUITS:
                self.deck_cards.append((value, suit))
        
    def shuffle(self):
        random.shuffle(self.deck_cards)

    def deal_cards(self):
        if len(self.deck_cards) > 1:
            return self.deck_cards.pop()

    
class Hand:
    def __init__(self):
        self.hand_cards = []
        self.card_img = []
        self.value = 0

    def add_card(self, card):
        self.hand_cards.append(card)

    def calc_hand(self):
        first_card_index = [a_card[0] for a_card in self.hand_cards]
        non_aces = [c for c in first_card_index if c != 'A']
        aces = [c for c in first_card_index if c == 'A']

        for card in non_aces:
            if card in 'JQK':
                self.value += 10
            else:
                self.value += int(card)

        for card in aces:
            if self.value <= 10:
                self.value += 11
            else:
                self.value += 1
            
    def display_cards(self):
        for card in self.hand_cards:
            cards = "".join((card[0], card[1]))
            if cards not in self.card_img:
                self.card_img.append(cards)