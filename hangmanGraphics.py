#Diego Aspinwall
#11-1-17
#hangmanGraphics.py - the second best game ever

from random import randint
from ggame import *
"""
def pickWord(): #Should take no arguments. The function should choose a random word. My program had five random words to chose from, but yours can have more if you like.
    rword = randint(1,6)
    if rword = 1:
        word = 'computer'
    if rword = 2:
        word = 'pneumonoultramicroscopicsilicovolcanoconiosis'
    if rword = 3:
        word = 'floccinaucinihilipilification'
    if rword = 4:
        word = 'antidisestablishmentarianism'
    if rword = 5:
        word = 'pseudopseudohypoparathyroidism'
    if rword = 6:
        word = 'spectrophotofluorometrically'
    
def wordComplete(): #Should take no arguments. The function should return True if all the letters in the word have been guessed and False otherwise.
    wordchar = len(word)

def printHangman(incguesses): #Should take one argument, the number of incorrect guesses. The function should print out a new part of the body based on how many wrong guesses have occurred.
    

def keyPress(event): #Should take one argument, event. The function should fill in the letter in the word if it was a correct guess and print the letter in the list of all letterers that have been guessed.
    
"""
if __name__ == '__main__':
    
    data = {}
    
    
    black = Color(0x000000,1)
    green = Color(0x00ff00,1)
    red = Color(0xff0000,1)
    white = Color(0xffffff,1)
    
    floor = RectangleAsset(300,100,LineStyle(4,black), white)
    beamup = RectangleAsset(50,300,LineStyle(4,black), white)
    
    Sprite(floor, (50,300))
    Sprite(beamup, (50,0))
    App().run()




