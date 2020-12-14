import socket
import pickle
import pygame
from pygame.locals import QUIT

from game_objects import Board, Move
from gaming_UI import GamingUI

SERVER_IP = "140.112.30.35"
LOCALLOST_IP = "127.0.0.1"
SERVER_DEFAULT_PORT = 62345
BUFSIZE = 32768

class Client():
    def __init__(self, server_port, server_ip):
        self.board = None
        # TODO need gaming UI to receive move from user
        self.ui = GamingUI()
        self.socket = None
        self.server_port = server_port
        self.server_ip = server_ip
        self.color = None


    def connect_client_to_server(self):  # 20
        """ connect client to server 
        """
        try:  
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
            print ("Socket successfully created") 
        except socket.error as err:  
            print ("Socket creation failed with error %s" %(err))
            return False
        
        #try:
        self.socket.connect((self.server_ip, self.server_port))
        color = pickle.loads(self.socket.recv(BUFSIZE))
        self.color = color
        print("Connected")
        """except:
            print("Connection error")
            return False"""
        
        return True


    def player_make_move(self, x, y):
        """ waiting for user input until getting a valid input and update the client board
        """
        move = Move(self.color, x, y)
        if self.check_if_valid_on_user_board(move):
            # update board
            return move
        else:
            return False


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
    input_server_port = input('Enter Server Port(just press enter for using default port 62345): ')
    input_server_ip = input('Enter 1 for remote server(140.112.30.35) / 0 for localhost(127.0.0.1): ')
    server_port = SERVER_DEFAULT_PORT if input_server_port == '' else int(input_server_port)
    #server_ip = SERVER_IP if input_server_ip == "1" else LOCALLOST_IP
    if input_server_ip == "1": server_ip = SERVER_IP
    elif input_server_ip == "0": server_ip =LOCALLOST_IP
    else: server_ip = input_server_ip
    player = Client(server_port, server_ip)

    pygame.init()
    pygame.display.set_caption('Dinosaur Game')
    screen = pygame.display.set_mode((800, 800))
    
    if player.connect_client_to_server():      
        while True:
            player.receive_board()
            player.ui.draw_board(player.board)     
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()

                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    x, y = player.ui.mouse_click(pos)
                    player_move = player.player_make_move(x, y)
                    if player_move:
                        player.send_move_to_server(player_move)
                    
            if player.receive_game_status() == "End_Game":
                break

