# Imports
import random
import os
from ascii_art import hangman_pics
from ascii_art import hangman_graphic
from colorama import Fore
from colorama import Style
from words import wordlist, wordlist1, wordlist2

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
    print("           WELCOME TO THE HANGMAN WORD GAME\n")
    print("       Guess all the letters in the word to win.\n")

    print("\n You get 6 lives to beat the Hangman.")
    print(" You enter one letter at a time.")
    print(" You guess correct and the letter will be displayed.")
    print(" You guess wrong and you lose a life.")


# Generate random word
def generate_random_word():
    """
    Generate a random word
    """
    level = input(f"\n press {Fore.CYAN}1 {Style.RESET_ALL}for easier level\n press {Fore.CYAN}2 {Style.RESET_ALL}for harder level\n")
    if level == "1":
        os.system('clear')
        random_word = random.choice(wordlist1)
        return random_word
    elif level == "2":
        os.system('clear')
        random_word = random.choice(wordlist2)
        return random_word

    else:
        os.system('clear')
        landing_page()
        generate_random_word()


def start():
    landing_page()
    generate_random_word()

start()


random_word = generate_random_word()  # call the random word generator

# Display list of blank letters to be filled
for i in range(len(random_word)):
    # print(random_word)
    list_blanks += "_"
print(f"{Fore.CYAN}{hangman_graphic}{Style.RESET_ALL}")
print(hangman_pics[lives])
print(f"                 {Fore.GREEN}{lives} lives\n")
print(f"              {Fore.CYAN}{str(' '.join(list_blanks)).upper()}{Style.RESET_ALL}\n")  # join list blanks for cleaner user experience
print(f"TESTWORD IS -->> {random_word.upper()}")


def gamearea_display():
    """
    Display hangman logo pics template
    """
    os.system('clear')
    print(f"{Fore.CYAN}{hangman_graphic}{Style.RESET_ALL}")
    print(hangman_pics[lives])
    print(f"                 {Fore.GREEN}{lives} lives\n")

    # if guess same letter
    if player_guess in list_blanks:
        print(f"{Fore.YELLOW} You already guessed the letter {player_guess.upper()}{Style.RESET_ALL}\n")

# Game on loop
while not game_over:

    player_guess = input(" Guess a letter:\n").lower()

    os.system('clear')

    # validation checks, graphic & feedback template
    try:
        if len(player_guess) != 1:
            gamearea_display()
            print(f"               {Fore.CYAN}{str(' '.join(list_blanks)).upper()}{Style.RESET_ALL}\n")  # join list blanks for cleaner user experience
            raise ValueError(
                f"{Fore.YELLOW}only one letter allowed, you entered characters '{player_guess}'{Style.RESET_ALL}"
            )
        # guess is not a letter
        elif not player_guess.isalpha():
            gamearea_display()
            print(f"               {Fore.CYAN}{str(' '.join(list_blanks)).upper()}{Style.RESET_ALL}\n")  # join list blanks for cleaner user experience
            raise ValueError(
                f"{Fore.YELLOW}only letters allowed, you entered '{player_guess}'{Style.RESET_ALL}"
            )

        # deduct life
        elif player_guess not in random_word:
            lives -= 1
            gamearea_display()
            print(f"               {Fore.CYAN}{str(' '.join(list_blanks)).upper()}{Style.RESET_ALL}\n")  # join list blanks for cleaner user experience
            print(f" {Fore.YELLOW}{player_guess.upper()} is not a letter in the word - you lose a life.{Style.RESET_ALL}\n")

    # Customer error message
    except ValueError as e:
        print(f"{Fore.YELLOW} Caution: {e}{Style.RESET_ALL}\n")

    # display any correct letter guesses
    for i in range(len(random_word)):
        letter = random_word[i]
        # Correct guesses
        if letter == player_guess:
            gamearea_display()
            list_blanks[i] = letter
            print(f"               {Fore.CYAN}{str(' '.join(list_blanks)).upper()}{Style.RESET_ALL}\n")  # join list blanks for cleaner user experience
            print(f" {player_guess.upper()} is a letter in the word\n")

    # Game over condition
    if lives == 0:
        print(f" You have no lives left ...The word was {random_word.upper()}")
        game_over = True
        print(f"{Fore.RED}                GAME OVER{Style.RESET_ALL}")


    # Game over condition
    if "_" not in list_blanks:
        game_over = True
        print(f"\n Congratulations! the word is {random_word.upper()} - {Fore.GREEN}You win!!{Style.RESET_ALL}\n\n")
        play_again = input("play again? press 1\n")




