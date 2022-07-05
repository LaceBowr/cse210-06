from random import choice
from objects import Paper, Rock, Scissors
class Computer():
    def __init__(self):
        pass
    def get_guess(self):
        text = choice(['r','s','p'])
        if text == 'p':
            return Paper()
        elif text == 'r':
            return Rock()
        elif text == 's':
            return Scissors()
        else:
            # you didn't handle one of the choices you allowed the computer to make
            raise Exception("This should not be able to happen")
'''import random
words = ("paper, rock, scissors" )

class Computer: 
    
    def __init__(self):
        self.random_word = ''
        self.word_with_placeholders = []

    def get_random_word(self):
        self.random_word = self.get_word(words)
        # copy the word and then wipe out ever letter with a _ 
        # so we have a place to stick guesses
        for i in range(len(self.random_word)):
            self.word_with_placeholders.append('_') 
        return 

    def get_word(self):
        computer_guess = random.choice(words)
        return computer_guess

    def get_guess(self, computer_guess):
        if computer_guess in self.random_word:
            for i, ch in enumerate(self.random_word):
                if ch == computer_guess:
                    self.get_word_with_object[i]=computer_guess
            return True
        return False
    
    def get_word_with_object(self):
       return "".join(self.get_word_with_object)'''