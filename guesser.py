# Import Rock, Paper, and Scissors
from objects import Paper,Rock,Scissors

# Create class guesser
class Guesser():

    # Create the init function
    def __init__(self):
        pass

    # Create the get guess and do a while
    # statement that allows the user guess
    # to choose Rock, Paper, Scissors
    def get_guess(self):
        while True:
            text = input("Do you guess (P)aper, (R)ock, or (S)cissors: ")
            text = text.lower()
            if text == 'p':
                return Paper()
            elif text == 'r':
                return Rock()
            elif text == 's':
                return Scissors()
            else:
                print("Invalid input, try again")
                
# This code shows the design of the objects in the game
# It prints out the Rock, Paper, and Siccors after the
# user has guess, it will then display any error
# messages if the user has type in the wrong letter
'''from objects import Paper, Rock, Scissors
class Display():
    def __init__(self) -> None:
        pass
    def print_guess(self, guess):
        if isinstance(guess, Scissors):
            print("0   0")
            print("  X ")
            print(" / \\")
            print("/   \\")

        elif isinstance(guess, Rock):
            print("  ____")
            print("/      \\")
            print("\ ____ /")

        elif isinstance(guess, Paper):
            print("   _______")
            print("  /      /,")   
            print(" /      //")
            print("/______//")
        else:
            print("Unknown Guess Type: You did something wrong")'''
