import pygame
from game_objects import *
from pygame.locals import QUIT
class GamingUI():
    def __init__(self):

        # pygame.init()
        self.surface = pygame.display.set_mode((800, 800))
        pygame.display.set_caption('五子棋')
        Raw_BoardImg = pygame.image.load('./images/board_img.png')
        self.B_img = pygame.image.load('./images/black.png')
        self.B_img = pygame.transform.scale(self.B_img, (45,45))        
        self.W_img = pygame.image.load('./images/white.png')
        self.W_img = pygame.transform.scale(self.W_img, (45,45))        
        self.boardImg = pygame.transform.scale(Raw_BoardImg, (630, 630)) #實際上是14個間隔 一格改成45 pix
        self.board_origin = (100,100)
        self.surface.fill((255,255,255))


    def draw_board(self, board):  # 100
        self.surface.blit(self.boardImg, self.board_origin)
        '''
        This is for cool gray stuff 
        maybe it should go to somewhere
        '''
        (i,j) = pygame.mouse.get_pos()
        i,j=int(round((i-100)/45)),int(round((j-100)/45))
        if i>-1 and j>-1 and i<16 and j<16:
            pygame.draw.circle(game1.surface, (175, 175, 175),[100+45*i, 100+45*j],45/2,0)
              
        for i in range(15):
            for j in range(15):
                if board.get_board()[i][j] == -1:
                    self.surface.blit(self.B_img, (100+45*i-35/2-4, 100+45*j-35/2-4))# 35/2那個是修正棋子的圖片偏移 定中心為(0,0)
                elif board.get_board()[i][j] == 1:
                    self.surface.blit(self.W_img, (100+45*i-35/2-4, 100+45*j-35/2-4))
        pygame.display.update()


    def mouse_click(self, coordinate):  # 100
        # converts pixel coordinate to board coordinate.
        print('raw coor',coordinate)
        x = int(round((coordinate[0]-100)/45))
        y = int(round((coordinate[1]-100)/45))
        if x < 0: x = 0
        elif x > 15: x=15
        if y < 0: y = 0
        elif y > 15: y=15
        print(x,y)
        return x, y


if __name__ == '__main__':
    empty_board=Board()
    
    game1 = GamingUI()
    '''
    while True:
        for j in range (15): 
            for i in range (15):
                pygame.time.delay(100)
                empty_board.update(Move(1 if (i+j)%2 else -1, (j, i)))

                game1.draw_board(empty_board)
                for event in pygame.event.get():
                        print(event)
                        if event.type == QUIT:
                            pygame.quit()

                        if event.type == pygame.MOUSEBUTTONUP:
                            pos = pygame.mouse.get_pos()
                            x, y = game1.mouse_click(pos)
    '''
    counter=0
    #Gray_Potential=pygame.Rect(100+45*i-35/2, 100+45*j-35/2, width, height)
    while True:
        game1.surface.fill((255,255,255))
        game1.draw_board(empty_board)
        for event in pygame.event.get():
                print(event)
                if event.type == QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    x, y = game1.mouse_click(pos)
                    empty_board.update(Move(1 if counter%2 else -1, (x, y)))
                    counter+=1
    
    


