import pickle
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
        
        # 這是ptt的sample code，但要處理2個clients好像要別的方法，待修改
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as l_s:
            l_s.bind((self.host, self.port))
            l_s.listen()
            c_s, addr = l_s.accept()
            with c_s:
                print("Connected", addr)
                while True:
                    data = c_s.recv(1024)
                    if not data:
                        break
                    c_s.sendall(data)
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
        # 要有board的定義才能寫
        pass

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
