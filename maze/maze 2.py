import pygame
# to evaluate duration
import time
# for music and sfx
from pygame import mixer
# for ai analyse
import numpy as np
from sklearn.linear_model import LinearRegression

class GameAnalyzer:
    def __init__(self):
        # train linear regression model
        self.model = LinearRegression()
        self.train_model()

    def train_model(self):
        # Training data
        # x is input. x = (duration, penalty)
        # y is output and shows score.
        X_train = np.array([[30, 0], [40, 1], [50, 2], [70, 3], [70, 4]])
        y_train = np.array([950, 900, 850, 800, 750])
        
        # train model
        self.model.fit(X_train, y_train)

    def analyze_game(self, duration, penalty):
        # Score prediction using the model
        X_test = np.array([[duration, penalty]])
        score = self.model.predict(X_test)[0]
        return score

    def display_analysis(self, screen, duration, penalty ):
        score = self.analyze_game(duration, penalty)
        run = True
        while run:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            # Show result
            screen.fill(BLACK)
            font = pygame.font.Font(None, 74)
            win_txt = font.render("You Win!", 1, GREEN)
            screen.blit(win_txt, (WIDTH // 2 - win_txt.get_width() // 2, HEIGHT // 2 - win_txt.get_height() // 2))
            
            font_small = pygame.font.Font(None, 36)
            score_txt = font_small.render(f"Score: {score:.2f}", 1, WHITE)
            screen.blit(score_txt, (WIDTH // 2 - score_txt.get_width() // 2, HEIGHT // 2 + win_txt.get_height()))
            
            details = f"Time: {duration:.2f}s, Penalty: {int(penalty)}"
            details_txt = font_small.render(details, 1, WHITE)
            screen.blit(details_txt, (WIDTH // 2 - details_txt.get_width() // 2, HEIGHT // 2 + win_txt.get_height() * 1.7))

            # Update screen
            pygame.display.flip()

        pygame.quit()

# Initialize Pygame
pygame.init()

# Constants
TILE_SIZE = 30
WIDTH = TILE_SIZE * 32
HEIGHT = TILE_SIZE * 32
FPS = 30

# Setup display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Game")

# Images
image = pygame.image.load(r'.\images\empty.png')
empty_img = pygame.transform.scale(image, (TILE_SIZE, TILE_SIZE))
image = pygame.image.load(r'.\images\wall.png')
wall_img = pygame.transform.scale(image, (TILE_SIZE, TILE_SIZE))
image = pygame.image.load(r'.\images\goal.png')
goal_img = pygame.transform.scale(image, (TILE_SIZE, TILE_SIZE))
image = pygame.image.load(r'.\images\player1.png')
player_img = pygame.transform.scale(image, (TILE_SIZE, TILE_SIZE))
image = pygame.image.load(r'.\images\penalty.png')
penalty_img = pygame.transform.scale(image, (TILE_SIZE, TILE_SIZE))

# tiles will be used for creating the map
tiles = [empty_img, wall_img]

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Music and SFX
mixer.pre_init(44100, 16, 2, 4096)
mixer.init()
mixer.music.load(r'.\sfx\music.wav')
mixer.music.set_volume(0.2)
mixer.music.play(-1)  # -1 for looping the music

sfx_stop = mixer.Sound(r'.\sfx\stop.wav')
sfx_stop.set_volume(1.0)

# Map
maze = [
    #0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], #0
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], #1
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1], #2
    [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1], #3
    [1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1], #4
    [1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1], #5
    [1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1], #6
    [1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1], #7
    [1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1], #8
    [1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1], #9
    [1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1], #10
    [1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1], #11
    [1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1], #12
    [1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1], #13
    [1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1], #14
    [1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1], #15
    [1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1], #16
    [1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1], #17
    [1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1], #18
    [1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1], #19
    [1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1], #20
    [1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1], #21
    [1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1], #22
    [1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1], #23
    [1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1], #24
    [1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1], #25
    [1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1], #26
    [1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1], #27
    [1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1], #28
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1], #29
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], #30
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]  #31
]

# Player starting position
player_pos = [2, 2]

# Goal position
goal_pos = [29, 22]

# Game clock
clock = pygame.time.Clock()

# Game start time - use for evaluate duration
start_time = time.time()

def draw_maze():
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            x = col * TILE_SIZE
            y = row * TILE_SIZE
            tile = tiles[maze[row][col]]
            screen.blit(tile, (x, y))

def draw_player():
    screen.blit(player_img, (player_pos[0] * TILE_SIZE, player_pos[1] * TILE_SIZE))

def draw_goal():
    screen.blit(goal_img, (goal_pos[0] * TILE_SIZE, goal_pos[1] * TILE_SIZE))
    
# Stack to undo
move_stack = []
    
# Main game loop
def main():
    global player_pos
    running = True    # for game loop
    play = True       # let player moves
    can_move = [1, 1, 1, 1] # Avoids movement by holding the button
    can_return = 1
    penalty = 0 # counts srops
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        new_pos = list(player_pos)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and can_move[0]:
                new_pos[1] -= 1
                can_move[0] = 0
            elif event.key == pygame.K_DOWN and can_move[1]:
                new_pos[1] += 1
                can_move[1] = 0
            elif event.key == pygame.K_LEFT and can_move[2]:
                new_pos[0] -= 1
                can_move[2] = 0
            elif event.key == pygame.K_RIGHT and can_move[3]:
                new_pos[0] += 1
                can_move[3] = 0
            elif event.key == pygame.K_RETURN and move_stack and can_return:
                new_pos = move_stack.pop()  
                player_pos = new_pos 
                can_return = 0
                continue
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP and can_move[0] == 0:
                can_move[0] = 1
            elif event.key == pygame.K_DOWN and can_move[1] == 0:
                can_move[1] = 1
            elif event.key == pygame.K_LEFT and can_move[2] == 0:
                can_move[2] = 1
            elif event.key == pygame.K_RIGHT and can_move[3] == 0:
                can_move[3] = 1
            elif event.key == pygame.K_RETURN and can_return == 0:
                can_return = 1
                

        # Check for wall collision
        if maze[new_pos[1]][new_pos[0]] == 0 and play:
            if new_pos != player_pos:
                move_stack.append(player_pos)
            player_pos = new_pos
        else :
             penalty += 1
             play = False
        
        # Penalty 
        if play == False:
            sfx_stop.play()
            time.sleep(1)
            play = True
            
        # Update screen
        screen.fill(BLACK)
        draw_maze()
        draw_player()
        draw_goal()
        
        pygame.display.flip()
        clock.tick(FPS)
        
        # End game
        if player_pos == goal_pos and running:
            end_time = time.time()
            duration = end_time - start_time
            display_winner(duration, penalty)
            running = False
            

    pygame.quit()

def display_winner(duration, penalty):
    analyzer = GameAnalyzer()
    analyzer.display_analysis(screen, duration, penalty)
    
    # --- score without Analyzer ---
    # if penalty == 0:
    #     penalty = 0.2
    # run = True
    # while run:
    #     clock.tick(FPS)
    #     for event in pygame.event.get():
            
    #         if event.type == pygame.QUIT:
    #             run = False
    #     # win txt
    #     screen.fill(BLACK)
    #     font = pygame.font.Font(None, 74)
    #     win_txt = font.render("You Win!", 1, GREEN)
    #     screen.blit(win_txt, (WIDTH // 2 - win_txt.get_width() // 2, HEIGHT // 2 - win_txt.get_height() // 2))
    #     # score txt
    #     font_small = pygame.font.Font(None, 36)
    #     score = f"Score: {int(1000 - (100 / duration*penalty))}"
    #     score_txt = font_small.render(score, 1, WHITE)        
    #     screen.blit(score_txt, (WIDTH // 2 - score_txt.get_width() // 2, HEIGHT // 2 + win_txt.get_height()))
    #     # details txt
    #     details = f"Time: {duration:.2f}s, Penalty: {int(penalty)}"
    #     details_txt = font_small.render(details, 1, WHITE)
    #     screen.blit(details_txt, (WIDTH // 2 - details_txt.get_width() // 2, HEIGHT // 2 + win_txt.get_height() * 1.7))
        
    #     pygame.display.flip()
        
    #pygame.quit()
    
if __name__ == "__main__":
    main()