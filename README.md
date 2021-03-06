# The Hangman Word Game

## Overview

This is a web application re-creating the old word game Hangman. Players try to discover a word by guessing its letters. Each time a player guesses a correct letter it is displayed on screen. Each time a player guesses a wrong letter they lose a life. The web application is for anyone who would like to play a word puzzle game. The game is a python console line web applicataion deployed on [Heroku](https://id.heroku.com/login).

Here is the link to the deployed site [The Hangman Word Game](https://the-hangman-wordgame.herokuapp.com/)


![landing page](docs/readme-images/landing-page.png)



# How to play
 - The player starts the game by selecting their option of an easier or harder level of the game.
 - A random word is generated but not revealed for the player to guess.
 - The word is presented on screen as a series of underscores "_ _ _ _ _" matching the number of letters in the word.
 - The player is prompted and enters their letter guess into the the terminal.
 - Invalid input returns a feedback message to the player.
 - A correct guess will result in the letter being displayed in its position in the list of underscores "_ O _ _ _".
 - An incorrect guess will result in losing a life and an ascii art image begins to be drawn.
 - The player begins each game with six lives. When all lives are gone the player loses the game.
 - If the player guesses all the letters in the word the player wins the game.

# Planning Phase

## User Stories:
As a user:
 - I want to know at first visit what the site is.
 - I want instructions on how to play the game.
 - I want feedback throughout the game.
 - I want to play the hangman word game

 ## Applications goals
The application aims to:
  - Make clear what the application is.
  - Provide instructions to play the game.
  - Provide feedback to players throughout the game.
  - Provide game functionality and enjoyable user experince to play the hangman word game.

## Achieving Application goals
 - A large ascii art Hangman banner is displayed on the landing page with a welcome message.
 - Instructions are immediately available to the user and the game is explained clearly.
 - Feedback messages for invalid input, correct guesses, incorrect guesses, number of lives are clear and consitent throughout the application.
 - The game functionality has been succesfully implemented and tested.
 - An easy and intuitive user experience has been delivered  while re-creating the hangman word game including the hangman graphics.

[Back to top](#Overview)

# Design

The Design process for the hangman game started with a flow chart to map out the steps involved through out the life cycle of the game.
The flow chart was created using [Lucid Charts](https://www.lucidchart.com/pages/).

![Flow chart](docs/readme-images/hangman-flow-chart.png)


# User Experience 

The user experience is designed to be as user friendly and intuitive as possible. Clear instructions and feedback messages are provided to the user and colour has been added to the text. This adds to the user experience within the constraints of a console line web application.


# Site Structure

The Hangman game runs python code in a console line web application hosted on the Heroku cloud application platform.

The code for the application consits of threw python files:
- run.py for the game funtionality.
- words.py for the word lists to store and provide the word to be guessed.
- ascii_art.py for the ascii art images used in the application.

[Back to top](#Overview)

# Features

## Landing page banner
 - The Hangman banner is displayed at the top of the landing page. 
 - It is an ascii art design in cyan color and welcomes the user. 
 - It immediately lets the user know what the site is and adds to the user experience.

![The Hangman banner](docs/readme-images/banner.png)


## Landing page menu
- A welcome message is displayed to the user.
- A menu introduces the user to the navigation system of the site.
- The user can choose to play the game or go to the instructions page.

![Landing page Menu](docs/readme-images/landing-menu.png)


## Instructions page
 - The instructions give clear details explaining how to play the game.
 - The user can then easily choose to play the game or return to the homepage.

![instructions](docs/readme-images/instructions.png)

## Game levels
 - When the user chooses to play there is an option for different game levels.
 - The user can press 1 for an easier level - words up to six letters in length.
 - The user can press 2 for a harder level - words with seven letters or more. 

 ![game levels](docs/readme-images/levels-menu.png)

 ## Game page
 - The game page displays an ascii art feature reprenting the gallows.
 - This is where the image of a person will be drawn as the game progresses.
 - The number of lives are displayed & updated in green text under the gallows.
 - The blanks/underscores displayed in cyan color represent the letters of the word.
 - The correct letters guessed will replace the blank underscores as the user guesses them.
 - The user is prompted to guess a letter. This provides input to the game.

 ![game page](docs/readme-images/game-page.png)


 ## Feedback to the user
  - Feedback is provided when a user inputs a guess.
  - When a correct letter is guessed the letter is displayed in the list of blank underscores.
  - A message is also returned advising that the Letter is in the word
  
 ![correct guess](docs/readme-images/correct-guess.png)


  - When an incorrect letter is guessed the ascii art image to starts to be drawn.
  - The number of lives displayed is updated with the remaining lives left.
  - A message is also returned in orange warning text advising that the Letter is not in the word.
  - A message in red text advises that the user has lost a life.
  - This all combines to give an easy and intuitive user experience.
  - The different colors add to the user experience.

   ![lose a life](docs/readme-images/lose-life.png)


 ## invalid input

  - If a user enters invalid input a corresponding feedback message is displayed.
  - If a user enters multiple characters as input then a customised message is returned clearly explaining what the issue is.

  ![invalid input](docs/readme-images/invalid-input.png)

  - If a user enters non-alpha characters as input then a customised message is returned clearly explaining what the issue is.

  ![invalid input](docs/readme-images/invalid-input-no.png)


 ## Game over - lose

 - If the user runs out of lives before guessing all the correct letters the game is over.
 - A message is returned to the user advising they have no lives left.
 - "Game Over" is displayed in red text.
 - The user can then easily choose to play again or return to the homepage by selecting from the menu feature.

 ![game lose](docs/readme-images/game-over.png)

  ## Game over - win
  - If the user guesses all the letters in the word they win the game.
  - A message is returned to the user advising they have won.
  - "YOU WIN" is displayed in green text
  - The user can then easily choose to play again or return to the homepage by selecting from the menu options.


 ![game win](docs/readme-images/game-win.png)

[Back to top](#Overview)

# Technologies used
  - [Python](https://www.python.org/) was used to code the application.
  - [pep8 validator](http://pep8online.com/) was used to validate the python3 code.
  - [Gitpod](https://www.gitpod.io/#get-started) was used to create and edit the applications files.
  - [Github](https://github.com/) was used to host the code repository.
  - [Heroku](https://id.heroku.com/login) was used to deploy the application.
  - [Lucid Chart](https://lucid.co/) was used to create the flow chart.

[Back to top](#Overview)


# Libraries

 - random:
   - random choice is used to generate a random word from the wordlists.

 - os:
   - os system clear command is used to clear the console as the user progresses through the game. This provides a cleaner user experience to the player.

 - colorama
   - colorama is used to bring color to text and ascii art in the console.


# Deployment
The Hangman web application was deployed using the [Heroku](https://id.heroku.com/login) platform.

The following steps were taken to deploy the site:

 - Log into your Heroku account.
 - From the home dashboard, click on "New" then "Create new app".
 - Enter the "App name" and "Choose a region" before clicking on "Create app".
 - Go to "Config Vars" under the "Settings" tab.
 - Click on "Reveals Config Vars" and add the KEY: CREDS and the VALUE stored in creds.json file if needed.
 - Add the Config Var, KEY: PORT and VALUE: 8000.
 - Go to "Buildpacks" section and click "Add buildpack".
 - Select "python" and click "Save changes"
 - Add "nodejs" buildpack as well using the same process.
 - Go to "Deployment method", under the "Deploy" tab select "GitHub" and click on "Connect to GitHub".
 - Go to "Connect to GitHub" section and "Search" the repository to be deployed.
 - Click "Connect" next the repository name.
- Choose "Automatic deploys" or "Manual deploys" to deploy your application.

[Back to top](#Overview)


# Testing

Please see the [testing](testing.md) page for details. 


# Credits

## Content
 - The Hangman banner ascii art came from [ascii.co.uk](https://ascii.co.uk/)
 - The Hangman ascii images came from [Chris Horton](https://gist.github.com/chrishorton/2624db0a0e82102bef769deb46971a47).
 - The colours used in the application came from [Colorama](https://pypi.org/project/colorama/)
 - The wordlists came from [hangmanwords](https://www.hangmanwords.com/words) and [randon word generator](https://www.randomlists.com/random-words)

 ## Resources
  Resources that were used learning how to develop this hangman application:
  - [Code Institute](https://codeinstitute.net/ie/) Code Institute Python module for python and OOP concepts.
  - [W3schools](https://www.python.org/) was referenced to check syntax.
  - [geeksforgeeks](https://www.geeksforgeeks.org/print-colors-python-terminal/) for bringing color text to the console.
  - [Net Ninja](https://www.youtube.com/watch?v=Ozrduu2W9B8&list=PL4cUxeGkcC9idu6GZ8EU_5B6WpKTdYZbK) to review concepts.
  - [Angela Yu Udemy](https://udemy.com) for the hangman idea and tutorials to bring concepts into practice including a simple version of hangman. 

## Acknowledgements

The Hangman word game was built as my Portfolio 3 Project for the Full Stack Software Developer (e-Commerce) Diploma at the [Code Institute](https://codeinstitute.net/ie/). I would like to thank my cohort facilitator [Kasia Bogucka](https://github.com/bezebee), my mentor [Precious Leige](https://www.linkedin.com/in/precious-ijege-908a00168/), the Code institue Slack community and the Code institute team for the help and support provided to me throughout this project. 

[Back to top](#Overview)
