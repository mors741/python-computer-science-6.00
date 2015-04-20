# 6.00 Problem Set 3
# 
# Hangman
#


# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

def current_word(word, choosen_letters):
    res = ""
    for char in word:
        if char in choosen_letters:
            res += char + " "
        else:
            res += "_ "
    return res

def is_fully_guessed(word, choosen_letters):
    for char in word:
        if char not in choosen_letters:
            return False
    return True

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()

print "Welcome to the game, Hangman!"
word = choose_word(wordlist)
print word #Debug
print "I am thinking of a word that is {} letters long.".format(len(word))
available = string.ascii_lowercase
guesses_left = 8
choosen_letters = ""
while guesses_left > 0:
    print "------------"
    print "You have {} guesses left.".format(guesses_left)
    print "Available letters:", available
    guess = raw_input("Please guess a letter: ").lower()
    if guess in available: #has not been choosen yet
        available = available.replace(guess, "")
        choosen_letters += guess
        if guess in word:
            print "Good guess:", current_word(word, choosen_letters)
            if is_fully_guessed(word, choosen_letters):
                break
        else:
            print "Oops! That letter is not in my word:", \
                  current_word(word, choosen_letters)
            guesses_left -= 1

    else:
        print "Sory, you have already tried this letter... Try another!"
       
print "------------"
if guesses_left == 0:
    print "Sorry, you lost..."
    print "The word was:", word
else:
    print "Congratulations, you won!"
    
