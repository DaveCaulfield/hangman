# Imports
import random
import os
from ascii_art import hangman_pics
from ascii_art import hangman_graphic
from colorama import Fore
from colorama import Style
from words import wordlist

# variables

lives = 6
game_over = False
list_blanks = []

# landing page graphic/display messsage
def landing_page():
    """
    Load 
    """
    print(f"{Fore.CYAN}{hangman_graphic}{Style.RESET_ALL}\n")
    print("        WELCOME TO THE HANGMAN WORD GAME\n")
    print("     Guess all the letters in the word to win.\n")

    print("\nHOW TO PLAY:")
    print("Enter one letter at a time.")
    print("If your guess is correct the letter will be displayed.")
    print("If your guess is wrong you lose a life.")

    print(hangman_pics[6])

landing_page()

#Generate random word
def generate_random_word():
    """
    Generate a random word
    """
    random_word = random.choice(wordlist)
    return random_word

random_word = generate_random_word()  # call the random word generator

# Display list of blank letters to be filled
for i in range(len(random_word)):
    list_blanks += "_"
print(f"Lives: {lives}\n")
print(f"{Fore.CYAN}{str(' '.join(list_blanks)).upper()}{Style.RESET_ALL}\n")  # join list blanks for cleaner user experience
print(f"TESTWORD IS -->> {random_word.upper()}")

def game_display_template():
    print(f"{Fore.CYAN}{hangman_graphic}{Style.RESET_ALL}\n")  #combine line and roll out to other parts
    print("      WELCOME TO THE HANGMAN WORD GAME\n")  #combine line and roll out to other parts
    print(hangman_pics[lives])  #combine line and roll out to other parts
    print(f"You have {lives} lives\n")  #combine line and roll out to other parts
    print(f"{Fore.CYAN}{str(' '.join(list_blanks)).upper()}{Style.RESET_ALL}\n") 


# Game on loop
while not game_over:

    player_guess = input("Guess a letter:").lower()

    os.system('clear')

    # validation checks, graphic & feedback template
    try:
        if len(player_guess) != 1:
            print(f"{Fore.CYAN}{hangman_graphic}{Style.RESET_ALL}\n")  #combine line and roll out to other parts
            print("      WELCOME TO THE HANGMAN WORD GAME\n")  #combine line and roll out to other parts
            print(hangman_pics[lives])  #combine line and roll out to other parts
            print(f"You have {lives} lives\n")  #combine line and roll out to other parts
            print(f"{Fore.CYAN}{str(' '.join(list_blanks)).upper()}{Style.RESET_ALL}\n")
            raise ValueError(
                f"only one letter allowed. you entered {len(player_guess)} characters '{player_guess}'"
            )
        # guess is not a letter
        elif not player_guess.isalpha():
            print(f"{Fore.CYAN}{hangman_graphic}{Style.RESET_ALL}\n")  #combine line and roll out to other parts
            print("      WELCOME TO THE HANGMAN WORD GAME\n")  #combine line and roll out to other parts
            print(hangman_pics[lives])  #combine line and roll out to other parts
            print(f"You have {lives} lives\n")  #combine line and roll out to other parts
            print(f"{Fore.CYAN}{str(' '.join(list_blanks)).upper()}{Style.RESET_ALL}\n")
            raise ValueError(
                f"only letters allowed. you entered '{player_guess}'"
            )
            #if guess same letter
        elif player_guess in list_blanks:
            print(f"You already guessed {player_guess}")
        #deduct life    
        elif player_guess not in random_word:
            lives -= 1
            print(f"{Fore.CYAN}{hangman_graphic}{Style.RESET_ALL}\n")  #combine line and roll out to other parts
            print("      WELCOME TO THE HANGMAN WORD GAME\n")  #combine line and roll out to other parts
            print(hangman_pics[lives])  #combine line and roll out to other parts
            print(f"You have {lives} lives\n")  #combine line and roll out to other parts
            print(f"{Fore.CYAN}{str(' '.join(list_blanks)).upper()}{Style.RESET_ALL}\n") 
            print(f"{player_guess.upper()} is not a letter in the word - you lose a life\n")
        
    #Customer error message
    except ValueError as e:
        print(f"Caution {e}\n")

    #display any correct letter guesses
    for i in range(len(random_word)):
        letter = random_word[i]
        #Correct guesses
        if letter == player_guess:
            game_display_template()
            # print(f"{Fore.CYAN}{hangman_graphic}{Style.RESET_ALL}\n")  #combine line and roll out to other parts
            # print("      WELCOME TO THE HANGMAN WORD GAME\n")  #combine line and roll out to other parts
            # print(hangman_pics[lives])  #combine line and roll out to other parts
            # print(f"You have {lives} lives\n")  #combine line and roll out to other parts
            # list_blanks[i] = letter
            # print(f"{Fore.CYAN}{str(' '.join(list_blanks)).upper()}{Style.RESET_ALL}\n") 
            print(f"{player_guess.upper()} is a letter in the word\n")

    #Game over condition
    if lives == 0:
        print(f"\nYou have no lives left")
        print(f"\nThe word was {random_word.upper()}\n")
        game_over = True
        print("Game Over")

    #Game over condition
    if "_" not in list_blanks:
        game_over = True
        print(f"\nCongratulations! the word is {random_word.upper()} - {Fore.GREEN}You win!!{Style.RESET_ALL}\n\n")




