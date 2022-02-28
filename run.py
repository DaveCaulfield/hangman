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
    

random_word = generate_random_word()
print(random_word)

