# Game objects

# Game constant
BLACK = -1
WHITE = 1
EMPTY = 0

class Move:
    def __init__(self, color, coordinate):
        pass

class Board:
    def __init__(self):
        # from constant import BLACK, WHITE, EMPTY
        self.__board = None # [[EMPTY]*n]*n
    
    def update(self, move):
        pass
    
    def get_board(self):
        return self.__board

class User:
    def __init__(self):
        self.ip = None
