ranks = ["Ace", '2', '3', '4', '5', '6', '7', '8', '9', '10', "Jack", "Queen", "King"]
suits = ["Diamonds", "Hearts", "Clubs", "Spades"]

cards = []
for rank in ranks:
    for suit in suits:
        cards.append(suit + ' ' + rank)
