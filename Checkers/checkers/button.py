import pygame
from .constants import *
clicked = False

class Button:
    def __init__(self, x, y, image) -> None:
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        
    def draw(self, win):
        global clicked
        action = False
        #get mouse pos
        pos = pygame.mouse.get_pos()
        
        #check mouse over and clicked condition
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and clicked == False: #left clicked
                action = True
                clicked = True
        if pygame.mouse.get_pressed()[0] == 0:
            clicked = False
                    
        #draw button on screen
        win.blit(self.image, (self.rect.x, self.rect.y))
        
        return action