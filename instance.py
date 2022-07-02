
class Instance (guess):

    def __init__ (self):
       computer_wins = 0
       player_wins = 0
    
    def Best_of_3(self):
       while True:
            try:
                turns = int(input("Best out of (3 or 5): "))
                if turns == 3: 
                    break
                continue
            except ValueError:
                necessary_wins = int(turns/2) + 1
                return
    
    def final_result (self):               
        if player_wins > computer_wins:
            print(f'>>> You win! <<<')
        else:
            print(f'>>> Computer wins! <<<')
        
        print(f'>>> You scored: {player_wins} point(s) <<<')
        