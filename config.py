import json
class Config:
    def __init__(self):
        with open('config.json', 'r') as f:
            CONFIG = json.load(f)

        self.screen_size = self.screen_width, self.screen_height = CONFIG['resolution']['width'], CONFIG['resolution']['height']
        self.FPS = CONFIG['resolution']['fps']

        self.snake_growth = CONFIG['game']['growth']
        self.snake_speed = CONFIG['game']['speed']
        self.cell_size = {
            'full': CONFIG['game']['cell_size'],
            'snake': int(CONFIG['game']['cell_size']*0.9)
        }

        self.board_size = [self.screen_width//self.cell_size['full'], self.screen_height//self.cell_size['full']]
        self.big_size = self.board_size[0] if self.board_size[0] > self.board_size[1] else self.board_size[1]
        self.gap = (self.cell_size['full']-self.cell_size['snake'])//2
        self.xy = { 'full': [a*self.cell_size['full'] for a in range(self.big_size)] }
        self.xy['snake'] = [a+self.gap for a in self.xy['full']]

        self.BLACK = (0, 0, 0)
        self.WHITE = (255,255,255)
        self.BLUE = (0, 0, 255)
        self.L_BLUE = (0, 100, 255)
        self.RED = (255, 0, 0)