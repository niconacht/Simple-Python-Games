# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random

num_range = 100
counter = 7
secret_number = 0

# helper function to start and restart the game
def new_game():
    global num_range
    global secret_number
    global counter
    secret_number = random.randrange(0, num_range)
    if num_range == 1000:
        counter = 10
    elif num_range == 100:
        counter = 7
 
    

# define event handlers for control panel
def range100():
    global num_range
    num_range = 100
    
    # button that changes the range to [0,100) and starts a new game 
    new_game()
    
def range1000():
    global num_range
    # button that changes the range to [0,1000) and starts a new game     
    num_range = 1000
    counter = 10
    new_game()
    

    
def input_guess(guess):
    global secret_number
    global numb
    global counter
    
    numb = int(guess)
 
    print "Guess was ", numb
    counter = counter -1
    print "Chances left: ", counter
  
    """Compare number with computerchoice"""
    if numb > secret_number:
        print "Lower. "
        
    elif numb < secret_number:
        print "Higher"
        
    else:
        print "Correct! You win!"
        new_game()
    
    if numb is not secret_number and counter == 0:
        print "Game over! Try again"
        new_game()
    
            
   
    
# create frame
frame = simplegui.create_frame("Guess the number", 200, 200)


# register event handlers for control elements and start frame
frame.add_input("Guess a number", input_guess, 100)
frame.add_button("Range[o, 100)", range100, 100)
frame.add_button("Range[o, 1000)", range1000, 100)


frame.start()

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
