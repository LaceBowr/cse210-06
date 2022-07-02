from objects.objects import Paper,Rock,Scissors

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
