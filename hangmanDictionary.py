#Diego Aspinwall
#12-6-17
#hangmanDictionary.py - the second best game ever

dictionary = open('engmix.txt')

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
arm = LineAsset(20,40,blackline)
arm2 = LineAsset(-20,40,blackline)
head = EllipseAsset(30,40,blackline,white)
torso = LineAsset(0,50,blackline)
leg = LineAsset(-20,40,blackline)
leg2 = LineAsset(20,40,blackline)
eye = LineAsset(10,10,blackline)
eye2 = LineAsset(-10,10,blackline)
mouth = LineAsset(25,0,blackline)

#Should take no arguments. The function should choose a random word.
def pickWord():
    return(dictionary[randint(0,84099)].strip())

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
        App().run()
