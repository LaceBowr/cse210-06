from objects import Paper,Rock,Scissors

class Guesser():

    def __init__(self):
        pass

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
