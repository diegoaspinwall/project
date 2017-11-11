#Diego Aspinwall
#11-1-17
#hangmanGraphics.py - the second best game ever

from random import randint
from ggame import *

#colors and line color
black = Color(0x000000,1)
green = Color(0x00ff00,1)
red = Color(0xff0000,1)
white = Color(0xffffff,1)
blackline = LineStyle(4,black)
    
#names things that are always there
floor = RectangleAsset(300,100,blackline, white)
beamup = RectangleAsset(50,275,blackline, white)
beamright = RectangleAsset(200,50,blackline, white)
deathrope = LineAsset(0,40,blackline)
underline = LineAsset(40,0,blackline)
armp = LineAsset(20,40,blackline)
armp2 = LineAsset(-20,40,blackline)
headp = EllipseAsset(30,40,blackline,white)
torsop = LineAsset(0,50,blackline)
legp = LineAsset(-20,40,blackline)
legp2 = LineAsset(20,40,blackline)
eyep = LineAsset(10,10,blackline)
eyep2 = LineAsset(-10,10,blackline)
mouthp = LineAsset(25,0,blackline)

head = Sprite(headp, (200,100))
arm2 = Sprite(armp2, (200,10))
arm = Sprite(armp, (200,10))
torso = Sprite(torsop, (200,10))
leg = Sprite(legp, (200,10))
leg2 = Sprite(legp2, (200,10))
eye1 = Sprite(eyep, (185,10))
eye2 = Sprite(eyep2, (195,10))
eye3 = Sprite(eyep, (205,10))
eye4 = Sprite(eyep2, (215,10))
mouth = Sprite(mouthp, (188,10))

headstop = 100
arm2stop = 150
armstop = 150
torsostop = 150
legstop = 200
leg2stop = 200
eye1stop = 85
eye2stop = 85
eye3stop = 85
eye4stop = 85
mouthstop = 120


#moves the hangman into place
def moveObject(object, objectystop):
    data['directiony'] = 1
    while object.y < objectystop:
        object.y += data['directiony']


#Should take no arguments. The function should choose a random word.
def pickWord():
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

#Should take no arguments. The function should return True if all the letters in the word have been guessed and False otherwise.
def wordComplete():
    letters = 0
    for ch in data['word']:
        if ch in data['guessed']:
            letters += 1
    if letters == len(data['word']):
        return True
    else:
        return False

#Should take one argument, the number of incorrect guesses. The function should print out a new part of the body based on how many wrong guesses have occurred.
def printHangman(incguesses):
    if incguesses==1:
        moveObject(head, headstop)
    if incguesses==2:
        moveObject(arm2, arm2stop)
    if incguesses==3:
        moveObject(arm, arm2stop)
    if incguesses==4:
        moveObject(torso, torsostop)
    if incguesses==5:
        moveObject(leg, legstop)
    if incguesses==6:
        moveObject(leg2, leg2stop)
        moveObject(eye1, eye1stop)
        moveObject(eye2, eye2stop)
        moveObject(eye3, eye3stop)
        moveObject(eye4, eye4stop)
        moveObject(mouth, mouthstop)
        data['endgame'] += 1

#Should take one argument, event. The function should fill in the letter in the word if it was a correct guess and print the letter in the list of all letters that have been guessed.
def keyPress(event):
    #if the hangamn isn't complete, keep playing
    if data['endgame'] == 0:
        #records the incorrect guesses in incguesses after every keyPress and displays the printHangman
        if event.key not in data['guessed'] and event.key not in data['word']:
            data['incguesses'] += 1
            printHangman(data['incguesses'])
        
        #checks for wordComplete every keyPress
        if wordComplete() == True:
            Sprite(TextAsset('You Win!',fill=green,style='bold 60pt Times'), (250,200))
            data['endgame'] -= 1
        
        #displays the guessedbank with every keyPress
        if event.key not in data['guessed']:
            data['guessed'] += event.key+' '
        guessedbank = TextAsset(data['guessed'],fill=black,style='bold 30pt Times')
        Sprite(guessedbank, (500,25))
        
        #displays letter in below that user correctly gets
        if event.key in data['word']:
            place = 0
            for ch in data['word']:
                place +=1
                if ch == event.key:
                    Sprite(TextAsset(event.key,fill=black,style='bold 30pt Times'), (((60)*place-50),450))
    
    #if the hangman is complete sprite the answer and end game
    if data['endgame'] == 1:
        place = 0
        for ch in data['word']:
            place += 1
            Sprite(TextAsset(ch,fill=red,style='bold 30pt Times'), (((60)*place-50),450))


#runs game
if __name__ == '__main__':
    
    #dictionaries
    data = {}
    data['guessed'] = ''
    data['incguesses'] = 0
    data['word'] = pickWord()
    data['endgame'] = 0
    data['directiony'] = 1

    #sprites things that are always there
    Sprite(floor, (50,300))
    Sprite(beamup, (50,25))
    Sprite(beamright, (50,0))
    Sprite(deathrope, (200,50))    
    
    #sprites the underlines, each word has different number
    for i in range(0,len(data['word'])):
        Sprite(underline, (((60)*i),500))
            
        #listens for keys
        for ch in 'abcdefghijklmnopqrstuvwxyz':
            App().listenKeyEvent('keydown',ch,keyPress)
        App().run(step)
