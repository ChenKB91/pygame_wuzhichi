import pygame

class GamingUI():
    def __init__(self):

        pygame.init()
        surface = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('五子棋')
        Raw_BoardImg = pygame.image.load('./images/board_img.png')
        BW_img = pygame.image.load('./images/BW.png')
        croppedBW = pygame.Surface((70, 70))
        boardImg = pygame.transform.scale(Raw_BoardImg, (600, 600))
        window_surface.blit(boardImg, (0,0))

    def draw_board(self, board , ):  # 100
        # [[EMPTY]*n]*n
        # draw_grid
        # draw zhi
        
        for i in range(15):
            for j in range(15):
                if board[i][j] == 1:
                    surface.blit(BW_img, (40*i, 40*j), (0, 70, 70, 70))
                elif board[i][j] == -1:
                    surface.blit(BW_img, (40*i, 40*j), (0, 0, 70, 70))


    def check_mouse_click(self):  # 100
        player_move = Move(mouse_coordinate)

if __name__ == '__main__':
    game1=GamingUI()
    game1.draw_board