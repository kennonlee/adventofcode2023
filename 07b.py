import sys

card_vals = {"A": 14, "K": 13, "Q": 12, "J": 1, "T": 10}
for i in range(1, 10):
    card_vals[str(10-i)] = 10-i

#print(card_vals)

class Hand:
    def __init__(self, cards, bet):
        self.cards = cards
        self.bet = bet
        self.score = self.get_score()

    def __repr__(self):
        return repr((self.cards, self.score))
#        return repr((self.cards, self.bet, self.score))

    def get_score(self):
        return (self.hand_score() * (100**5)) + self.card_score()

    # score based on poker hand
    def hand_score(self):
        # too lazy to remake, just copy the dict and zero out the vals
        card_counts = card_vals.copy()
        for k in card_counts.keys():
                card_counts[k] = 0
        for c in self.cards:
             card_counts[c] += 1
#        print(card_counts)
        jcount = card_counts.pop("J")
        counts = list(card_counts.values())
        ret = 0
        # 5 of a kind
        if 5 in counts:
            ret = 6
        # 4 of a kind
        elif 4 in counts:
            if jcount == 1:
                ret = 6
            else:
                ret = 5
        elif 3 in counts:
            # full house
            if 2 in counts: 
                ret = 4
            # 3 of a kind
            else:  
                if jcount == 1:
                    ret = 5
                elif jcount == 2:
                    ret = 6
                else:
                    ret = 3
        elif 2 in counts:
            counts.remove(2)
            # 2 pair
            if 2 in counts:
                if jcount > 0:
                    ret = 4
                else:
                    ret = 2
            # 1 pair
            else:
                if jcount == 0:
                    ret = 1
                elif jcount == 1:
                    ret = 3
                elif jcount == 2:
                    ret = 5                    
                elif jcount == 3:
                    ret = 6
                else:
                    ret = 1
        # all singles
        else:
            if jcount == 1:
                ret = 1
            elif jcount == 2:
                ret = 3
            elif jcount == 3:
                ret = 5
            elif jcount == 4:
                ret = 6
            elif jcount == 5:
                ret = 6
            else:
                ret = 0
#        if ret == 3:
#            print(self.cards, ret, self.card_score())
        return ret

    # score based on card order
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
#print(hands)

sum = 0
for i, hand in enumerate(hands):
     sum += (i+1) * hand.bet
print(sum)
