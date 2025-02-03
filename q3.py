import random

suits = "♠♥♣♦"
values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

deck = []

# Create the deck of cards
for suit in suits:
    for value in values:
        deck.append(f"{value}{suit}")

# Shuffle the deck
random.shuffle(deck)

# Sample a hand of 5 cards (without replacement)
hand = deck[:5]

# Print the shuffled deck and the hand
print("Shuffled deck:", deck)
print("Hand of 5 cards:", hand)