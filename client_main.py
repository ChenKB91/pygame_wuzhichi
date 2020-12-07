import Gaming_UI

class Client():
    board = None;
    client_socket = socket()
    def __init__(self):
        # self.board = None
        pass

    def connect_client_to_server(self):  # 20
        """ bind, accept, listen?, ... """
        pass

    def player_make_move(self):
        """ Detect coordinate, process it ,and return player's move """
        Client.check_if_valid_on_user_board(player_move)  # loop
        return Gaming_UI.check_mouse_click()

    def recieve_board(self):  # 15
        """ Update self.board """
        pass

    def check_if_valid_on_user_board(self, player_move):  # 15
        """ check if there's been chess on that location """
        return bool

    def send_move_to_server(self, player_move):  # 15
        self.client_socket.send(player_move)

    def recieve_game_status(self):  #15
        """ Return a boolean stands for is game end """
        return self.client_socket.recv()


Client.connect_client_to_server()
# Gaming_UI.draw_start_screen()
while True:
    Client.recieve_board()
    Gaming_UI.draw_board(Client.board)
    player_move = Client.player_make_move()
    Client.send_move_to_server(player_move)
    if Client.recieve_game_status() == "End_Game":
        break
