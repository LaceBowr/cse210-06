from display import Display
from computer import Computer
from guesser import Guesser

winner= 3 or 2
computer_win = 1
human_win = 1
Computer_total = 0
Human_total = 0

class Director():
    # the Director in Paper-Rock-Sissors 
    # introduces, starts, collects input and 
    # updates and concludes the game.

    def __init__ (self):
        """Constructs a new Director using the specified video service.
        
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        display = Display()

    def close_window(self):
        while Director.update(self) < 3: 
            return Director.start_game(self)
        if Director.update(Computer_total) > 2:
            winner = Computer_total 
            print('Winner of Best_of_3 is Computer')
            return

        elif Director.update(Human_total) > 2:
            winner = Human_total
            print('Winner of Best_of_3 is Human')
            return
            
        elif (Director.update(Computer_total),Director.update(Human_total)):
            winner = (2,1)
            print('Winner of Best_of_3 is Computer')
            return
            
        elif (Director.update(Human_total),Director.update(Computer_total)):
            winner = (2,1)
            print('Winner of Best_of_3 is Human')
            return
        exit()

    def start_game(self):
        computer_win = 1
        human_win = 1
        neither_win = 0 
        guesser = Guesser()
        human_guess = guesser.get_guess()
        computer = Computer()
        computer_guess = computer.get_guess()
        display = Display()
        display.print_guess(human_guess)
        display.print_guess(computer_guess)
        if human_guess.beats(computer_guess):   
            print('Human wins')
            return human_win
        elif computer_guess.beats(human_guess):
            print('Computer wins')
            return computer_win        
        else:
            print('Draw')
            return neither_win
