from __future__ import print_function
import numpy

#All the default gameboard pieces
gameBoard = ["_________"," |/      "," |       "," |       ", " |      "," |       "," |       "," |       "]

#list of words
wordList = ["AWKWARD","BAGPIPES","BANJO","BUNGLER","CROQUET","CRYPT","FJORD","GYPSY","HAPHAZARD","JAZZY","KAYAK","MEMENTO","NUMBSKULL","PHLEGM","QUAD", "RHYTHMIC","SPHINX","SWIVEL","TWELFTH","UNZIP","WAXY","YACHT","ZEALOUS","ZIPPY"]

#variable checking for the number of correct guesses. Resets to zero at the end of each loop
correctGuesses = 0

#empty lists, changed during the game to contain necessary content
guessLetters = []
blanks = []

#function that prints the board dependent on the number of guesses.
def Board(guesses):
    if guesses == 0:
        print (gameBoard[0],gameBoard[1],gameBoard[2],gameBoard[3],gameBoard[4],gameBoard[5],gameBoard[6],gameBoard[7], sep='\n')
    elif guesses == 1:
        print (gameBoard[0]," |/   |  ",gameBoard[2],gameBoard[3],gameBoard[4],gameBoard[5],gameBoard[6],gameBoard[7], sep='\n')
    elif guesses == 2:
        print (gameBoard[0]," |/   |  "," |   (_)",gameBoard[3],gameBoard[4],gameBoard[5],gameBoard[6],gameBoard[7], sep='\n')
    elif guesses == 3:
        print (gameBoard[0]," |/   |  "," |   (_)"," |    |   ",gameBoard[4],gameBoard[5],gameBoard[6],gameBoard[7], sep='\n')
    elif guesses == 4:
        print (gameBoard[0]," |/   |  "," |   (_)"," |   /|   ",gameBoard[4],gameBoard[5],gameBoard[6],gameBoard[7], sep='\n')
    elif guesses == 5:
        print (gameBoard[0]," |/   |  "," |   (_)"," |   /|\ ",' |    | ',gameBoard[5],gameBoard[6],gameBoard[7], sep='\n')
    elif guesses == 6:
        print (gameBoard[0]," |/   |  "," |   (_)"," |   /|\ ",' |    | '," |   /     ",gameBoard[6],gameBoard[7], sep='\n')
    elif guesses == 7:
        print (gameBoard[0]," |/   |  "," |   (_)"," |   /|\ ",' |    | '," |   / \  ",gameBoard[6],gameBoard[7], sep='\n')
    #printing blanks and filled in letters
    print ('%s' % ' '.join(map(str, blanks)))

#function that grabs a random word from the word list
def randomWord(dictionary):
    return numpy.random.choice(dictionary)
gameWord = randomWord(wordList)

#sticking each character in the randomly selected word in one of the blank lists
for char in gameWord:
    guessLetters.append(char)

#creating the blanks dependent on how many characters are in the random word
for char in gameWord:
    blanks.append('__')

#variable that controls how many false guesses the player gets
guesses = 0
#welcoming print
print ("WELCOME TO HANGMAN")

#print(gameWord)
#debug print

#Actual game stuff
while guesses < 7:
    #prints out the board
    Board(guesses)
    #guess goes here
    guessedLetter = raw_input("Please enter your guess: ")
    #if guesses aren't valid
    if len(guessedLetter) != 1:
        print("Guess is not valid.")
        continue
    #checks if guess is correct
    for i in range(len(guessLetters)):
        if guessedLetter.upper() == guessLetters[i]:
            blanks[i] = guessLetters[i]
            guesses = guesses - 1
            continue
    #checks if all blanks are filled
    for i in range(len(blanks)):
        if blanks[i] != '__':
            correctGuesses += 1
    #if all blanks are filled, ends the game
    if correctGuesses == len(blanks):
        print("You win!")
        break
    #ensuring that all false guesses cause the guesses variable to increment
    guesses += 1
    #sets the variable correctGuesses to 0 to prep for the next loop
    correctGuesses = 0
else:
    #finishes game if you lose
    Board(guesses)

    print("You lose!")
    print("The word was %s!" % gameWord)




