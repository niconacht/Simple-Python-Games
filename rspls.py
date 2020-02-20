# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def name_to_number(name):
    
    if name == "rock":
        return 0
    elif name == "spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    
    elif name == "scissors":
        return 4
    
    else:
        print(" Choose Rock, Spock, Paper, Lizard or Scissors!Try again")


def number_to_name(number):
    # delete the following pass statement and fill in your code below
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else: 
        print("Something went wrong. Please try again")
    
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    

def rpsls(player_choice): 
    import random
    # delete the following pass statement and fill in your code below
    print "\n"
    player_choice = player_choice.lower()
    print "Player chooses %s" % player_choice
    player_number = name_to_number(player_choice)
    #print player_number
    comp_number = random.randrange(0, 4)
    #print comp_number
    comp_choice = number_to_name(comp_number)
    print "Computer chose %s" % comp_choice 
    result = (player_number - comp_number) % 5
    #print result
    
    if result > 0 and result <= 2:
        print "The winner is Player"
     
    elif result >2 and result <= 4:
        print "The winner is Computer"
    elif result == 0:
         print "It's a tie"
    else:
         print "Something went wrong"
    
    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


