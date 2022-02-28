# generate random word
# ask user to guess letter
# check user input is valid
# check if user guessed letter is in the random word
import random

test_list = ["avenue", "awkward", "diagram"]



def generate_random_word():
    """
    Generate a random word
    """
    random_word = random.choice(test_list)
    return random_word


def player_guess():
    """
    Generate a random word
    """
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

    return player_guess



# the game loop
random_word = generate_random_word() # call the random word generator
print(f"for testing  - - random word is : {random_word.upper()}")
list_blanks =[]
for i in range(len(random_word)):
    list_blanks += "_"
print(list_blanks)

player_guess = player_guess() #call the player guess function
print(player_guess)

#display any correct letter guesses
for i in range(len(random_word)):
    letter = random_word[i]

    if letter == player_guess:
        print(f"{player_guess.upper()} is a letter in the word")
        list_blanks[i] = letter.upper()
        print(list_blanks)



