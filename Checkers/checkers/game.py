import pygame
from .board import Board
from .constants import *

class Game:
    def __init__(self, win) -> None:
        self._init()
        self.win = win
    
    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = RED
        self.valid_moves = {}
     
    def update(self):
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()
        
    def reset(self):
        self._init()
        
    def select(self, row, col):
        if self.selected: #already selected
            result = self._move(row, col) #selected must be valid
            if not result: #if is not valid
                self.selected = None
                self.select(row, col) #reselect
                
        piece = self.board.get_piece(row, col)
        if (piece != 0) and (piece.color == self.turn):
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True
        return False
        
    def _move(self, row, col):
        piece = self.board.get_piece(row, col)
        if self.selected and (piece == 0) and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            skipped = self.valid_moves[(row, col)]
            if skipped:
                self.board.remove(skipped)
            self.change_turn()
        else:
            return False
        
        return True

    def draw_valid_moves(self, moves):
        for move in moves: #moves are dictionary 
            row, col = move
            pygame.draw.circle(self.win, BLUE, (col * SQUARE_SIZE + SQUARE_SIZE // 2 , row * SQUARE_SIZE + SQUARE_SIZE // 2), 15)
    
    def change_turn(self):
        self.valid_moves = {}
        if self.turn == BLACK:
            self.turn = RED
        else:
            self.turn = BLACK
    
    def restart(self, win):
        if self.board.draw_restart(win) == True:
            self.reset()
            
    def home(self, win):
        return self.board.draw_home(win)
    
    def get_board(self): #for ai
        return self.board
    
    def ai_move(self, board): #for ai
        self.board = board
        self.change_turn()