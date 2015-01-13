#Tony K.
#Lists - Development

import random

def questions_answer():
    country_capitals = [
    ["Germany","England","Austria","France","Italy","Scotland","Spain","Norwegain","Spain","Hungary"],
    ["Berlin","London","Vienna","Paris","Rome","Edinburgh","Madrid","Stockholm","Madrid","Budapest"]
    ]
    return country_capitals
    
def game(country_capitals):
    correct = 0

    for count in range(10):
        random_number = random.randrange(10)
        user_answer = input("What is the capital city of {0}: ".format(country_capitals[0][random_number]))
        user_answer = user_answer.lower()
        user_answer = user_answer.capitalize()
        if user_answer == country_capitals[1][random_number]:
            correct = correct + 1
            print("Well Done, the Capital of {0} is {1}".format(country_capitals[0][random_number],country_capitals[1][random_number]))
            print()
        else:
            print("Sorry, the Capital of {0} is {1}".format(country_capitals[0][random_number],country_capitals[1][random_number]))
            print()
    return correct

def display(correct):
    false = 10 - correct
    print("You have completed the Game")
    print("You have gotten {0} correct answers.".format(correct))
    print("You have gotten {0} wrong answers.".format(false))
    

def main():
    print("This program tests your knowledge on European Countries and Capital Cities")
    print()
    country_capitals = questions_answer()
    correct = game(country_capitals)
    display(correct)
    

    
        
