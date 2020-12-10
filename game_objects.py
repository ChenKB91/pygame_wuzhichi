# Game objects

# Game constant
BLACK = -1
WHITE = 1
EMPTY = 0

class Move:
    def __init__(self, color, coordinate):
        self.__value = [color, coordinate[0], coordinate[1]]
    
    def get_value(self):
        return self.__value


class Board:
    def __init__(self, board_width=15, board_length=15):
        self.board_width = board_width
        self.board_length = board_length
        self.__board = [[EMPTY]*board_width for _ in range(board_length)]
        
    def update(self, move):
        move_value = move.get_value()
        self.__board[move_value[1]][move_value[2]] = move_value[0]
    
    def get_board(self):
        return self.__board
    
    def check_valid(self, move:Move):
        """ check if the move is valid

        args:
            :move: game_objects.Move
        """

        color, x, y = move.get_value()
        if self.__board[x][y] != EMPTY:
            return False
        elif self.__board[x][y] == EMPTY:
            return True


class User:
    def __init__(self, socket, addr):
        self.ip = None
        self.socket = socket
        self.addr = addr
