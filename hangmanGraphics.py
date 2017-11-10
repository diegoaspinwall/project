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

def wordComplete(): #Should take no arguments. The function should return True if all the letters in the word have been guessed and False otherwise.
    for ch in data['word']:
        if ch in data['guessed']:
            return True
        else:
            return False
            break

def printHangman(incguesses): #Should take one argument, the number of incorrect guesses. The function should print out a new part of the body based on how many wrong guesses have occurred.
    arm = LineAsset(20,40,blackline)
    arm2 = LineAsset(-20,40,blackline)
    head = EllipseAsset(30,40,blackline,white)
    torso = LineAsset(0,50,blackline)
    leg = LineAsset(-20,40,blackline)
    leg2 = LineAsset(20,40,blackline)
    if incguesses==1:
        Sprite(head, (200,100))
    if incguesses==2:
        Sprite(arm2, (200,150))
    if incguesses==3:
        Sprite(arm, (200,150))
    if incguesses==4:
        Sprite(torso, (200,150))
    if incguesses==5:
        Sprite(leg, (200,200))
    if incguesses==6:
        Sprite(leg2, (200,200))

def keyPress(event): #Should take one argument, event. The function should fill in the letter in the word if it was a correct guess and print the letter in the list of all letters that have been guessed.
    #records the incorrect guesses in incguesses and prints the hangman
    if event.key not in data['guessed'] and event.key not in data['word']:
        data['incguesses'] += 1
        printHangman(data['incguesses'])
    
    #checks for wordComplete every keyPress
    if wordComplete() == True:
        print('You win!')
    
    #displays the guessedbank
    if event.key not in data['guessed']:
        data['guessed'] += event.key+' '
    guessedbank = TextAsset(data['guessed'],fill=black,style='bold 30pt Times')
    Sprite(guessedbank, (500,25))
    
    #displays letter in word that user correctly gets
    if event.key in data['word']:
        place = 0
        for ch in data['word']:
            place +=1
            if ch == event.key:
                Sprite(TextAsset(event.key,fill=black,style='bold 30pt Times'), (((60)*place-50),450))



if __name__ == '__main__':
    
    data = {}
    data['guessed'] = ''
    data['incguesses'] = 0
    data['word'] = pickWord()
    
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
    
    if wordComplete() == True:
        print('You win!')
    
    for i in range(0,len(data['word'])):
        Sprite(underline, (((60)*i),500))
    
    Sprite(floor, (50,300))
    Sprite(beamup, (50,25))
    Sprite(beamright, (50,0))
    Sprite(deathrope, (200,50))
    
    for ch in 'abcdefghijklmnopqrstuvwxyz':
        App().listenKeyEvent('keydown',ch,keyPress)
    App().run()
