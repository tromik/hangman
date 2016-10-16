import random

# Generate a word list
# Randomly pick from the word list
# Get length of word and output blanks (e.g. 'zipper' > '_ _ _ _ _ _')
# Get letter guess from player
# Check word for letter, if exists populate with letter
# If guess is not in word begin to draw the hangman (player gets 7 guess, 8th ends the game in lose state)
# If player guesses the word within 8 guesses they win

hang_man = ['0', '1', '2', '3', '4', '5', '6', '7', '8']

word_list = ['animal', 'toothbrush', 'bookstore']

secret_word = word_list[random.randint(0, len(word_list) - 1)]

blank = '_ ' * len(secret_word)

print blank

counter = 0
already_guessed = ''

def getGuess():
    guess = raw_input("Enter a guess: ").lower()
    while len(guess) != 1 or guess not in 'qwertyuiopasdfghjklzxcvbnm':
        print 'One letter from the alaphabet please.'
        guess = getGuess()
    return guess

def checkGuess_Word(guess):
    if guess in secret_word:
        return True
    return False

def checkGuess_Guessed(guess):
    if guess in already_guessed:
        return True
    return False

while counter < 8:
    guess = getGuess()
    while checkGuess_Guessed(guess):
        print 'You already guessed {}'.format(guess)
        guess = getGuess()
    if checkGuess_Word(guess):
        print 'Guess good'
        char_counter = 0
        for char in secret_word:
            if char == guess:
                blank = blank[:char_counter*2] + char + ' ' + blank[2*char_counter+2:]
            char_counter = char_counter + 1
        if blank.replace(' ', '') == secret_word:
            print "Congrats"
            break
        else:
            print blank
    else:
        counter = counter + 1
        print hang_man[counter]

    already_guessed = already_guessed + guess

print 'The word was ' + secret_word
