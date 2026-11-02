import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])
class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]


beer_card = Card('7','diamonds')
print(beer_card)
print("===a2=="+"\n")
deck = FrenchDeck()
print(len(deck))
#
# for card in deck:
#     print(card)
#     print("\n")


print(deck[30])

from random import choice
print(choice(deck))

print(choice(deck))


flag = Card('Q','hearts') in deck
print(flag)

flag = Card('7','beasts') in deck

print(flag)

print("=============\n")

suit_values = dict(spades=3,hearts=2,diamonds=1,clubs=0)

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

for card in sorted(deck, key=spades_high):
    print(card)