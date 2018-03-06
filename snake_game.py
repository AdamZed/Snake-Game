import sys, pygame, json
from time import sleep
from snake import Snake
from config import Config

pygame.init()
CFG = Config()
SNAKE = Snake(CFG.board_size, CFG.snake_growth)
SCREEN = pygame.display.set_mode(CFG.screen_size)
font = pygame.font.SysFont("monospace", CFG.screen_size[1]//20)
after_font = pygame.font.SysFont("monospace", CFG.screen_size[1]//10)

status = {
    'playing': False,
    'g_over': False
}

def game_over():
    status['playing'] = False
    status['g_over'] = True
    score = after_font.render(f"Final Score: {SNAKE.length}", True, CFG.WHITE)
    SCREEN.blit(score, (CFG.screen_size[0]//4, CFG.screen_size[1]//2))
    pygame.display.flip()

def reset_board():
    status['g_over'] = False
    SNAKE.reset()
    draw_screen()

def draw_screen():
    SCREEN.fill(CFG.BLACK)
    pygame.draw.rect(SCREEN, CFG.BLUE, (CFG.xy_snake[SNAKE.head[0]-1],CFG.xy_snake[SNAKE.head[1]-1],CFG.snake_size,CFG.snake_size))
    for place in SNAKE.body:
        if place == SNAKE.head: continue
        pygame.draw.rect(SCREEN, CFG.L_BLUE, (CFG.xy_snake[place[0]-1],CFG.xy_snake[place[1]-1],CFG.snake_size,CFG.snake_size))
    pygame.draw.rect(SCREEN, CFG.RED, (CFG.xy[SNAKE.apple[0]-1],CFG.xy[SNAKE.apple[1]-1],CFG.cell_size,CFG.cell_size))
    score = font.render(str(SNAKE.length), True, CFG.WHITE)
    SCREEN.blit(score, (10,10))
    pygame.display.flip()

def update(key):
    move = SNAKE.move(key)
    if not move:
        game_over()
        return
    draw_screen()

def get_key(keydown):
    if keydown == pygame.K_UP: return 1
    elif keydown == pygame.K_DOWN: return -1
    elif keydown == pygame.K_LEFT: return 2
    elif keydown == pygame.K_RIGHT: return -2
    else: return 0


draw_screen()
mcount = 0
frame_step = 1000//CFG.FPS
key=0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        elif event.type == pygame.KEYDOWN:
            while status['playing']:
                key = get_key(event.key)
                break
            else:
                if not status['g_over']:
                    status['playing'] = True
                    key = get_key(event.key)
                else:
                    if mcount > 500: #instant reset prevention
                        reset_board()
                        mcount = 0
    if status['playing']:
        if mcount % CFG.snake_speed == 0:
            update(key)
            mcount = 0
        elif mcount % frame_step == 0 and key!= 0:                    
            update(key)
            key = 0
            mcount = 0
        sleep(0.001)
        mcount+=1       
    else:  
        sleep(0.001)
        mcount+=1