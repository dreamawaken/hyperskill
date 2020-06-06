# Write your code here
from string import ascii_lowercase
import random

word_list = ["python", "java", "kotlin", "javascript"]
chosen_word = random.choice(word_list)
# Create an empty list with hyphens that corresponds with
# the length of the word.
empty_list = list(len(chosen_word) * "-")
guesses_list = []
attempt_count = 0

print("H A N G M A N")

choice = input(f'Type "play" to play the game, "exit" to quit: ')

if choice == "play":

    while attempt_count < 8 and "".join(empty_list) != chosen_word:
        print()
        print("".join(empty_list))
        letter = input(f"Input a letter: ")

        if len(letter) > 1:
            print("You should input a single letter")

        elif letter not in ascii_lowercase:
            print("It is not an ASCII lowercase letter")

        elif letter in guesses_list:
            print("You already typed this letter")

        elif letter in chosen_word:
            for letter_index in range(len(chosen_word)):
                # Check to see that inputted letter matches the
                # current letter in the index.
                if chosen_word[letter_index] == letter:
                    # If so, replace the hyphen with the letter.
                    empty_list[letter_index] = letter
                    guesses_list.append(letter)

        else:
            print("No such letter in the word")
            guesses_list.append(letter)
            if attempt_count == 8:
                break
            elif "".join(empty_list) == chosen_word:
                break
            else:
                attempt_count += 1

    if attempt_count == 8:
        print("You are hanged!")
    else:
        print(f"You guessed the word {chosen_word}!")
        print("You survived!")

else:
    exit()
