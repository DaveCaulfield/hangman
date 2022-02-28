# generate random word
# ask user to guess letter
# check user input is valid
# check if user guessed letter is in the random word
import random

test_list = ["avenue", "awkward", "diagram"]
lives = 6
game_over = False
list_blanks = []

def generate_random_word():
    """
    Generate a random word
    """
    random_word = random.choice(test_list)
    return random_word


random_word = generate_random_word()  # call the random word generator
print(f"for testing  - - random word is : {random_word.upper()}")

for i in range(len(random_word)):
    list_blanks += "_"
print(list_blanks)


# the game loop
while not game_over:
    
    player_guess = input("Pick a letter:").lower()

    try:
        if len(player_guess) != 1:
            raise ValueError(
                f"only one letter allowed. you entered {len(player_guess)} letters {player_guess}"
            )
        elif not player_guess.isalpha():
            raise ValueError(
                f"only letters allowed. you entered {player_guess}"
            )
        # add elif when user already

    except ValueError as e:
        print(f"invalid data - {e}")
    #display any correct letter guesses
    for i in range(len(random_word)):
        letter = random_word[i]

        if letter == player_guess:
            print(f"{player_guess.upper()} is a letter in the word")
            list_blanks[i] = letter.upper()
    print(list_blanks)

    if player_guess not in random_word:
        print(f"\nThats not a letter in the word - you lose a life")
        lives -= 1
        if lives == 0:
            print(f"\nYou have no lives left")
        print(f"{lives} lives left")

    if "_" not in list_blanks:
        game_over = True
        print("You win.")

