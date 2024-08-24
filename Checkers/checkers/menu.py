import pygame
from .constants import *
from .button import Button
    
    
    
class Menu:
    def __init__(self, win) -> None:
        self.win = win
        self.fill()
        self.draw_player()
        self.draw_computer()
        self.draw_name()
        self.draw_black()
        self.draw_red()

    
    def fill(self):
        self.win.fill(LIGHT_PURPLE)
    
    def draw_player(self):
        button = Button((WIDTH + HUD_WIDTH) / 4, HEIGHT / 2, PLAYER)
        return button.draw(self.win)
    
    def draw_computer(self):
        button = Button((WIDTH + HUD_WIDTH) * 3 / 4, HEIGHT / 2, COMPUTER)
        return button.draw(self.win)
    
    def draw_black(self):
        button = Button((WIDTH + HUD_WIDTH) * 3 / 4 - 70, HEIGHT / 2 + 200, BLACK_PIC)
        return button.draw(self.win)
    
    def draw_red(self):
        button = Button((WIDTH + HUD_WIDTH) * 3 / 4 + 70, HEIGHT / 2 + 200, RED_PIC)
        return button.draw(self.win)
    
    def draw_name(self):        
        txt_name = NAME_FONT.render("CHECKERS!", True, DARK_PURPLE)
        txt_name_rect = txt_name.get_rect()
        txt_name_rect.center = ((WIDTH + HUD_WIDTH) / 2, HEIGHT / 5)
        self.win.blit(txt_name, txt_name_rect) 
    
    def update(self):
        pygame.display.update()