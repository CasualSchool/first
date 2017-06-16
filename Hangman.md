Python Hangman
import numpy
gameBoard = ["_________"," |/      "," |       "," |       ", " |       "," |       "," |       "," |       "]

wordList = ["AWKWARD","BAGPIPES","BANJO","BUNGLER","CROQUET","CRYPT","FJORD","GYPSY","HAPHAZARD","JAZZY","KAYAK","MEMENTO","NUMBSKULL","PHLEGM"]

def Board(guesses):
    if guesses == 0:
        print gameBoard[0],gameBoard[1],gameBoard[2],gameBoard[3],gameBoard[4],gameBoard[5],gameBoard[6],gameBoard[7]
    elif guesses == 1:
        print gameBoard[0]," |/   |  ",gameBoard[2],gameBoard[3],gameBoard[4],gameBoard[5],gameBoard[6],gameBoard[7]
    elif guesses == 2:
        print gameBoard[0]," |/   |  "," |   (_)",gameBoard[3],gameBoard[4],gameBoard[5],gameBoard[6],gameBoard[7]
    elif guesses == 3:
        print gameBoard[0]," |/   |  "," |   (_)"," |    |   ",gameBoard[4],gameBoard[5],gameBoard[6],gameBoard[7]
    elif guesses == 4:
        print gameBoard[0]," |/   |  "," |   (_)"," |   /|   ",gameBoard[4],gameBoard[5],gameBoard[6],gameBoard[7]
    elif guesses == 5:
        print gameBoard[0]," |/   |  "," |   (_)"," |   /|\ ",gameBoard[4],gameBoard[5],gameBoard[6],gameBoard[7]
    elif guesses == 6:
        print gameBoard[0]," |/   |  "," |   (_)"," |   /|\ ",gameBoard[4]," |   /     ",gameBoard[6],gameBoard[7]
    elif guesses == 7:
        print gameBoard[0]," |/   |  "," |   (_)"," |   /|\ ",gameBoard[4]," |   / \  ",gameBoard[6],gameBoard[7]

guesses = 0
print "WELCOME TO HANGMAN"

def randomWord(dictionary):
    return numpy.random.choice(dictionary)

Board(7)