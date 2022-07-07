from computer import Computer
from guesser import Guesser
from display import Display


class Instance():
    computer_wins = 0
    human_wins = 0
    draws = 0
    def __init__ (self):
        pass
    
    def play_one_round(self):
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
            self.human_wins += 1
        elif computer_guess.beats(human_guess):
            print('Computer wins')
            self.computer_wins += 1       
        else:
            print('Draw')
            self.draws += 1

    def Best_of_3(self):
       while self.computer_wins < 2 and self.human_wins < 2:
            try:
                self.play_one_round()
                if self.draws + self.human_wins + self.computer_wins == 1:
                    # we only ask this question on the first turn
                    q = input("Best of 3?: y/n")
                    if q.lower() != 'y': 
                        break
            except ValueError:
                print("Invalid Selection")
                return
    
    def final_result (self):               
        if self.computer_wins > self.human_wins:
            print(f'>>> Computer won: {self.computer_wins} to {self.human_wins} <<<')
        else:
            print(f'>>> Human won: {self.human_wins} to {self.computer_wins} <<<')
        print(f'>>> There were {self.draws} draws! <<<')
        