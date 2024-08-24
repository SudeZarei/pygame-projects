import pygame
pygame.init()
from checkers.constants import *
from checkers.game import Game
from minimax.algorithm import minimax
from checkers.menu import Menu

RED = (0, 0, 255)

class Vars:
    def __init__(self) -> None:
        self._game_mode = None
        self._player_color = None
        self._ai_color = None
    
    @property
    def game_mode(self):
        return self._game_mode
    @game_mode.setter
    def game_mode(self, mode):
        self._game_mode = mode
    
    @property
    def player_color(self):
        return self._player_color
    @player_color.setter
    def player_color(self, mode):
        self._player_color = mode
    
    @property
    def ai_color(self):
        return self._ai_color
    @ai_color.setter
    def ai_color(self, mode):
        self._ai_color = mode
        


FPS = 60 # this is for rendering so we don't put it in constant
clock = pygame.time.Clock() # to make sure that main doesn't run too fast or too slow


# setup window
WIN = pygame.display.set_mode((WIDTH + 300, HEIGHT))
pygame.display.set_caption('Checkers')

def get_pos_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

# event loop
def main():
    run = True
    
    game = Game(WIN) 

    while run:
        clock.tick(FPS)
        
        for event in pygame.event.get(): # check if any event has are happen in the currrent time
            
            if Vars.game_mode == 'AI':
                if game.turn == Vars.ai_color:
                    value, new_board = minimax(game.get_board(), 4, Vars.ai_color ,game, Vars.ai_color, Vars.player_color, False)
                    game.ai_move(new_board) #ai have move and update the board
            
            if event.type == pygame.QUIT:
                run = False
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_pos_from_mouse(pos)
                game.select(row, col)
                
                #if restart
                game.restart(WIN)
                
                if game.home(WIN) == True:
                    main_menu()
                    run = False
        
        game.update()
    
    pygame.quit() # while loop ends
  
def main_menu():
    run = True
    clock = pygame.time.Clock()
    
    while run:
        menu = Menu(WIN)
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if menu.draw_player() == True:
                    Vars.game_mode = "player"
                    main()
                    run = False
                elif menu.draw_black() == True:
                    Vars.player_color = BLACK
                    Vars.ai_color = RED
                    Vars.game_mode = "AI"
                    main()
                    run = False
                elif menu.draw_red() == True:
                    Vars.player_color = RED
                    Vars.ai_color = BLACK
                    Vars.game_mode = "AI"
                    main()
                    run = False  
                    
        menu.update()
        
    pygame.quit()
                      
main_menu()
#main()