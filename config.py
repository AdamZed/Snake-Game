import json
class Config:
    def __init__(self):
        with open('config.json', 'r') as f:
            CONFIG = json.load(f)

        self.screen_size = self.screen_width, self.screen_height = CONFIG['resolution']['width'], CONFIG['resolution']['height']
        self.FPS = CONFIG['resolution']['fps']

        self.cell_size = CONFIG['game']['cell_size']
        self.snake_size = int(self.cell_size*0.9)
        self.snake_growth = CONFIG['game']['growth']
        self.snake_speed = CONFIG['game']['speed']

        self.board_size = [self.screen_width//self.cell_size, self.screen_height//self.cell_size]
        self.big_size = self.board_size[0] if self.board_size[0] > self.board_size[1] else self.board_size[1]
        self.xy = [a*self.cell_size for a in range(self.big_size)]
        self.gap = (self.cell_size-self.snake_size)//2
        self.xy_snake = [a*self.cell_size+self.gap for a in range(self.big_size)]

        self.BLACK = (0, 0, 0)
        self.WHITE = (255,255,255)
        self.BLUE = (0, 0, 255)
        self.L_BLUE = (0, 100, 255)
        self.RED = (255, 0, 0)