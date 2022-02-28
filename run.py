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
display =[]
for i in range(len(random_word)):
    display += "_"
print(display)


def player_guess():
    return input("Pick a letter:").lower()

guess = player_guess()