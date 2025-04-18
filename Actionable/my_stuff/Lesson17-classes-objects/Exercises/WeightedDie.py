import random
from collections import Counter
from Die2 import Die

class WeightedDie(Die):
    "A weighted die"
    def __init__(self, weights, sides=6):
        """Creates a new weighted die
        
        Keyword arguments:
        sides (int) -- number of die sides.
        weights (list) -- a list of integers holding the weights 
            for each die side
        """
        if len(weights) != sides:
            raise Exception(f'weights must be a list of length {sides}.')
        super().__init__(sides)
        self._weights = weights
    
    def roll(self):
        """Returns a value between 1 and the number of die sides."""
        
        # COMPLETE THIS CODE