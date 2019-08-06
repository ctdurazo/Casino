from random import shuffle


def ranks(): return ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]


def suites(): return ["Clubs", "Diamonds", "Hearts", "Spades"]


class Card:
    def __init__(self, rank, suite):
        self.rank = rank
        self.suite = suite

    def description(self):
        if self.rank == "Ace":
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

    
def newdeck(numdecks):
    decks = []
    for i in range(1, numdecks):
        deck = Deck()
        decks.extend(deck.contents)
        shuffle(decks)
    shuffle(decks)
    return decks

    
def deal(numplayers, deck):
    hands = []
    for i in range(0, numplayers):
        hands.append({'player': i, 'cards': []})
    
    for i in range(0, numplayers):
        hands[i]['cards'].append(deck.pop())
       
    for i in range(0, numplayers):
        hands[i]['cards'].append(deck.pop())
    return hands


def valueofhand(cards):
    value = 0
    for i in range(0, len(cards)):
        value = value + cards[i].value(value)
    return value
