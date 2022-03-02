# generate random word
# ask user to guess letter
# check user input is valid
# check if user guessed letter is in the random word
# Lives
import random
import os
from ascii_art import hangman_pics
from ascii_art import hangman_graphic
from colorama import Fore
from colorama import Style


test_list = ["avenue", "awkward", "diagram"]
lives = 6
game_over = False
list_blanks = []


def landing_page():
    print(f"{Fore.CYAN}{hangman_graphic}{Style.RESET_ALL}\n")
    print("      WELCOME TO THE HANGMAN WORD GAME\n")
    print("     Guess the letters in the word to win\n")

    print(hangman_pics[6])

landing_page()


def generate_random_word():
    """
    Generate a random word
    """
    random_word = random.choice(test_list)
    return random_word

random_word = generate_random_word()  # call the random word generator


for i in range(len(random_word)):
    list_blanks += "_"
print(f"Lives: {lives}\n")
print(f"{Fore.CYAN}{str(' '.join(list_blanks)).upper()}{Style.RESET_ALL}\n")  # join list blanks for cleaner user experience
print(f"TESTWORD IS -->> {random_word.upper()}")


# the game loop
while not game_over:

    player_guess = input("Guess a letter:").lower()

    os.system('clear')


    try:
        if len(player_guess) != 1:
            raise ValueError(
                f"only one letter allowed. you entered {len(player_guess)} characters {player_guess}"
            )
        elif not player_guess.isalpha():
            raise ValueError(
                f"only letters allowed. you entered {player_guess}"
            )
        elif player_guess in list_blanks:
            print(f"You already guessed {player_guess}")


    except ValueError as e:
        print(f"warning {e}\n")
    #display any correct letter guesses
    for i in range(len(random_word)):
        letter = random_word[i]

        if letter == player_guess:
            print(f"{Fore.CYAN}{hangman_graphic}{Style.RESET_ALL}\n")  #combine line and roll out to other parts
            print("      WELCOME TO THE HANGMAN WORD GAME\n")  #combine line and roll out to other parts
            print(hangman_pics[lives])  #combine line and roll out to other parts
            print(f"You have {lives} lives\n")  #combine line and roll out to other parts
            list_blanks[i] = letter
            print(f"{Fore.CYAN}{str(' '.join(list_blanks)).upper()}{Style.RESET_ALL}\n") 
            print(f"{player_guess.upper()} is a letter in the word\n")

    if player_guess.isalpha() and player_guess not in random_word:
        
        lives -= 1
        print(f"{Fore.CYAN}{hangman_graphic}{Style.RESET_ALL}\n")  #combine line and roll out to other parts
        print("      WELCOME TO THE HANGMAN WORD GAME\n")  #combine line and roll out to other parts
        print(hangman_pics[lives])  #combine line and roll out to other parts
        print(f"You have {lives} lives\n")  #combine line and roll out to other parts
        # list_blanks[i] = letter . . .this line caused a bug, least letter was being displayed
        print(f"{Fore.CYAN}{str(' '.join(list_blanks)).upper()}{Style.RESET_ALL}\n") 
        print(f"{player_guess.upper()} is not a letter in the word - you lose a life\n")

        if lives == 0:
            print(f"\nYou have no lives left")
            print(f"\nThe word was {random_word.upper()}\n")
            game_over = True
            print("Game Over")


    if "_" not in list_blanks:
        game_over = True
        print(f"\nCongratulations! the word is {random_word.upper()} - {Fore.GREEN}You win!!{Style.RESET_ALL}\n\n")




