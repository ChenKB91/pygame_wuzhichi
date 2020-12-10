import socket
import pickle

from game_objects import Board

SERVER_IP = "140.112.30.35"
SERVER_DEFAULT_PORT = 62345
BUFSIZE = 32768

class Client():
    def __init__(self, server_port):
        self.board = None
        # TODO need gaming UI to receive move from user
        self.gaming_interface = None
        self.socket = None
        self.server_port = server_port


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
            self.socket.connect((SERVER_IP, self.server_port))
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


    def receive_board(self):  # 15 (Use "module pickle"--binary)

        """ receive the new board from the server and update
        """
        try:
            received_board = pickle.loads(self.socket.recv(BUFSIZE))
            self.board = received_board
            print("receive the new board from server.")
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


    def receive_game_status(self):  #15
        """ Return a list stands for is game end ("Playing" or "
        End_Game")"""
        return self.client_socket.recv()


    def receive_game_status(self):  #15
        """ receive the game status from the server
        """
        try:
            received_game_status = pickle.loads(self.socket.recv(BUFSIZE))
            print("receive the new game status from server.")
        except:
            print("something goes wrong when receiving game status from the server.")

        return received_game_status


if __name__ == '__main__':
    input_server_port = int(input('Enter Server Port(enter empty for using default port 62345): '))
    server_port = SERVER_DEFAULT_PORT if input_server_port == '' else input_server_port
    player = Client(server_port)
    
    if player.connect_client_to_server():
        # Gaming_UI.draw_start_screen()
        while True:
            player.receive_board()
            # Gaming_UI.draw_board(player.board)
            player_move = player.player_make_move()
            player.send_move_to_server(player_move)
            if player.receive_game_status() == "End_Game":
                break
