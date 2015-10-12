# Name: Frank Karunaratna
# Date: 3 June 2015
# File Name: HangmanGame.py
# Description: This program allows the user to play the game hangman with a
#              randomly selected word from the input file.

from button2 import *
from graphics import *
import random

def setupGUI(word):
    '''creates the main GUI'''

    global squareList,win,button_list,instruction,play_again,quitt,message,image

    win = GraphWin("Hangman Game",500,420)
    win.setBackground("thistle4")

    #Creates a list of all the alphabet buttons
    button_list = []

    alphabet_list = ["Q","W","E","R","T","Y","U","I","O","P"]
    alphaButtonList(alphabet_list,70,320,button_list)

    alphabet_list = ["A","S","D","F","G","H","J","K","L"]
    alphaButtonList(alphabet_list,90,340,button_list)

    alphabet_list = ["Z","X","C","V","B","N","M"]
    alphaButtonList(alphabet_list,130,360,button_list)

    buttonActivation(button_list)  

    #Creates a list with the names of the empty squares
    squareList = drawSquares(word)

    #Draws remaining elements on the screen
    instruction = Button(win,Point(110,400),120,20,"Instructions","pink4")
    instruction.activate()

    play_again = Button(win,Point(250,400),100,25,"Play Again","PaleVioletRed4")

    quitt = Button (win,Point(390,400),120,20,"Quit","pink4")
    quitt.activate()

    messageBox = Rectangle(Point(50,200),Point(450,240))
    messageBox.setWidth(3)
    messageBox.setFill("thistle3")
    messageBox.draw(win)

    message = Text (Point(250,220),"Choose a letter to begin")
    message.draw(win)

    rectangle = Rectangle(Point(196,54),Point(309,186))
    rectangle.setWidth(3)
    rectangle.setFill("white")
    rectangle.draw(win)

    image = Image(Point(250,120),"HangMan.gif")
    image.draw(win)

    title = Text(Point(250,25),"THE HANGMAN GAME")
    title.setSize(18)
    title.setStyle("bold")
    title.draw(win)

def main():
    '''runs the main program'''
    
    #Gets the random word
    word = getWord()

    #Draws the GUI
    setupGUI(word)

    #Waits for a mouse click
    pt = win.getMouse()

    #Counters for the correct guesses and wrong guesses
    errors = 0
    corrects = 0

    #Empty list where each letter in the word will be put into
    letters = []

    #Gets the anchor for the first letter in the word
    if len(word) % 2 == 0:
        letter_anchor = 280 - (40 * (len(word)//2))
    else:
        letter_anchor = 265 - (40 * ((len(word)-1)//2))

    #Creates a list, with each element being a list of the black squares
    #This is to make it easier to undraw the squares
    squareLists = [squareList]
    counter = 0

    #Main event loop
    while not quitt.clicked(pt):

        #Checks to see if a alphabet button has been clicked
        for but in button_list:
            
            if but.clicked(pt):
                correct = False
                
                for letter in range (len(word)):

                    #Checks if the letter clicked is in the word
                    if but.getLabel().lower() == word[letter]:
                        correct = True
                        corrects = corrects + 1

                        #Message box text changes
                        part1 = "Congratulations the letter "
                        part2 = " is in the word!"
                        
                        message.setText(part1 + word[letter].upper() + part2)

                        #Letter(s) are drawn to the window
                        textAnchor = Point(letter_anchor-15+40*letter,270)
                        
                        text = Text(textAnchor,word[letter].upper())
                        text.setStyle("bold")
                        text.draw(win)

                        #Text objects are added to a list so they can be easily
                        #undrawn when the play again button is pressed
                        letters.append(text)
                        

                if correct == False:
                    errors = errors + 1

                    #Message box text changes
                    part1 = "Sorry, the letter "
                    part2 = " is not in the word"
                    message.setText(part1 + but.getLabel() + part2 )

                    #Proper hangman image is displayed
                    image_list = ["HangMan2.gif","HangMan3.gif","HangMan4.gif",
                                  "HangMan5.gif","HangMan6.gif","HangMan7.gif"]
                    image = Image(Point(250,120), image_list[errors-1])
                    image.draw(win)

                if errors == 6:
                    #If 6 errors have been made all alphabet buttons are
                    #deactivated and the play again button is activated
                    for but in button_list:
                        but.deactivate()
                        
                    play_again.activate()
                    
                    part1 = "Sorry, you lost!\n"
                    part2 = "The word you were looking for was: "
                    message.setText(part1 + part2 + word.upper())

                #If the number of correct guesses equals the length of the word
                #they have correctly guesses the entire word and all the buttons
                #are deactivated
                if corrects == len(word):
                    
                    for but in button_list:
                        but.deactivate()

                    play_again.activate()
                    message.setText("Congratulations you won!")

                #Deactivates the letter button that was clicked
                but.deactivate()

        if play_again.clicked(pt):

            #Resets values to the original
            errors = 0
            corrects = 0
            play_again.deactivate()
            message.setText("Choose a letter to begin")

            #Draws original image
            image = Image(Point(250,120),"HangMan.gif")
            image.draw(win)

            #Reactivates letter buttons
            buttonActivation(button_list)

            #Undraws the letters
            objectUndraw(letters)

            letters = []

            #Undraws the square boxes
            objectUndraw(squareLists[counter])

            #Gets new word    
            word = getWord()

            #Creates a list with the square boxes
            squareList1 = drawSquares(word)
            squareLists.append(squareList1)
            counter = counter + 1

            #Gets the letter anchor
            if len(word) % 2 == 0:
                letter_anchor = 280 - (40 * (len(word)//2))
            else:
                letter_anchor = 265 - (40 * ((len(word)-1)//2))

        if instruction.clicked(pt):
            win2 = GraphWin("Instructions",300,250)

            #Calls the instructionsGUI
            instructionsGUI(win2)
            
            win2.getMouse()
            win2.close()

        #Waits for a mouse click
        pt = win.getMouse()

    win.close()

def instructionsGUI(win2):
    '''creates the instruction window'''

    #Draws the instructionGUI
    win2.setBackground("thistle4")
    
    instructionsTitle = Text(Point(150,20),"Hangman Instructions")
    instructionsTitle.setStyle("bold")
    instructionsTitle.setSize(17)
    instructionsTitle.draw(win2)

    text = "Guess the letters in the randomly \n generated word \n\n You \
have 6 wrong guesses before \n you lose the game \n\n If you can get the \
word with less \n than 6 errors you win"
    
    instruction1 = Text(Point(150,125),text)
    instruction1.draw(win2)

    instruction2 = Text(Point(150,240),"(click anywhere to close this window)")
    instruction2.setSize(8)
    instruction2.setStyle("italic")
    instruction2.draw(win2)

def getWord():
    '''returns a random word from the file'''

    #Creates a list with the words
    infile = open("words.txt",'r')
    words = infile.readlines()
    infile.close()

    #Randomizes the list
    random.shuffle(words)

    #Chooses the first word in the list
    word = words[0][:len(words[0])-1]

    ###PRINTS THE WORD IN THE WINDOW###
    #print (word) <- Uncomment this if you want to know the word

    return word

def drawSquares(word):
    '''returns a list of the square boxes'''
    
    rect_list = []

    #Draws the square boxes centered on the screen and creates a list with them
    if len(word) % 2 == 0:
        for num in range (len(word)//2):
            rect = Rectangle(Point(250+40*num,255),Point(280+40*num,285))
            rect.setWidth(3)
            rect.setFill("HotPink4")
            rect.draw(win)

            rect_list.append(rect)

        for num2 in range(len(word)//2):
            rect2 = Rectangle(Point(240-40*num2,255),Point(210-40*num2,285))
            rect2.setWidth(3)
            rect2.setFill("HotPink4")
            rect2.draw(win)

            rect_list.append(rect2)

    else:
        rect = Rectangle(Point(235,255),Point(265,285))
        rect.setWidth(3)
        rect.setFill("HotPink4")
        rect.draw(win)

        rect_list.append(rect)

        for num in range ((len(word)-1)//2):
            rect2 = Rectangle(Point(275+40*num,255),Point(305+40*num,285))
            rect2.setWidth(3)
            rect2.setFill("HotPink4")
            rect2.draw(win)

            rect_list.append(rect2)

        for num2 in range ((len(word)-1)//2):
            rect3 = Rectangle(Point(225-40*num2,255),Point(195-40*num2,285))
            rect3.setWidth(3)
            rect3.setFill("HotPink4")
            rect3.draw(win)

            rect_list.append(rect3)


    return rect_list

def alphaButtonList(listt,xAnchor,yAnchor,button_list):
    '''creates a list with the buttons in it'''

    for button in range (len(listt)):

        point = Point(xAnchor+40*button,yAnchor)
        button_list += [Button(win,point,40,20,listt[button],"HotPink4")]
        
def buttonActivation(listt):
    '''activates buttons in a list'''
    
    for button in listt:
        button.activate()

def objectUndraw(object_list):
    '''undraws objects in a list'''
    
    for objectt in object_list:
        objectt.undraw()

main()

