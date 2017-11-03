#Diego Aspinwall
#11-1-17
#hangmanGraphics.py - the second best game ever

from random import randint
from ggame import *

def pickWord(): #Should take no arguments. The function should choose a random word. My program had five random words to chose from, but yours can have more if you like.
    rword = randint(1,6)
    if rword == 1:
        return 'computer'
    if rword == 2:
        return 'kernighan'
    if rword == 3:
        return 'binary'
    if rword == 4:
        return 'brython'
    if rword == 5:
        return 'programming'
    if rword == 6:
        return 'boolean'
"""    
def wordComplete(): #Should take no arguments. The function should return True if all the letters in the word have been guessed and False otherwise.
    

def printHangman(incguesses): #Should take one argument, the number of incorrect guesses. The function should print out a new part of the body based on how many wrong guesses have occurred.
    
"""
def keyPress(event): #Should take one argument, event. The function should fill in the letter in the word if it was a correct guess and print the letter in the list of all letterers that have been guessed.
    print(event.key)


if __name__ == '__main__':
    
    data = {}
    
    word = pickWord()
    
    black = Color(0x000000,1)
    green = Color(0x00ff00,1)
    red = Color(0xff0000,1)
    white = Color(0xffffff,1)
    
    blackline = LineStyle(4,black)
    
    floor = RectangleAsset(300,100,blackline, white)
    beamup = RectangleAsset(50,275,blackline, white)
    beamright = RectangleAsset(200,50,blackline, white)
    deathrope = LineAsset(0,40,blackline)
    underline = LineAsset(40,0,blackline)
    
    for i in range(0,len(word)):
        Sprite(underline, (((10+50)*i),500))
    
    Sprite(floor, (50,300))
    Sprite(beamup, (50,25))
    Sprite(beamright, (50,0))
    Sprite(deathrope, (200,50))
    
    for ch in 'abcdefghijklmnopqrstuvwxyz':
        App().listenKeyEvent('keydown',ch,keyPress)
    App().run()

#Useful detail - event.key contains the key that was pressed to trigger the key press function. You will need to listen for 26 different keys (use a loop to shorten this code!)

