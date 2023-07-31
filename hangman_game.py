from hangman_art import logo, stages
from hangman_words import word_list
import random

end_game = False
lives = 6
display = list()
guess_list = list()


chosen_word = random.choice(word_list)
print(chosen_word)
word_length = len(chosen_word)

for i in range (0, word_length):
    display += "_"

print(logo)

# Loop till the game ends.
while not end_game:
    repeat = False
    guess = input("Guess a letter: ").lower()

    if guess in guess_list:
        print(f"you have already guessed {guess}")
        repeat = True

    guess_list.append(guess)

    for cursor in range(0, word_length):
        letter = chosen_word[cursor]

        if guess == letter:
            display[cursor] = letter
    
    # Checking for the words that are repeated for both incorrect and correct guesses.
    if guess not in chosen_word and repeat is False:
        print("You guessed a letter, that is not in the word. you lose a life")
        lives -= 1
        if lives == 0:
            end_game = True
            print("GAME OVER, YOU LOSE")


    print(f"{' '.join(display)}")

    if "_" not in display:
        print("GAME OVER, YOU WIN")

    print(stages[lives])

    if lives != 0:
        print(f"********************************* You have {lives} lives left *********************************")
    


