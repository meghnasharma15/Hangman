import random
import sqlite3
from tabulate import tabulate

word_sets = {
    "Animals": 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split(),
    "Shapes": 'circle square triangle rectangle oval rhombus trapezoid pentagon hexagon octagon'.split(),
    "Places": 'paris london tokyo newyork sydney mumbai toronto dubai berlin madrid'.split()
}

HANGMAN_PICS = ['''
  +---+
      |
      |
      |
     ===''', '''
  +---+
  O   |
      |
      |
     ===''', '''
  +---+
  O   |
  |   |
      |
     ===''', '''
  +---+
  O   |
 /|   |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
 /    |
     ===''', '''
  +---+
  O   |
 /|\  |
 / \  |
     ===''', '''
  +---+
 [O   |
 /|\  |
 / \  |
     ===''', '''
  +---+
 [O]  |
 /|\  |
 / \  |
     ===''']

words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()


def getRandomWord(wordList):
    # This function returns a random string from the passed list of strings.
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]


def display_intro():
    print("Welcome to the game of Hangman!")
    print("You have to guess the secret word one letter at a time.")
    print("You can make a limited number of incorrect guesses before you lose.")
    print("Let's get started!")

def about_the_game():
    about_text = [
        ["Easy",
         "The user can select the list from which the random word will be selected (Animal, Shape, Place). This will make it easier to guess the secret word. Also, the number of trials will be increased from 6 to 8."],
        ["Moderate",
         "Similar to Easy, the user can select the set from which the random word will be selected (Animal, Shape, Place) but the number of trials will be reduced to 6. The last two graphics will not be used or displayed."],
        ["Hard",
         "The code will randomly select a set of words. From this set, the code will randomly select a word. The user will have no clue about the secret word. Also, the number of trials will remain at 6."]
    ]
    print("ABOUT THE GAME")
    print(tabulate(about_text, headers=["Level", "Description"], tablefmt="grid"))


def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print('Missed letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)):  # Replace blanks with correctly guessed letters.
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i + 1:]

    for letter in blanks:  # Show the secret word with spaces in between each letter.
        print(letter, end=' ')
    print()



def getGuess(alreadyGuessed):
    # Returns the letter the player entered. This function makes sure the player entered a single letter and not something else.
    while True:
        print('Guess a letter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess


def playAgain():
    # This function returns True if the player wants to play again; otherwise, it returns False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')


def select_level(level):
    while True:
        print("\nSelect Level of Challenge")
        print("1. Easy")
        print("2. Moderate")
        print("3. Hard")

        choice = input("Please select a level (1-3): ",).strip()

        if choice == '1':
            return 'Easy'
        elif choice == '2':
            return 'Moderate'
        elif choice == '3':
            return 'Hard'
        else:
            print("Invalid choice, please select again.")


def select_word_set(level):
    while True:
        print("\nSELECT FROM THE FOLLOWING SETS OF SECRET WORDS")
        print("1. Animals")
        print("2. Shapes")
        print("3. Places")
        choice = input("Please select a set (1-3): ").strip()
        if choice in ['1', '2', '3']:
            return list(word_sets.values())[int(choice) - 1]  # Corrected to access values by index
        else:
            print("Invalid choice, please select again.")


def play_game(player_name, level):
    if level == 'Easy':
        word_set = select_word_set(level)
        max_trials = 8
        hangman_pics = HANGMAN_PICS
    elif level == 'Moderate':
        word_set = select_word_set(level)
        max_trials = 6
        hangman_pics = HANGMAN_PICS[:6]
    elif level == 'Hard':
        word_set = random.choice(list(word_sets.values()))
        max_trials = 6
        hangman_pics = HANGMAN_PICS[:6]

    secret_word = getRandomWord(word_set)
    missed_letters = []
    correct_letters = []
    wrong_attempts = 0

    while wrong_attempts < max_trials:
        displayBoard(missed_letters, correct_letters, secret_word)
        guess = getGuess(missed_letters + correct_letters)

        if guess in secret_word:
            correct_letters.append(guess)
        else:
            missed_letters.append(guess)
            wrong_attempts += 1

        if all(letter in correct_letters for letter in secret_word):
            print(f"Congratulations, you guessed the word: {secret_word}")
            remaining_lives = max_trials - wrong_attempts
            update_hall_of_fame(player_name, level, remaining_lives)
            break
    else:
        print(f"Sorry, you've run out of lives. The word was: {secret_word}")

    play_again = input("Would you like to play again? (yes/no): ").lower()
    if play_again.startswith('y'):
        return True
    else:
        return False



def setup_database():
    conn = sqlite3.connect('hangman.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS hall_of_fame (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        level TEXT NOT NULL,
        remaining_lives INTEGER NOT NULL
    )''')
    conn.commit()
    conn.close()


def update_hall_of_fame(player_name, level, remaining_lives):
    conn = sqlite3.connect('hangman.db')
    cursor = conn.cursor()
    cursor.execute('''
    SELECT remaining_lives FROM hall_of_fame WHERE level=? ORDER BY remaining_lives DESC LIMIT 1''', (level,))
    row = cursor.fetchone()

    if row is None or remaining_lives > row[0]:
        cursor.execute('''
        INSERT INTO hall_of_fame (name, level, remaining_lives)
        VALUES (?, ?, ?)''', (player_name, level, remaining_lives))
        conn.commit()
    conn.close()


def display_hall_of_fame():
    conn = sqlite3.connect('hangman.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM hall_of_fame')
    records = cursor.fetchall()
    if records:
        print("HALL OF FAME")
        table = [[record[1], record[2], record[3]] for record in records]
        print(tabulate(table, headers=["Winner Name", "Level", "Remaining Lives"], tablefmt="grid"))
    else:
        print("No records found in the Hall of Fame.")
    conn.close()


def main():
    setup_database()
    player_name = input("Please enter your name: ").strip()
    while True:
        menu_options = [["1", "Easy level"], ["2", "Moderate level"], ["3", "Hard level"], ["4", "Hall of Fame"], ["5", "About the Game"], ["6", "Exit"]]
        print(f"\nHi {player_name}.\nWelcome to HANGMAN\n")
        print("PLAY THE GAME\n")
        print(tabulate(menu_options, headers=["Option", "Description"], tablefmt="grid"))
        choice = input("Please select an option (1-6): ").strip()
        if choice == '1':
            if not play_game(player_name, 'Easy'):
                break
        elif choice == '2':
            if not play_game(player_name, 'Moderate'):
                break
        elif choice == '3':
            if not play_game(player_name, 'Hard'):
                break
        elif choice == '4':
            display_hall_of_fame()
        elif choice == '5':
            about_the_game()
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please select again.")

if __name__ == "__main__":
    main()



