def readTXT(inputFile):
    with open(inputFile, "r") as input:
        content = []
        for row in input:
            row = row.replace("\r", "")
            row = row.replace("\n", "")
            content.append(row)
    return content

def rowProcessor(row):
    cards = row.split(" ")[0]
    bid = int(row.split(" ")[1])
    hand = Hand(cards, bid)
    for char in hand.hand:
        charCount = hand.hand.count(char)
        if charCount > 1:
            hand.counts.append(charCount)
        hand.power.append(STRENGTHS[char])
    hand.counts.sort()
    for name in TYPES:
        if hand.counts == name[0]:
            hand.type = name[1]
    return hand

def rowProcessor2(row):
    cards = row.split(" ")[0]
    bid = int(row.split(" ")[1])
    hand = Hand(cards, bid)
    for char in hand.hand:
        charCount = hand.hand.count(char)
        if char == "J":
            hand.jokers += 1
        elif charCount > 1:
            hand.counts.append(charCount)
        hand.power.append(NEWSTRENGTHS[char])
    hand.counts.sort()
    i = 0
    while i < len(TYPES):
        if hand.counts == TYPES[i][0]:
            hand.type = TYPES[i][1]
            if TYPES[i][1] == "Two pair" and hand.jokers != 0:
                hand.type == "Full house"
            elif hand.jokers != 0 and hand.jokers != 5:
                hand.type = TYPES[i + hand.jokers][1]
            elif hand.jokers == 5:
                hand.type = "Five of a kind"
        i += 1
    return hand

class Hand:
    def __init__(self, hand, bid):
        self.hand = hand
        self.counts = []
        self.jokers = 0
        self.type = ""
        self.power = []
        self.bid = bid
        self.rank = 0
        

STRENGTHS = {"2": 1,
             "3": 2,
             "4": 3,
             "5": 4,
             "6": 5,
             "7": 6,
             "8": 7,
             "9": 8,
             "T": 9,
             "J": 10,
             "Q": 11,
             "K": 12,
             "A": 13
            }

NEWSTRENGTHS = {"2": 1,
                "3": 2,
                "4": 3,
                "5": 4,
                "6": 5,
                "7": 6,
                "8": 7,
                "9": 8,
                "T": 9,
                "J": 0,
                "Q": 11,
                "K": 12,
                "A": 13
                }

TYPES = [[[], "High card"],
         [[2, 2], "Pair"],
         [[3, 3, 3], "Three of a kind"],
         [[4, 4, 4, 4], "Four of a kind"],
         [[5, 5, 5, 5, 5], "Five of a kind"],
         [[2, 2, 2, 2], "Two Pair"],
         [[2, 2, 3, 3, 3], "Full house"],
        ]

TYPESTOSORT = [[[], "High card"],
                [[2, 2], "Pair"],
                [[2, 2, 2, 2], "Two Pair"],
                [[3, 3, 3], "Three of a kind"],
                [[2, 2, 3, 3, 3], "Full house"],
                [[4, 4, 4, 4], "Four of a kind"],
                [[5, 5, 5, 5, 5], "Five of a kind"],
                ]

content = readTXT("input.txt")

# Preparing input for processing
hands = []
hands2 = []
for row in content:
    hand = rowProcessor(row)
    hand2 = rowProcessor2(row)
    hands.append(hand)
    hands2.append(hand2)

hands.sort(key=lambda hand: hand.power)
hands2.sort(key=lambda hand2: hand2.power)

ranker = 1
ranker2 = 1
for name in TYPESTOSORT:
    for hand in hands:
        if hand.type == name[1]:
            hand.rank = ranker
            ranker += 1
    for hand2 in hands2:
        if hand2.type == name[1]:
            hand2.rank = ranker2
            ranker2 += 1

answer1 = 0
for hand in hands:
    answer1 += hand.bid * hand.rank

answer2 = 0
for hand in hands2:
    answer2 += hand.bid * hand.rank

print(f"Q1: {answer1}")
print(f"Q2: {answer2}")