import abc
class Guess(metaclass=abc.ABCMeta):
    def __init__():
        #The random choice of the guesser from scissors, rock, or paper.
        #The random choice of the computer from scissors, rock, or paper.
        pass
    
    # this forces all classes that inherit from guess implement "beats"
    @abc.abstractmethod
    def beats(self, guess):
        # implemented in each of the classes that inherits from guess, and determines
        # whether it beats a different guess -- for example if you implement a child class
        # of guess that is "Rock", the rock subclass must implent "beats" and determin if
        # which other types of guesses it beats (i.e rock beats scissors).  The base class
        # itself has no implementation.

        pass
