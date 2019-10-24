from random import shuffle
import operator


def ranks(): return ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]


def suites(): return ["Clubs", "Diamonds", "Hearts", "Spades"]


class Card:
    def __init__(self, rank, suite):
        self.rank = rank
        self.suite = suite

    def description(self):
        if self.rank == "A":
            value = 1 or 11
        elif self.rank == "J" or self.rank == "Q" or self.rank == "K":
            value = 10
        else:
            value = int(self.rank)
        return "The {} of {} is worth {}".format(self.rank, self.suite, value)
   
    def value(self, curvalue):
        if self.rank == "A":
            value = 11 if curvalue <= 10 else 1
        elif self.rank == "J" or self.rank == "Q" or self.rank == "K":
            value = 10
        else:
            value = int(self.rank)
        return value

    def image(self):
        return self.rank + self.suite[0] + '.png'


class Deck:
    def __init__(self):
        self.contents = [Card(rank, suit) for rank in ranks() for suit in suites()]
        shuffle(self.contents)

    def pop(self):
        return self.contents.pop().description()
        
    def remaining(self):
        return len(self.contents)

    
def newshoe(numdecks):
    shoe = []
    for i in range(0, numdecks):
        deck = Deck()
        shoe.extend(deck.contents)
        shuffle(shoe)
    shuffle(shoe)
    return shoe

    
def deal(players, shoe):
    hands = {}
    if players:
        for i in players:
            hands[i] = []

        hands['dealer'] = []

        for i in players:
            hands[i].append(shoe.pop())

        hands['dealer'].append(shoe.pop())

        for i in players:
            hands[i].append(shoe.pop())

        hands['dealer'].append(shoe.pop())
    return hands


def hit(player, shoe, hands):
    hands[player].append(shoe.pop())
    return hands


def valueofhand(cards):
    cards.sort(key=operator.attrgetter('rank'))
    value = 0
    for i in range(0, len(cards)):
        value = value + cards[i].value(value)
    return value
