import os
from cards_shuffle import cards_shuffle, pack_of_cards
from deal_card import deal_card
from calculate_score import calculate_score
from compare_sum import compare
from logo import logo

start_game = input("Do you want to play a game of Blackjack? Type 'y' for yes and 'n' for no: ").lower()
end_game = False

def blackjack():

    ''' Blackjack game. 
    
    This function simply returns who wins the game of blackjack, whether the computer or the player.

    Returns:
        Draw 🙃. player score: {player_score} and computer score: {comp_score} \n"
        Lose, opponent has Blackjack 😱 \n
        Win with a Blackjack 😎 \n
        You went over. You lose 😭 \n
        Opponent went over. You win 😁 \n
        You win 😃. player score: {player_score} and computer score: {comp_score} \n
        You lose 😤. player score: {player_score} and computer score: {comp_score} \n

    '''

    deck = cards_shuffle(pack_of_cards)
    user_cards = list()
    computer_cards = list()
    for i in range (0, 2):
        player_card = deal_card(deck)
        user_cards.append(pack_of_cards[player_card][0])
        comp_card = deal_card(deck)
        computer_cards.append(pack_of_cards[comp_card][0])
    
    player_score = calculate_score(user_cards)
    comp_score = calculate_score(computer_cards)
    print(f"Your cards: {user_cards}, current score: {player_score} \n")
    print(f"computer's first card: {computer_cards[0]} \n")
    
    while player_score < 21:
        player_input = input("Type 'y' to draw another card, type 'n' to pass : ").lower()
        print("\n")
        if player_input == "y":
            player_card = deal_card(deck)
            user_cards.append(pack_of_cards[player_card][0])
            player_score = calculate_score(user_cards)
            print(f"Your cards: {user_cards}, current score: {player_score} \n")
            print(f"computer's first card: {computer_cards[0]} \n")
        else:
            break
    
    while comp_score < 17 and player_score <= 21:
        comp_card = deal_card(deck)
        computer_cards.append(pack_of_cards[comp_card][0])
        comp_score = calculate_score(computer_cards)
        #print(f"computer hold cards: {computer_cards}, current score: {comp_score} \n")

    print(f"Your final Hand: {user_cards}, final score: {player_score} \n")
    print(f"Compouter's final hand: {computer_cards}, final score: {comp_score} \n")
    cmp = compare(player_score, comp_score)
    return cmp


while start_game == 'y' and end_game == False:
    os.system("clear")
    print(logo)
    print(blackjack())
    choice = input("Do you want to play again? Type 'y' for yes and 'no' for no: ").lower()
    print("\n")
    if choice == "n":
        end_game = True
        print("Goodbye \n")



