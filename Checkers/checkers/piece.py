import pygame
from .constants import *

class Piece:
    PADDING = 15 #from each cube
    OUTLINE = 2

    def __init__(self, row, col, color) -> None:
        self.row = row
        self.col = col
        self.color = color
        self.king = False        
        self.x = 0
        self.y = 0
        self.position() 
    
    def position(self):#we need to call func many times
        self.x = (SQUARE_SIZE * self.col) + (SQUARE_SIZE // 2) #middle of square
        self.y = (SQUARE_SIZE * self.row) + (SQUARE_SIZE // 2)

    def make_king(self):
        self.king = True

    def draw(self, win): #draw piece in window
        radius = (SQUARE_SIZE // 2) - self.PADDING
        pygame.draw.circle(win, GRAY, (self.x, self.y), radius + self.OUTLINE) #outline
        pygame.draw.circle(win, self.color, (self.x, self.y), radius) #real one
        if self.king:
            win.blit(CROWN, (self.x - CROWN.get_width() // 2, self.y - CROWN.get_height() // 2) )
            
    def move(self, row, col):
        self.row = row
        self.col = col
        self.position()

    def __repr__(self) -> str: #for debug
        return f"{self.color}, {self.x}, {self.y}"
        