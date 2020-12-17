import pickle
import socket
from game_objects import User, Board

BUFSIZE = 32768

class Server():
    def __init__(self):
        self.board = Board()
        #self.socket = None
        self.game_status = "Playing" # temporary
        self.user_list = []
        self.host = "140.112.30.35"
        self.port = 62345

    def receive_user_connection(self):  # 20
        """ bind, accept, listen, ...
            And update user_list"""
        self.host = socket.gethostbyname(socket.gethostname())
        print("Host: ", self.host)
        # 這是ptt的sample code，但要處理2個clients好像要別的方法，待修改（已修改完成）
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as l_s:
            l_s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
            l_s.bind((self.host, self.port))
            l_s.listen()
            c_s, addr = l_s.accept()
            self.user_list.append(User(c_s, addr))
            print("1 Connected", addr)
            self.user_list[0].socket.sendall(pickle.dumps(int(-1)))
            print("1 Color Assigned")

            l_s.listen()
            c_s, addr = l_s.accept()
            self.user_list.append(User(c_s, addr))
            print("2 Connected", addr)
            self.user_list[1].socket.sendall(pickle.dumps(int(1)))
            print("2 Color Assigned")


    def send_board_to_client(self):  # 15
        # sends board to both clients
        for user in self.user_list:
            user.socket.sendall(pickle.dumps(self.board))

    def receive_move_from_client(self, user):  # 15
        # receives baord from the specified user
        data = user.socket.recv(BUFSIZE)
        while data == None: data = user.socket.recv(BUFSIZE)
        return pickle.loads(data)

    def make_move(self, move):
        self.board.update(move)

    def check_if_the_game_end(self, move):  # looooongic
        """ Check if there's 5 connected pieces, 
            and update game status """
        move_color = move.get_value()[0]
        pi = (move.get_value()[2:0:-1])  # initial point(x, y)
        dx = [1, 1, 0, -1, -1, -1, 0, 1]  # 從右邊逆時針繞一圈
        dy = [0, -1, -1, -1, 0, 1, 1, 1]
        chess_count = [0] * 8
        board = self.board.get_board()

        NoChessFound = 99

        for step in range(1, 5):
            for direct in range(8):
                if chess_count[direct] > 0:
                    continue
                if 0 <= pi[0]+dx[direct]*step < 15 and 0 <= pi[1]+dy[direct]*step < 15:
                    if board[pi[1]+dy[direct]*step][pi[0]+dx[direct]*step] == move_color:  # 1 found
                        chess_count[direct] -= 1
                    else:  # kill this direction
                        if chess_count[direct] == 0:
                            chess_count[direct] = NoChessFound
                        else:
                            chess_count[direct] *= -1

        for direct in range(8):
            if chess_count[direct] == NoChessFound:
                chess_count[direct] = 0
            else:
                chess_count[direct] = abs(chess_count[direct])

        for direct in range(4):
            if chess_count[direct] + chess_count[direct+4] >= 4:
                self.game_status = "End_Game"
                return
        return

    def send_game_status(self):
        # sends game status to both clients
        for user in self.user_list:
            user.socket.send(pickle.dumps(self.game_status))


if __name__ == '__main__':
    server = Server()
    server.receive_user_connection()
    moves_history = []
    while True:
        for user in server.user_list:
            #print(1)
            server.send_board_to_client()
            # print(2)
            move = server.receive_move_from_client(user)
            moves_history.append(move)
            # print(3)
            server.make_move(move)
            server.check_if_the_game_end(move)
            #print(4)
            server.send_game_status()
            #print(5)
            if server.game_status == "End_Game":
                break
