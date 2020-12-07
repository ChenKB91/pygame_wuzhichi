import pygame

class GamingUI():
    def __init__(self):
        surface = None  # pygame.surface

    def draw_board(self, board):  # 100
   		# 
        # draw_grid
        # draw zhi
        for i in range(15):
        	for j in range(15):
        		if board[i][j] == 1:
        			pass
        		elif board[i][j] == -1:
        			pass


    def check_mouse_click(self):  # 100
        player_move = Move(mouse_coordinate)
        return player_move