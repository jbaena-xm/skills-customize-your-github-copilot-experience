
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a classic Hangman game in Python using strings, loops, conditionals, and user input. By the end of this assignment, you will create a playable terminal game where users guess letters to reveal a hidden word before running out of attempts.

## 📝 Tasks

### 🛠️	Create the Hangman Game Setup

#### Description
Define the game data and initialize the core game state. Use a predefined word list, select one word at random, and prepare variables that track guessed letters and remaining incorrect attempts.

#### Requirements
Completed program should:

- Include a predefined list of possible words
- Randomly select one word from the list at the start of the game
- Initialize and track incorrect guesses remaining
- Initialize and store player guesses for later checks


### 🛠️	Implement the Gameplay Loop

#### Description
Build the loop that accepts one-letter guesses, updates the displayed progress, and checks for win or loss conditions after each turn.

#### Requirements
Completed program should:

- Accept letter guesses from the player
- Display current word progress in hidden-letter format (for example, `_ _ _`)
- Reduce remaining attempts for incorrect guesses
- End the game when the full word is guessed or attempts reach zero
- Display a clear win message when the player succeeds
- Display a clear lose message when the player runs out of attempts
