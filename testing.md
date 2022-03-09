# TESTING
 - Python code validation was checked.
 - Game functionality was tested to ensure the gameworked as expected.
 - Menu validation and functionality was tested to ensure they worked as expected.
 - User input was tested to ensure it was valid input.
 - User feedback messages were tested to ensure correct messages were returned to the user.

  ## Python Validation

  - PEP8 online validator was used to check python code was valid.
  - Warnings relating to line length, spaces between lines and trailing whitespace were displayed.
  - Once these warnings were addressed the code passed the pep8 validation check.

  ![pep8 validation](docs/readme-images/pep8.png)

[Back to top](#TESTING)


## Game functionality

 - The game was tested through development to ensure features worked as they were introduced.
 - The games features work as expected eg random word is generated and displayed correctly, letters display correctly, lives deduct accordingly, player wins or player loses all work as expected.
 - The game was tested by friends and family.
 - The game checked by peer code review. 

## Game input validation
 - User input validataion has been applied in the application.
 - Input validation was tested and works as expected.
 
 - eg user enters a charcter that is not a letter then feedback message is returned.
 ![invalid game input](docs/readme-images/input-one.png)

- eg user enters more than one charcter then feedback message is returned.
 ![invalid game input](docs/readme-images/input-two.png)


## Menu input validation

 - The menus on the landing page, instructions page, start play page, game over page all work as expected.
 - Input validation checks have been applied to the menus.
 - Feedback messages are returned to the user if they enter invalid input.
 - This ensures easy and intuitive navigation for the user with conistent styling.


   - Landing page menu validation:

 ![landing validation](docs/readme-images/landing-menu-msg.png)
  
   - Instructions page menu validation:

 ![instructions validation](docs/readme-images/instruction-menu-msg.png)
 
  - Start Play menu validation:

 ![start play validation](docs/readme-images/start-play-msg.png)
 
   - Game over menu validation:

 ![game over validation](docs/readme-images/game-over-msg.png)
 

# Bugs

## Resolved:
### PEP8
 - PEP8 warnings were encountered during the development process. 
 - These were minor issues and addressed accordingly. 
 - See python code validation section.

### Deployment

- When the application was deployed on the Heroku platform an error message occurred:
'ModuleNotFoundError: No module named 'colorama' 
- This was error was researched and the solution was found on slack.
- Manually adding colorama to the requirements.txt file resolved the issue.



## Unresolved