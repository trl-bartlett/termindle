import random

ascii_title = """
                         _           _ _        
   _                    (_)         | | |       
 _| |_ _____  ____ ____  _ ____   __| | | _____ 
(_   _) ___ |/ ___)    \| |  _ \ / _  | || ___ |
  | |_| ____| |   | | | | | | | ( (_| | || ____|
   \__)_____)_|   |_|_|_|_|_| |_|\____|\_)_____)
   
by @trl-bartlett
------------------------------------------------
"""
print(ascii_title)

# list of 5 letter words
word_vault = ["apple", "brave", "charm", "delta",
              "eagle", "frost", "glyph", "honey",
              "ivory", "joker", "knack", "lunar",
              "mango", "noble", "oasis", "prism",
              "quilt", "raven", "sheep", "thief",
              "umbra", "vivid", "waltz", "xenon",
              "yacht", "zesty"]

# get a random word
random_word = random.choice(word_vault)

# display blank word
display_word = ["_" for _ in random_word]
print(" ".join(display_word))

# end game bool
game_end = False

# attempts variable
attempts_left = 6

# used letter set 
used_letters = set()

# game loop
while not game_end and attempts_left > 0:

    # prompt user for a word
    user_guess = input("\nenter a word: ").lower()

    # add each letter of the guessed word to the used letters set
    for letter in user_guess:
        used_letters.add(letter)

    # check each position in the guessed word
    if len(user_guess) == len(random_word):
        for i in range(len(random_word)):
            if user_guess[i] == random_word[i]:
                display_word[i] = random_word[i].upper()

    # check for correct letters in incorrect positions
    correct_letters_wrong_position = [letter for letter in user_guess if letter in random_word and letter != random_word[user_guess.index(letter)]]

    # sort and format the used letters
    sorted_used_letters = sorted(used_letters)
    formatted_used_letters = ", ".join(sorted_used_letters)

    # print current state of letters guessed
    print(" ".join(display_word))

    # print used letters
    print(f"\nused letters: {formatted_used_letters}")

    # tell user that there are letter(s) from their guess that are in the word, but in the wrong place
    if correct_letters_wrong_position:
        print(f"letters {', '.join(correct_letters_wrong_position).upper()} are in the word but in the wrong position.")

    # print attempts left
    attempts_left -= 1
    print(f"attempts left: {attempts_left}\n")

    # check if the word is completely guessed
    if "_" not in display_word:
        game_end = True

# print win or lose message
if game_end:
    print(f"\nyou got the word! it was {random_word}")
else:
    print(f"game over! the word was '{random_word.upper()}'.")
