'''
shallow copy, copy reffrence to an object
deep copy, copy not only the reffrence but the object itself

x = []
y = deepcopy(x) # x or y wouldn't modify eachother
'''
from copy import deepcopy
import pygame
from .constants import WHITE, RED

def minimax(position, depth, max_player, game, AI_color, player_color, show_all_moves):
    # position:  First Board, tell us all the pieces information
    # depth: how many positions do i wanna consider
    # max_player: looking for maximize the score or minimize it
    # game: 
    
    # furthest down that we can go OR if someone won
    if depth == 0 or position.winner() != 0: 
        return position.evaluate(), position
    
    if max_player:
        maxEval = float('-inf')
        best_move = None
        for move in get_all_move(position, AI_color, game, show_all_moves): #for every single move that we can make
            evaluation = minimax(move, depth - 1, False, game, AI_color, player_color, show_all_moves)[0] #we just want maxEval
            maxEval = max(maxEval, evaluation) #how good this move is
            if maxEval == evaluation:
                best_move = move
        return maxEval, best_move
    else: #get worst moves for opponnent
        minEval = float('inf')
        best_move = None
        for move in get_all_move(position, player_color, game, show_all_moves): #for every single move that we can make
            evaluation = minimax(move, depth - 1, True, game, AI_color, player_color, show_all_moves)[0] #we just want minEval
            minEval = min(minEval, evaluation) #how bad this move is
            if minEval == evaluation:
                best_move = move
        return minEval, best_move


def get_all_move(board, color, game, show_all_moves:bool):
    moves = [] #[board1, board2] board that we get from moving that piece
    for piece in board.get_all_pieces(color):
        valid_moves = board.get_valid_moves(piece)
        for move, skip in valid_moves.items(): #(row, col):[piece]
            if show_all_moves == True:
                draw_moves(game, board, piece)
            temp_board = deepcopy(board)
            temp_piece = temp_board.get_piece(piece.row, piece.col)
            new_board = simulate_move(temp_piece, move, temp_board, game, skip) #make new move anf return the new board
            moves.append(new_board)
    return moves
            
def simulate_move(piece, move, board, game, skip):
    board.move(piece, move[0], move[1]) #piece, row, col
    if skip: #jump over a piece
        board.remove(skip)
    return board

def draw_moves(game, board, piece):
    valid_moves = board.get_valid_moves(piece)
    board.draw(game.win)
    pygame.draw.circle(game.win, (0, 255, 0), (piece.x, piece.y), 50, 5)
    game.draw_valid_moves(valid_moves.keys())
    pygame.display.update()
    pygame.time.delay(100)

RED = (0, 0, 255)