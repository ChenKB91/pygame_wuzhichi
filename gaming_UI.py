import pygame

class GamingUI():
    def __init__(self, s):

        # pygame.init()
        self.surface = pygame.display.set_mode((800, 800))
        pygame.display.set_caption('五子棋')
        Raw_BoardImg = pygame.image.load('./images/board_img.png')
        self.B_img = pygame.image.load('./images/black.png')
        self.B_img = pygame.image.scale(self.B_img, (40,40))        
        self.W_img = pygame.image.load('./images/white.png')
        self.W_img = pygame.image.load('./images/white.png')
        
        self.boardImg = pygame.transform.scale(Raw_BoardImg, (600, 600))
        self.surface.blit(boardImg, (0,0))

        self.board_origin = (100,100)


    def draw_board(self, board):  # 100
        self.surface.blit(boardImg, self.board_origin)        
        for i in range(15):
            for j in range(15):
                if board.get_board()[i][j] == 1:
                    self.surface.blit(B_img, (180+40*i, 180+40*j))
                elif board.get_board()[i][j] == -1:
                    self.surface.blit(W_img, (180+40*i, 180+40*j))
        pygame.display.update()


    def mouse_click(self, coordinate):  # 100
        # converts pixel coordinate to board coordinate.
        x = int(round((coordinate[0]-100)/40))
        y = int(round((coordinate[1]-100)/40))
        if x < 0: x = 0
        elif x > 15: x=15
        if y < 0: y = 0
        elif y > 15: y=15

        return x,y


if __name__ == '__main__':
    game1=GamingUI()
    game1.draw_board