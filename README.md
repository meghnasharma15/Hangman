# Hangman Game

## Overview
This Hangman game is a command-line implementation of the classic word-guessing game. Players can select from different levels of difficulty and categories of words. The game tracks high scores and displays a "Hall of Fame" for top performers. This project uses Python for the game logic and SQLite for storing high scores. The game interface is enhanced with the `tabulate` library for better formatting of menus and tables.

## Features

### Introductory Menu
- When running the code, the user is asked to provide their name.
- An introductory menu appears, allowing the user to select the level of challenge, explore the Hall of Fame, and read instructions about the game.
- This menu reappears at the end of the game if the user chooses to play again.

### Levels of Difficulty
- **Easy**: Users can select the category (Animals, Shapes, Places) from which the random word will be chosen. They get 8 attempts to guess the word.
- **Moderate**: Similar to Easy, but users get only 6 attempts.
- **Hard**: The word is selected randomly from all categories, and users have 6 attempts to guess the word.

### Word Categories
Users can choose from categories like Animals, Shapes, and Places for the Easy and Moderate levels.

### Hall of Fame
- Displays a list of top performers with their names, levels, and remaining lives.
- Uses the `tabulate` library to present the information in a formatted table.

### About the Game
Provides detailed instructions about the game, levels of difficulty, and the Hall of Fame.

## Requirements
- Python 3.x
- `tabulate` library
- `sqlite3` library (included with Python)

## Installation
1. Clone this repository to your local machine.
2. Navigate to the project directory.
3. Install the `tabulate` library using pip:
    ```bash
    pip install tabulate
    ```

## How to Play
1. Run the `main.py` file.
    ```bash
    python main.py
    ```
2. Enter your name when prompted.
3. Choose an option from the menu:
    - Select a difficulty level to start the game.
    - View the Hall of Fame.
    - Read about the game.
4. If you choose to play, follow the prompts to guess the letters of the secret word.
5. At the end of each game, you can choose to play again or exit.

## Project Structure
- `main.py`: The main script to run the game.
- `hangman.db`: SQLite database file to store the Hall of Fame records (created automatically).

## Code Description
### `main.py`
- **Libraries Imported**:
    - `random`: For random word selection.
    - `sqlite3`: For database operations.
    - `tabulate`: For formatting tables in the console.

- **Functions**:
    - `getRandomWord(wordList)`: Returns a random word from the provided list.
    - `display_intro()`: Displays the introductory text for the game.
    - `displayBoard(missedLetters, correctLetters, secretWord)`: Displays the current state of the game board.
    - `getGuess(alreadyGuessed)`: Prompts the user for a letter and validates the input.
    - `play_game(player_name, level)`: Main game loop for playing a single round.
    - `setup_database()`: Sets up the SQLite database for storing high scores.
    - `update_hall_of_fame(player_name, level, remaining_lives)`: Updates the Hall of Fame with a new score.
    - `display_hall_of_fame()`: Displays the Hall of Fame in a formatted table.
    - `select_word_set(level)`: Allows the user to select a category of words.
    - `about_the_game()`: Displays information about the game and its rules.
    - `main()`: Main function to run the game, display menus, and handle user input.

## Future Improvements
- Add more categories of words.
- Implement a graphical user interface (GUI) for better user experience.
- Allow for multiplayer functionality.

## Contribution
Feel free to fork this repository, make improvements, and submit pull requests. Any contributions to enhance the game are welcome.

---

Enjoy playing Hangman! If you encounter any issues or have suggestions, please open an issue on the GitHub repository.
