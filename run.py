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
    Load landing page
    """
    print(f"{Fore.CYAN}{hangman_graphic}{Style.RESET_ALL}\n")
    print("        WELCOME TO THE HANGMAN WORD GAME\n")
    print("     Guess all the letters in the word to win.\n")

    print("\nTo beat the Hangman:")
    print("- Enter one letter at a time.")
    print("- If your guess is correct the letter will be displayed.")
    print("- If your guess is wrong you lose a life.")

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
print(f"You have {lives} lives\n")
print(f"{Fore.CYAN}{str(' '.join(list_blanks)).upper()}{Style.RESET_ALL}\n")  # join list blanks for cleaner user experience
print(f"TESTWORD IS -->> {random_word.upper()}")


def gamearea_display():
    """
    Display hangman logo pics template
    """
    os.system('clear')
    print(f"{Fore.CYAN}{hangman_graphic}{Style.RESET_ALL}")  #combine line and roll out to other parts
    # print("      WELCOME TO THE HANGMAN WORD GAME\n")  #combine line and roll out to other parts
    print(hangman_pics[lives])  #combine line and roll out to other parts
    print(f"You have {lives} lives\n")  #combine line and roll out to other parts
    
    #if guess same letter
    if player_guess in list_blanks:
        print(f"{Fore.YELLOW}You already guessed the letter {player_guess.upper()}{Style.RESET_ALL}\n")
  

# Game on loop
while not game_over:

    player_guess = input("Guess a letter:\n").lower()

    os.system('clear')

    # validation checks, graphic & feedback template
    try:
        if len(player_guess) != 1:
            gamearea_display()
            print(f"{Fore.CYAN}{str(' '.join(list_blanks)).upper()}{Style.RESET_ALL}\n")
            raise ValueError(
                f"{Fore.YELLOW}only one letter allowed, you entered {len(player_guess)} characters '{player_guess}'{Style.RESET_ALL}"
            )
        # guess is not a letter
        elif not player_guess.isalpha():
            gamearea_display()
            print(f"{Fore.CYAN}{str(' '.join(list_blanks)).upper()}{Style.RESET_ALL}\n")
            raise ValueError(
                f"{Fore.YELLOW}only letters allowed, you entered '{player_guess}{Style.RESET_ALL}'"
            )
       
        #deduct life    
        elif player_guess not in random_word:
            lives -= 1
            gamearea_display()
            print(f"{Fore.CYAN}{str(' '.join(list_blanks)).upper()}{Style.RESET_ALL}\n") 
            print(f"{Fore.YELLOW}{player_guess.upper()} is not a letter in the word - you lose a life{Style.RESET_ALL}\n")
        
    #Customer error message
    except ValueError as e:
        print(f"{Fore.YELLOW}Caution: {e}{Style.RESET_ALL}\n")

    #display any correct letter guesses
    for i in range(len(random_word)):
        letter = random_word[i]
        #Correct guesses
        if letter == player_guess:
            gamearea_display()
            list_blanks[i] = letter
            print(f"{Fore.CYAN}{str(' '.join(list_blanks)).upper()}{Style.RESET_ALL}\n") 
            print(f"{player_guess.upper()} is a letter in the word\n")

    #Game over condition
    if lives == 0:
        print(f"\nYou have no lives left")
        print(f"\nThe word was {random_word.upper()}\n")
        game_over = True
        print(f"{Fore.RED}Game Over{Style.RESET_ALL}")

    #Game over condition
    if "_" not in list_blanks:
        game_over = True
        print(f"\nCongratulations! the word is {random_word.upper()} - {Fore.GREEN}You win!!{Style.RESET_ALL}\n\n")




