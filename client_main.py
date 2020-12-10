import socket
import pickle

from game_objects import Board

SERVER_IP = "127.0.0.1"
SERVER_PORT = 65432
BUFSIZE = 32768

class Client():
    def __init__(self):
        self.board = None
        # TODO need gaming UI to receive move from user
        self.gaming_interface = None
        self.socket = None

    def connect_client_to_server(self):  # 20
        """ connect client to server 
        """
        try:  
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
            print ("Socket successfully created") 
        except socket.error as err:  
            print ("Socket creation failed with error %s" %(err))
            return False
        
        try:
            self.socket.connect((SERVER_IP, SERVER_PORT))
            print("Connected")
        except:
            print("Connection error")
            return False
        
        return True


    def player_make_move(self):
        """ waiting for user input until getting a valid input and update the client board
        """

        while True:
            move = self.gaming_interface.make_move()
            if self.check_if_valid_on_user_board(move):
                # update board
                return move


    def recieve_board(self):  # 15 (Use "module pickle"--binary)
        """ receive the new board from the server and update
        """
        try:
            received_board = pickle.loads(self.socket.recv(BUFSIZE))
            self.board = received_board
            print("recieve the new board from server.")
        except:
            print("something goes wrong when receiving board from the server.")
        
        return


    def check_if_valid_on_user_board(self, player_move):  # 15
        """ check if the move valid
        """
        return self.board.check_valid(player_move)


    def send_move_to_server(self, player_move):  # 15
        """ send the move to the server
        """
        self.socket.send(pickle.dumps(player_move))
        return


    def recieve_game_status(self):  #15
        """ receive the game status from the server
        """
        try:
            received_game_status = pickle.loads(self.socket.recv(BUFSIZE))
            print("recieve the new game status from server.")
        except:
            print("something goes wrong when receiving game status from the server.")

        return received_game_status


if __name__ == '__main__':
    player = Client()
    if player.connect_client_to_server():
        # Gaming_UI.draw_start_screen()
        while True:
            player.recieve_board()
            # Gaming_UI.draw_board(player.board)
            player_move = player.player_make_move()
            player.send_move_to_server(player_move)
            if player.recieve_game_status() == "End_Game":
                break
