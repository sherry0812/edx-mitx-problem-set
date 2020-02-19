import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    
    print('')
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    print('')
    
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)
    Returns a word from wordlist at random
    """
    
    return random.choice(wordlist)

# Load the list of words into the variable wordlist
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
    False otherwise
    '''
    correctGuessedNum = 0
    for letter in secretWord:
        if letter in lettersGuessed:
            correctGuessedNum += 1
    if correctGuessedNum == len(secretWord):
        return True
    else:
        return False

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
    what letters in secretWord have been guessed so far.
    '''
    correctGuessed = secretWord
    for letter in secretWord:
        if not letter in lettersGuessed:
           correctGuessed = correctGuessed.replace(letter, '_ ')

    return correctGuessed

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
    yet been guessed.
    '''
    alphabet = 'abcdefghijlmnopqrstuvwxyz'
    return alphabet.replace(''.join(lettersGuessed), '')   

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    n = len(secretWord)
    
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is ' + str(n) + ' letters long.')
    print('')
    print('------------------------------------------')

    guessesLeft = 10
    lettersGuessed = []
    
    while guessesLeft >= 0:
        
        if (isWordGuessed(secretWord, lettersGuessed) == True):
            print('Congratulations you won!')
            
            break
        
        else:
            
            if guessesLeft == 0:
                print('Sorry, you ran out of guesses. The word was ' + str(secretWord) + '.')
                print('')
                break
            
            else:
                
                letter = ''
                
                print('You have ' + str(guessesLeft) + ' guesses left.')
                print('Available letters: ' + str(getAvailableLetters(lettersGuessed)))
                letter = (input('Please guess a letter: '))
                
                if not letter in lettersGuessed:
                    lettersGuessed.append(letter)
                    if letter in secretWord:
                       
                        print('Good guess: ' + str(getGuessedWord(secretWord, lettersGuessed)))
                        print('')
                        print('------------------------------------------')
                        print('')
                    
                    else:
                        
                        print('Oops! That letter is not in my word: ' + str(getGuessedWord(secretWord, lettersGuessed)))
                        print('')
                        print('------------------------------------------')
                        print('')
                        guessesLeft -= 1
                else:
                    
                    print("Oops! You've already guessed that letter: " + str(getGuessedWord(secretWord, lettersGuessed)))
                    print('')
                    print('------------------------------------------')
                    print('')

secretWord = chooseWord(wordlist).lower()
hangman(secretWord) 
