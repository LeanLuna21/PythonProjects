# Let's play hangman
# Tries = 6
# Given a list of words (goal):
##### Generate a random choice from the list of options
##### Show selected word in terms of spaces (n° of letters - low dashes?)
##### Ask the user for to introduce a character (letter-uppercase)
##### Check if the character exists in the goal word
########### If it does -> print letter in correct space (index) --- print all corresponding indexes if letter is repeated
########### If it does not -> show it doesn't and add an x to the count
##### When tries = 0 game is over 

import random
import string

# word options
words = ['AWESOME','POLAROID','MOUNTAIN','TRUSTWORTHY','UNRELIABLE','SYMPATHETIC','MAINTENANCE']
# generate 1 random word from options
goal = str(random.choice(words))

def run ():
    print (f"\nWelcome to HANGMAN!\nYour word is {len(goal)} letters long:")
    solution_spaces = show_goal(goal) 
    print (solution_spaces)
    
    checking_letters()

# fx that shows the letter spaces of the goal word
def show_goal(goal):
    spaces = ""

    for i in goal:
        spaces += "_  "
    return spaces

# fx that asks for letters to user and checks if they exist in goal word
def checking_letters():
    win = False
    tries = 6
    options = list(string.ascii_uppercase)  # we make sure the user chooses a LETTER character.
    not_correct = [] # empty list to show letters which were wrong.
    used_letters = []  # list to show letters that are correct.
    while win != True and tries > 0:
        # "x" will be the letter input from user.
        x = input ("\nChoose a letter between A and Z: ").upper()
        
        # if x is not a letter
        if x not in options: 
            print ("Choose a correct character!")
        # else, if x is letter and appears in the goal word
        elif x in options and x in goal:
            print ("Letter found!")
            # add letter to list of correct characters
            used_letters.append(x)
            # create the list of correct characters in the correct spaces comparing them to goal word using a list comprehension
            temp = [letters if letters in used_letters else "_" for letters in goal]
            # show on screen for user
            print (*temp,sep="  ")
            # when there are no more empty spaces...
            if "_" not in temp:
                print(f"\nThe word was {goal}\nYou WIN!\nCONGRATULATIONS")
                break
        
        # else, if letter not in goal word
        else:
            print ("xx Letter not found xx")
            # add letter to list of incorrect characters
            not_correct.append(x)
            # print it as a set { }
            print(set(not_correct))
            # decrease n° of tries
            tries -= 1
            print (f"Tries left: {tries}")

    if tries == 0:
        print (f"\nThe word was {goal}\nYou lose!")
    print ("\nGAME OVER\n")


def restart():
    op = input("\nTry again?: ").upper()
    if op == "Y":
        run()
    else:
        print("Okay Bye!")


if __name__ == "__main__": 
    run()
    restart() 