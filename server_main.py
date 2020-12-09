import pickle
from GameObjects import User
class Server():
    def __init__(self):
        self.board = None
        self.socket = None
        self.game_status = None
        self.user_list = None
        self.host = "127.0.0.1"
        self.port = 65432

    def recieve_user_connection(self):  # 20
        """ bind, accept, listen, ...
            And update user_list"""
        
        # 這是ptt的sample code，但要處理2個clients好像要別的方法，待修改（已修改完成）
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as l_s:
            l_s.bind((self.host, self.port))
            l_s.listen()
            c_s, addr = l_s.accept()
            user_list.append(User(c_s, addr))
            print("1 Connected", addr)

            l_s.listen()
            c_s, addr = l_s.accept()
            user_list.append(User(c_s, addr))
            print("2 Connected", addr)

            """
            with c_s:
                print("Connected", addr)
                while True:
                    data = c_s.recv(1024)
                    if not data:
                        break
                    c_s.sendall(data)"""
        # 待修改結束

        pass

    def send_board_to_client(self, user_list):  # 15
        # 也要改成多個clinet的方法
        self.socket.send(pickle.dumps(self.board))

    def recieve_move_from_client(self, user):  # 15
        # 對指定ip的user接收move的方法？
        return pickle.loads(self.socket.recv(user.ip))

    def make_move(self, move):
        self.board.update(move)

    def check_if_the_game_end(self, move):  # looooongic
        """ Check if there's 5 connected chesses, 
            and update game status """
        move_color = move.get_value()[0]
        pi = (move.get_value()[1:])  # initial point(x, y)
        dx = [1, 1, 0, -1, -1, -1, 0, 1]  # 從右邊逆時針繞一圈
        dy = [0, -1, -1, -1, 0, 1, 1, 1]
        chess_count = [0] * 8
        board = self.board.get_value()

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

    def send_game_status(self, users):
        for user in users:
            self.socket.send(self.game_status)

Server.receieve_user_connection()
while not Server.ended:
    for user in user_list:
        Server.send_board_to_client(user_list)
        move = Server.recieve_move_from_client(user)
        Server.make_move(move)
        Server.check_if_the_game_end(move)
        Server.send_game_status(user_list)
        if Server.game_status == "End_Game":
            break
