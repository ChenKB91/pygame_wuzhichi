# Game objects

# Game constant
BLACK = -1
WHITE = 1
EMPTY = 0

class Move:
    def __init__(self, color, coordinate):
        self.__value=[color,coordinate[0],coordinate[1]]
    def get_value(self):
        return self.__value
class Board:
    def __init__(self):
        # from constant import BLACK, WHITE, EMPTY
        def constructing_board():
            board=[]
            for _ in range(15):
                tmp=[]
                for i in range(15):
                    tmp.append(EMPTY)
                board.append(tmp)
            return board
        self.__board = constructing_board() # [[EMPTY]*n]*n
        
    def update(self, move):
        move_value=move.get_value()
        self.__board[move_value[1]][move_value[2]] = move_value[0]
    
    def get_board(self):
        return self.__board

class User:
    def __init__(self,socket,addr):
        self.ip = None
        self.socket = socket
        self.addr = addr
