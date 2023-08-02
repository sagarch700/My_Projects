import random

card_type = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "K", "Q", "j" ]
card_values = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
no_of_cards = 4
pack_of_cards = dict()
face_down = list()

for i in range(0, len(card_type)):
    pack_of_cards[card_type[i]] = [card_values[i], no_of_cards]

#print(pack_of_cards)
def cards_shuffle(pack_of_cards):
    for i in pack_of_cards:
        #print(i)
        no_of_cards = pack_of_cards[i][1]
        for x in range(0, no_of_cards):
            face_down.append(i)
    random.shuffle(face_down)
    return face_down