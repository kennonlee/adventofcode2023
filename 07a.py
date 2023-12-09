import sys

card_vals = {"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10}
for i in range(1, 10):
    card_vals[str(10-i)] = 10-i

#print(card_vals)

class Hand:
    def __init__(self, cards, bet):
        self.cards = cards
        self.bet = bet
        self.score = self.get_score()

    def __repr__(self):
        return repr((self.cards, self.bet, self.score))

    def get_score(self):
        return (self.hand_score() * (100**5)) + self.card_score()

    def hand_score(self):
        card_counts = card_vals.copy()
        for k in card_counts.keys():
                card_counts[k] = 0
        for c in self.cards:
             card_counts[c] += 1
#        print(card_counts)
        counts = list(card_counts.values())
        if 5 in counts:
             return 10
        elif 4 in counts: return 9
        elif 3 in counts and 2 in counts: return 8
        elif 3 in counts: return 7
        elif 2 in counts:
             counts.remove(2)
             if 2 in counts:
                  return 6
             else:
                  return 5
        else:
             return 0
    
    def card_score(self):
        ret = 0
        for c in self.cards:
              ret += card_vals[c]
              ret *= 100
        ret /= 100
        return int(ret)
             
        
hands = []
for line in sys.stdin.readlines():
     cards, bet = line.split()
     hands.append(Hand(cards, int(bet)))

hands.sort(key=lambda hand: hand.score)
print(hands)

sum = 0
for i, hand in enumerate(hands):
     sum += (i+1) * hand.bet
print(sum)
