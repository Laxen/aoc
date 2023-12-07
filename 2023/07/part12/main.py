import sys
import numpy as np
from collections import defaultdict, deque
from pyhelpers import Parser
import re

class Hand:
    def __init__(self, cards, bid):
        self.cards = cards
        self.bid = bid

        card_dict = defaultdict(lambda: 0)
        for c in cards:
            card_dict[c] = card_dict[c] + 1

        card_dict = dict(sorted(card_dict.items(), key=lambda x: x[1], reverse=True))
        self.hand_value = 0
        for card, count in card_dict.items():
            if card == "J" and count != 5:
                # There something more than just Js, some other card is more valuable
                continue

            if card != "J" and "J" in card_dict:
                count += card_dict["J"]
                card_dict["J"] = 0

            if count == 5:
                # Five of a kind
                self.hand_value = max(self.hand_value, 6)
            elif count == 4:
                # Four of a kind
                self.hand_value = max(self.hand_value, 5)
            elif count == 3 and self.hand_value == 1:
                # Full house
                self.hand_value = max(self.hand_value, 4)
            elif count == 2 and self.hand_value == 3:
                # Full house
                self.hand_value = max(self.hand_value, 4)
            elif count == 3:
                # Three of a kind
                self.hand_value = max(self.hand_value, 3)
            elif count == 2 and self.hand_value == 1:
                # Two pairs
                self.hand_value = max(self.hand_value, 2)
            elif count == 2:
                # Two of a kind
                self.hand_value = max(self.hand_value, 1)
            elif count == 1:
                # High card
                self.hand_value = max(self.hand_value, 0)

    def __repr__(self):
        return f"{self.cards} - {self.hand_value}"

    def __lt__(self, other):
        if self.hand_value == other.hand_value:
            for ci in range(5):
                if order.index(self.cards[ci]) > order.index(other.cards[ci]):
                    return False
                elif order.index(self.cards[ci]) < order.index(other.cards[ci]):
                    return True
            return False
        return self.hand_value < other.hand_value

np.set_printoptions(linewidth=np.inf)

def make_data(input_file):
    ret = []
    with open(input_file, "r") as f:
        for line in f:
            cards, bid = line.strip().split()
            ret.append(Hand(cards, bid))
    return ret

if len(sys.argv) > 1:
    print("INPUT\n")
    data = make_data("input")
else:
    print("EXAMPLE\n")
    data = make_data("example")

# -----------------

order = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
order.reverse()

data = sorted(data, reverse=True)
data.reverse()

s = sum([(i+1) * int(c.bid) for i, c in enumerate(data)])
print(s)
