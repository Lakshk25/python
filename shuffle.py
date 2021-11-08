import itertools
import random
my_deck = list(itertools.product(
    range(1, 11), ['Spade', 'Heart', 'Diamond', 'Club']))
print("The cards are being shuffled")
random.shuffle(my_deck)
print("Cards are drawn at random")
print("They are : ")
for i in range(5):
    print(my_deck[i][0], "of", my_deck[i][1])
