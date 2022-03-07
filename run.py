# Imports
import random
import os
from colorama import Fore
from colorama import Style
from words import wordlist1, wordlist2
from ascii_art import hangman_pics
from ascii_art import hangman_graphic




# landing page 

def landing_page():
    """
    Load landing page
    """
    print(f"{Fore.CYAN}{hangman_graphic}{Style.RESET_ALL}\n")
    print("           WELCOME TO THE HANGMAN WORD GAME\n")
    print("       Guess all the letters in the word to win.\n")

    menu_landing = False

    print(f"\n press {Fore.CYAN}1 {Style.RESET_ALL}to play")
    print(f" press {Fore.CYAN}2 {Style.RESET_ALL}for instructions")
    landing_input = input("\n")

    if landing_input == "1":
        play()
    elif landing_input == "2":
        instructions()
    else:
        menu_landing = False
        while menu_landing is False:
            print(f"{Fore.CYAN}{hangman_graphic}{Style.RESET_ALL}\n")
            print("           WELCOME TO THE HANGMAN WORD GAME\n")
            print("       Guess all the letters in the word to win.\n")

            print(f"{Fore.YELLOW}\n Please enter valid choice . . .")
            print(f"{Style.RESET_ALL}")
            print(f" press {Fore.CYAN}1 {Style.RESET_ALL}to play")
            print(f" press {Fore.CYAN}2 {Style.RESET_ALL}for instructions")
            landing_input = input("\n")

            if landing_input == "1":
                play()
            elif landing_input == "2":
                instructions()


def instructions():
    """
    instructions page
    """
    print(f"{Fore.CYAN}{hangman_graphic}{Style.RESET_ALL}")
    print(f" {Fore.CYAN}Instructions:{Style.RESET_ALL}")
    print("\n You get six lives to beat the Hangman.")
    print(" You try to guess all the letters in the word to win.")
    print(" You guess one letter at a time.")
    print(" You guess correct and the letter will be displayed.")
    print(" You guess wrong and you lose a life.\n")

    print(f" press {Fore.CYAN}1 {Style.RESET_ALL}to play")
    print(f" press {Fore.CYAN}2 {Style.RESET_ALL}to return to homepage")
    instruction_choice = input(" \n")

    if instruction_choice == "1":
        play()
    elif instruction_choice == "2":
        start()
    else:
        instruction = False
        while instruction is False:
            print(f"{Fore.CYAN}{hangman_graphic}{Style.RESET_ALL}")
            print(f" {Fore.CYAN}Instructions:{Style.RESET_ALL}")
            print("\n You get six lives to beat the Hangman.")
            print(" You try to guess all the letters in the word to win.")
            print(" You guess one letter at a time.")
            print(" You guess correct and the letter will be displayed.")
            print(" You guess wrong and you lose a life.\n")

            print(f"{Fore.YELLOW} Please enter a valid choice . . .")
            print(f"{Style.RESET_ALL}")
            print(f" press {Fore.CYAN}1 {Style.RESET_ALL}to play")
            print(f" press {Fore.CYAN}2 {Style.RESET_ALL}to return to homepage")
            instruction_choice = input(" \n")

            if instruction_choice == "1":
                play()
            elif instruction_choice == "2":
                start()

def play():
    """
    start playing the game
    """
    lives = 6
    game_over = False
    list_blanks = []

    # Generate random word
    def generate_random_word():
        """
        Generate a random word
        """
        print(f"{Fore.CYAN}{hangman_graphic}{Style.RESET_ALL}")
        print(hangman_pics[6])
        print("")
        print(" Let's play Hangman . . select your level\n")
        print(f"\n press {Fore.CYAN}1 {Style.RESET_ALL}for easy level")
        print(f" press {Fore.CYAN}2 {Style.RESET_ALL}for hard level")
        level = input(" \n")
        print(f"{Style.RESET_ALL}")

        if level == "1":
            random_word = random.choice(wordlist1)
            return random_word
            user_choice = True
        elif level == "2":
            random_word = random.choice(wordlist2)
            return random_word
            user_choice = True
        else:
            user_choice = False
            while user_choice is False:
                print(f"{Fore.CYAN}{hangman_graphic}{Style.RESET_ALL}")
                print(hangman_pics[6])
                print("")
                print(
                    " Let's play Hangman . . select your level\n"
                    )
                print(f"{Fore.YELLOW} Please enter a valid choice . . .")
                print(f"{Style.RESET_ALL}")
                print(f" press {Fore.CYAN}1 {Style.RESET_ALL}for easy level")
                print(f" press {Fore.CYAN}2 {Style.RESET_ALL}for hard level")
                level = input(" \n")
                print(f"{Style.RESET_ALL}")
                if level == "1":
                    random_word = random.choice(wordlist1)
                    return random_word
                    user_choice = True
                elif level == "2":
                    random_word = random.choice(wordlist2)
                    return random_word
                    user_choice = True

    # call the random word generator
    random_word = generate_random_word()

    # Display list of blank letters to be filled
    for i in range(len(random_word)):
        list_blanks += "_"
    print(f"{Fore.CYAN}{hangman_graphic}{Style.RESET_ALL}")
    print(hangman_pics[lives])
    print(f"                 {Fore.GREEN}{lives} lives\n")
    print(f" {Fore.CYAN}{str(' '.join(list_blanks)).upper()}\n")
    print(f"{Style.RESET_ALL}")
    print(f"TESTWORD IS -->> {random_word.upper()}")


    def gamearea_display():
        """
        Display hangman logo pics template
        """
        os.system('clear')
        print(f"{Fore.CYAN}{hangman_graphic}{Style.RESET_ALL}")
        print(hangman_pics[lives])
        print(f"                 {Fore.GREEN}{lives} lives")

        # if guess same letter
        if player_guess in list_blanks:
            print(f"{Fore.YELLOW}")
            print(f" You already guessed letter '{player_guess.upper()}'\n")

    # Game on loop
    while not game_over:

        player_guess = input(" Guess a letter:\n").lower()

        os.system('clear')

        # validation checks, graphic & feedback template
        try:
            if len(player_guess) != 1:
                gamearea_display()
                print(f" {Fore.CYAN}{str(' '.join(list_blanks)).upper()}\n\n")
                raise ValueError(
                    f"only one letter allowed, you entered '{player_guess}'"
                )
            # guess is not a letter
            elif not player_guess.isalpha():
                gamearea_display()
                print(f" {Fore.CYAN}{str(' '.join(list_blanks)).upper()}\n")
                print(f"{Style.RESET_ALL}")
                raise ValueError(
                    f"{Fore.YELLOW}letters only, you entered '{player_guess}'"
                )

            # deduct life
            elif player_guess not in random_word:
                lives -= 1
                gamearea_display()
                print(f" {Fore.CYAN}{str(' '.join(list_blanks)).upper()}\n")
                print(f"{Style.RESET_ALL}{Fore.YELLOW}")
                print(f" '{player_guess.upper()}' is not a letter in the word")
                print(f"{Style.RESET_ALL}")

        # Custom error message
        except ValueError as e:
            print(f"{Fore.YELLOW} Caution: {e}{Style.RESET_ALL}\n")

        # display any correct letter guesses
        for i in range(len(random_word)):
            letter = random_word[i]
            # Correct guesses
            if letter == player_guess:
                gamearea_display()
                list_blanks[i] = letter
                print(f" {Fore.CYAN}{str(' '.join(list_blanks)).upper()}\n")
                print(f"{Style.RESET_ALL}")
                print(f" '{player_guess.upper()}' is a letter in the word")
                print(f"{Style.RESET_ALL}")

        # Game over condition
        if lives == 0:
            print(
                f" You have no lives left ..The word was {random_word.upper()}"
                )
            game_over = True
            print(f"{Fore.RED}                GAME OVER{Style.RESET_ALL}")
            print(f"\n press {Fore.CYAN}1 {Style.RESET_ALL}to play again")
            print(f" press {Fore.CYAN}2 {Style.RESET_ALL}for homepage")
            play_again = input(" \n")
            if play_again == "1":
                play()
            elif play_again == "2":
                start()
            else:
                replay = False
                while replay is False:
                    print(f"{Fore.CYAN}{hangman_graphic}{Style.RESET_ALL}")
                    print(
                        f"{Fore.RED}                GAME OVER{Style.RESET_ALL}"
                        )
                    print(f"{Fore.YELLOW}\n Please enter valid choice . . .")
                    print(f"{Style.RESET_ALL}")
                    print(
                        f" press {Fore.CYAN}1 {Style.RESET_ALL}to play again"
                        )
                    print(f" press {Fore.CYAN}2 {Style.RESET_ALL}for homepage")
                    play_again = input(" \n")
                    if play_again == "1":
                        play()
                    elif play_again == "2":
                        start()

        # Game over condition
        if "_" not in list_blanks:
            game_over = True
            print(f" Congratulations! the word is {random_word.upper()}\n")
            print(f"                {Fore.GREEN}YOU WIN!!{Style.RESET_ALL}")
            
            print(f"\n press {Fore.CYAN}1 {Style.RESET_ALL}to play again")
            print(f" press {Fore.CYAN}2 {Style.RESET_ALL}for homepage")
            play_again = input(" \n")
            if play_again == "1":
                play()
            elif play_again == "2":
                start()
            else:
                replay = False
                while replay is False:
                    print(f"{Fore.CYAN}{hangman_graphic}{Style.RESET_ALL}")
                    print(
                        f"{Fore.RED}                GAME OVER{Style.RESET_ALL}"
                        )
                    print(f"{Fore.YELLOW}\n Please enter valid choice . . .")
                    print(f"{Style.RESET_ALL}")
                    print(
                        f" press {Fore.CYAN}1 {Style.RESET_ALL}to play again"
                        )
                    print(f" press {Fore.CYAN}2 {Style.RESET_ALL}for homepage")
                    play_again = input(" \n")
                    if play_again == "1":
                        play()
                    elif play_again == "2":
                        start()



def start():
    """
    start the program
    """
    landing_page()
    # landing_menu()
    play()


start()