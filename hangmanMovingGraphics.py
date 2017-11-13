#Diego Aspinwall
#11-1-17
#hangmanGraphics.py - the second best game ever

'''Mr Smedinghoff - this is my "moving graphics" version of the hangman program. The other one, placed in the same
folder is more concise. Note: I created "thing" so that the step would be doing something before the user puts a 
letter in. Also, don't click two wrong letters in short succession, because the poor guy falls apart -Diego'''

from random import randint
from ggame import *

#colors and line color
black = Color(0x000000,1)
green = Color(0x00ff00,1)
red = Color(0xff0000,1)
white = Color(0xffffff,1)
blackline = LineStyle(4,black)
    
#names things
floor = RectangleAsset(300,100,blackline, white)
beamup = RectangleAsset(50,275,blackline, white)
beamright = RectangleAsset(200,50,blackline, white)
deathrope = LineAsset(0,10,blackline)
underline = LineAsset(40,0,blackline)
armp = LineAsset(20,40,blackline)
armp2 = LineAsset(-20,40,blackline)
headp = EllipseAsset(30,40,blackline,white)
torsop = LineAsset(0,50,blackline)
legp = LineAsset(-20,40,blackline)
legp2 = LineAsset(20,40,blackline)
eye = LineAsset(10,10,blackline)
eye2 = LineAsset(-10,10,blackline)
mouth = LineAsset(25,0,blackline)
thingp = LineAsset(5,5,LineStyle(1, white))

#sprites things
head = Sprite(headp, (200,10))
arm2 = Sprite(armp2, (200,10))
arm = Sprite(armp, (200,10))
torso = Sprite(torsop, (200,10))
leg = Sprite(legp, (200,10))
leg2 = Sprite(legp2, (200,10))
thing = Sprite(thingp)

#when to stop moving
headstop = 100
arm2stop = 150
armstop = 150
torsostop = 150
legstop = 200
leg2stop = 200
thingstop = 400


#moves the hangman into place
def step():
    if data['object'].y < data['objectystop']:
        data['object'].y += 1

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
        data['object'] = head
        data['objectystop'] = headstop
    if incguesses==2:
        data['object'] = arm2
        data['objectystop'] = arm2stop
    if incguesses==3:
        data['object'] = arm
        data['objectystop'] = armstop
    if incguesses==4:
        data['object'] = torso
        data['objectystop'] = torsostop
    if incguesses==5:
        data['object'] = leg
        data['objectystop'] = legstop
    if incguesses==6:
        data['object'] = leg2
        data['objectystop'] = leg2stop
        Sprite(eye, (185,85))
        Sprite(eye2, (195,85))
        Sprite(eye, (205,85))
        Sprite(eye2, (215,85))
        Sprite(mouth, (188,120))
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
            if ch not in data['guessed']:
                Sprite(TextAsset(ch,fill=red,style='bold 30pt Times'), (((60)*place-50),450))


#runs game
if __name__ == '__main__':
    
    #dictionaries
    data = {}
    data['guessed'] = ''
    data['incguesses'] = 0
    data['word'] = pickWord()
    data['endgame'] = 0
    data['object'] = thing
    data['objectystop'] = thingstop

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
