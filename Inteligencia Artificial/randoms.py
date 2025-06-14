import random

#Generate a random number
random_number = random.randint(1,10)
print(random_number)

#Choose a random color
colors = ["red", "green", "blue"]
random_color = random.choice(colors)
print(random_color)

#Shuffle a card deck
cards = ["As", "King", "Queen", "Jack", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
random.shuffle(cards)
print(cards)