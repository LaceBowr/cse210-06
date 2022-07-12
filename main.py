# Import director
from director import Director

# Create the main function and start the game
# using director
def main():
    #Where the initial play is run and observed in the terminal
    director = Director()
    director.start_game()

# Create a if statement and add in the name
# function into the main function to allow
# the user to guess on Rock, Paper, or Scissors
if __name__ == "__main__":
    main()

# Previous code
'''
def main():
    g = Game()
    
    while g.answer != "q":
        print()
        g.makeItRandom()
        answer1 = input("Pick one: rock, paper, scissors, lizard, spock:  ")
        print()
        g.answer = answer1
        print()
        print("You Choose ({})".format(g.answer))
        print()
        g.print()
        print()
        g.letsCheck()

if __name__ == "__main__":
    main()
'''
