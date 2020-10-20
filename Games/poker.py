from random import shuffle
import operator


def ranks(): return ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]


def suites(): return ["Clubs", "Diamonds", "Hearts", "Spades"]


class Card:
    def __init__(self, rank, suite):
        self.rank = rank
        self.suite = suite

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

        for x in range(0,5):
          for i in players:
              hands[i].append(shoe.pop())

          hands['dealer'].append(shoe.pop())
    return hands
    
    
def hold(player, shoe, hands, cards)
    for card in hands[player]:
        if card not in cards:
              hands[player].remove[card]
    for i in range(0, 5-len(cards)):
        hands[player].append(shoe.pop())
    return hands
    
    
def valueofhand(cards):    
    ranks = []
    suites = []
    
    for card in cards:
        ranks.append(card.rank)
        suites.append(card.suite)
    
    suites = list(dict.fromkeys(suites))
    
    if len(suites) = 1 and ranks = ['10' 'J', 'Q', 'K', 'A']
        if ranks = ['10' 'J', 'Q', 'K', 'A']:
            return 'Royal flush'
        else if ranks in [['A', '2', '3', '4' , '5'], ['2', '3', '4' , '5', '6'], ['3', '4' , '5', '6', '7'], ['4', '5' , '6', '7', '8'], ['5', '6' , '7', '8', '9'], ['6', '7' , '8', '9', '10'], ['7', '8' , '9', '10', 'J'], ['8', '9' , '10', 'J', 'Q'], ['9', '10' , 'J', 'Q', 'K']
            return 'Straight Flush'
        return 'Flush'
            
    ranks = collections.Counter(ranks)
    value1, count1 = ranks.most_common(2)[0]
    value2, count2 = ranks.most_common(2)[1]

    if count1 == 4:
        return 'Four of a Kind'
    else if count1 == 3:
        if count2 == 2:
            return 'Full House'
        return 'Three of a Kind'
    else if count1 == 2:
        if count2 == 2:
            return 'Two Pairs'
        return 'Pair'
    
    return 'error'
