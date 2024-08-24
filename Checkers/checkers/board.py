import pygame
from .constants import *
from .piece import Piece
from .button import Button

class Board:
    def __init__(self) -> None:
        self.board = [] # black or red pieces
        self.red_left = self.black_left = 12
        self.red_king = self.black_king = 0
        self.create_board() #automaticly create the board
        self.red_score = {'x':WIDTH + (HUD_WIDTH / 2), 'y':HEIGHT * 5 / 6, 'radius': 50}
        self.black_score = {'x':WIDTH + (HUD_WIDTH / 2), 'y':HEIGHT / 6, 'radius': 50}
    
    def draw_squares(self, win):
        # create checkered board
        win.fill(BROWN)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2): # place all biege then - یکی در میون
                pygame.draw.rect(win, BIEGE, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
    
    def draw_score(self, win):
        pygame.draw.circle(win, GRAY, (self.red_score['x'], self.red_score['y']), self.red_score['radius'] + 5) #outline
        pygame.draw.circle(win, RED, (self.red_score['x'], self.red_score['y']), self.red_score['radius'])
        pygame.draw.circle(win, GRAY, (self.black_score['x'], self.black_score['y']), self.black_score['radius'] + 5) #outline
        pygame.draw.circle(win, BLACK, (self.black_score['x'], self.black_score['y']), self.black_score['radius'])
        
        txt_red_score = FONT.render(str(12 - self.black_left), True, WHITE)
        txt_red_rect = txt_red_score.get_rect()
        txt_red_rect.center = (self.red_score['x'], self.red_score['y'])
        win.blit(txt_red_score, txt_red_rect)
        
        txt_black_score = FONT.render(str(12 - self.red_left), True, WHITE)
        txt_black_rect = txt_black_score.get_rect()
        txt_black_rect.center = (self.black_score['x'], self.black_score['y'])
        win.blit(txt_black_score, txt_black_rect)     
            
    def draw_winner(self, win):
        if self.winner() == BLACK:
            txt_winner = FONT.render(f"BLACK WINS!", True, BLACK, WHITE)
        else:
            txt_winner = FONT.render(f"RED WINS!", True, RED, WHITE)
                    
        txt_winner_rect = txt_winner.get_rect()
        txt_winner_rect.center = (WIDTH + (HUD_WIDTH / 2), HEIGHT / 2)
        win.blit(txt_winner, txt_winner_rect)
        
    def draw_restart(self, win):
        button = Button(WIDTH + HUD_WIDTH / 2, HEIGHT / 3, RESTART)
        return button.draw(win)
    
    def draw_home(self, win):
        button = Button(WIDTH + HUD_WIDTH / 2, HEIGHT * 2 / 3, HOME)
        return button.draw(win)
    
    def evaluate(self): #it's for ai
        return self.black_left - self.red_left + (self.black_king * 0.5 - self.red_king * 0.5)
    
    def get_all_pieces(self, color): #still for ai
        pieces = [] 
        for row in self.board:
            for piece in row:
                if piece != 0 and piece.color == color:
                    pieces.append(piece)
        return pieces
                        
    def move(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col] #swap position
        piece.move(row, col)
        
        if (row == ROWS - 1) or (row == 0):
            piece.make_king()
            if piece.color == BLACK:
                self.black_king += 1
            else:
                self.red_king += 1
        
    def get_piece(self, row, col):
        try:
            return self.board[row][col]
        except:
            return False

    def create_board(self):
        for row in range(ROWS):
            self.board.append([]) #what each row has inside of it
            for col in range(COLS):
                if (col % 2) == ((row + 1) % 2): #place the pieces
                    if row < 3:
                        self.board[row].append(Piece(row, col, BLACK))
                    elif row > 4:
                        self.board[row].append(Piece(row, col, RED))
                    else:
                        self.board[row].append(0) #empty
                else:
                    self.board[row].append(0) #empty
    
    def draw(self, win):
        self.draw_squares(win)
        self.draw_score(win)
        self.draw_restart(win)
        self.draw_home(win)
        if self.winner() != 0:
            self.draw_winner(win)    
        
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win) 
    
    def remove(self, pieces):
        for piece in pieces:
            self.board[piece.row][piece.col] = 0
            if piece != 0:
                if piece.color == RED:
                    self.red_left -= 1
                else:
                    self.black_left -= 1   
                    
    def winner(self):
        if self.red_left <= 0:
            return BLACK
        elif self.black_left <= 0:
            return RED
    
        return 0    
    
    def get_valid_moves(self, piece):
        moves = {}
        left = piece.col - 1
        right = piece.col + 1
        row = piece.row
        
        if (piece.color == RED) or piece.king:
            #                                 up      max row can go    up               subtract
            moves.update(self._traverse_left(row - 1, max(row - 3, -1), -1, piece.color, left))
            moves.update(self._traverse_right(row - 1, max(row - 3, -1), -1, piece.color, right))
        
        if (piece.color == BLACK) or piece.king:
            moves.update(self._traverse_left(row + 1, min(row + 3, ROWS), 1, piece.color, left))
            moves.update(self._traverse_right(row + 1, min(row + 3, ROWS), 1, piece.color, right))
            
        return moves
    
    def _traverse_left(self, start, stop, step, color, left, skipped=[]):
        moves = {}
        last = []
        for row in range(start, stop, step):
            if left < 0:
                break
            
            cur = self.board[row][left]
            if cur == 0: #found empty square
                if skipped and not last:
                    break
                elif skipped: #duoble jump
                    moves[(row, left)] = last + skipped 
                else: #add possible move
                    moves[(row, left)] = last
                 
                if last: #skip over
                    if step == -1:
                        r = max(row - 3, 0)
                    else:
                        r = min(row + 3, ROWS)
                    # for duoble jump or triple jump
                    moves.update(self._traverse_left(row + step, r, step, color, left - 1, skipped=last))
                    moves.update(self._traverse_right(row + step, r, step, color, left + 1, skipped=last)) 
                break # to make sure          
            elif cur.color == color: #our piece is in that square - same color
                break
            else: #opponent's piece is in the square - different color
                last = [cur]
            
            left -= 1  
        
        return moves
     
    
    def _traverse_right(self, start, stop, step, color, right, skipped=[]):
        moves = {}
        last = []
        for row in range(start, stop, step):
            if right >= COLS:
                break
            
            cur = self.board[row][right]
            if cur == 0: #found empty square
                if skipped and not last:
                    break
                elif skipped: #duoble jump
                    moves[(row, right)] = last + skipped 
                else: #add possible move
                    moves[(row, right)] = last
                 
                if last: #skip over
                    if step == -1:
                        r = max(row - 3, 0)
                    else:
                        r = min(row + 3, ROWS)
                    # for duoble jump or triple jump
                    moves.update(self._traverse_left(row + step, r, step, color, right - 1, skipped=last))
                    moves.update(self._traverse_right(row + step, r, step, color, right + 1, skipped=last)) 
                break # to make sure       
                
            elif cur.color == color: #our piece is in that square - same color
                break
            else: #opponent's piece is in the square - different color
                last = [cur]
            
            right += 1   
            
        return moves