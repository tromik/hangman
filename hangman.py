import random

# Generate a word list
# Randomly pick from the word list
# Get length of word and output blanks (e.g. 'zipper' > '_ _ _ _ _ _')
# Get letter guess from player
# Check word for letter, if exists populate with letter
# If guess is not in word begin to draw the hangman (player gets 7 guess, 8th ends the game in lose state)
# If player guesses the word within 8 guesses they win


# Create word list
word_list = ['stop', 'helmet', 'remote', 'board',
    'book', 'bookstore', 'animal', 'computer', 'keyboard', 'lampshade', 'speaker']

# Generate the hangman
# Temp - Using states
hang_man = ['1', '2', '3', '4', '5', '6', '7', '8']

def getRandomWord(word_list):
    # Randomly select word from word list and store
    word = word_list[random.randint(0, len(word_list) - 1)]
    print "Word is " + word + "\n"
    return word

def displayGame(hang_man, missed_letters, correct_letters, secret_word):
    print hang_man[len(missed_letters) - 1]
    print ''

    print "Missed letters: "
    for letter in missed_letters:
        print letter,
    print ''

    blanks = '_ ' * len(secret_word)

    for i in range(len(secret_word)):
        if secret_word[i] in correct_letters:
            blanks = blanks[:i] + secret_word[i] + blanks[i + 1:]

    for letter in blanks:
        print letter,

    print ''

def getGuess(already_guessed):
    while True:
        guess = raw_input("Guess a letter: ").lower()
        if len(guess) != 1:
            print "Please guess a single letter"
        elif guess in already_guessed:
            print "You've already guessed that letter, please guess again"
        elif guess not in 'qwertyuiopasdfghjklzxcvbnm':
            print "Please guess a letter"
        else:
            return guess

def playAgain():
    play_again = raw_input("Do you want to again? (Yes or No): ")
    if play_again.lower()[0] == 'y':
        return play_again

print "H A N G M A N"
missed_letters = ''
correct_letters = ''
secret_word = getRandomWord(word_list)
game_over = False

while TRUE:
    displayGame(hang_man, missed_letters, correct_letters, secret_word)

    guess = getGuess(missed_letters + correct_letters)
