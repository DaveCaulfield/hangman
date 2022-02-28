# generate random word
# ask user to guess letter
# check user input is valid
# check if user guessed letter is inthe random word
import random

test_list = ["avenue", "awkward", "diagram"]

def generate_random_word():
    """
    Generate a random word
    """
    return random.choice(test_list)

def player_guess():
    """
    Generate a random word
    """
    return input("Pick a letter:").lower()

    
def game_loop(): 
    random_word = generate_random_word()
    print(random_word)
    list_blanks =[]
    for i in range(len(random_word)):
        list_blanks += "_"
    print(list_blanks)



game_loop()
guess = player_guess()