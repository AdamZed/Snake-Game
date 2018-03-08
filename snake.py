from random import randint
class Snake:
    def __init__(self, board_size, growth_rate):
        self.board_size = board_size
        self.growth_rate = growth_rate
        self.reset()

    def move(self, key):
        if abs(key) != self.last_key:
            if key == 1:
                self.step = [0,-1]
                self.last_key = abs(key)
            elif key == -1:
                self.step = [0,1]
                self.last_key = abs(key)
            elif key == 2:
                self.step = [-1,0]
                self.last_key = abs(key)
            elif key == -2:
                self.step = [1,0]
                self.last_key = abs(key)

        self.head = [self.head[0]+self.step[0], self.head[1]+self.step[1]]
        if self.good_move():
            self.body.append(self.head)
            if self.persist: self.persist-=1
            else: del self.body[0]
        else: return False
        if self.head == self.apple: self.get_apple()
        return True

    def get_apple(self):
        self.persist+=self.growth_rate
        self.length+=self.growth_rate
        self.gen_apple()

    def gen_apple(self):
        while True:
            self.apple = [randint(1,self.board_size[0]), randint(1,self.board_size[1])]
            if self.apple not in self.body: return

    def good_move(self):
        if self.head in self.body: return False
        if self.head[0] > self.board_size[0] or self.head[0] < 1: return False
        if self.head[1] > self.board_size[1] or self.head[1] < 1: return False
        return True

    def reset(self):
        self.length = 1
        self.persist = 0
        self.head = [self.board_size[0]//2, self.board_size[1]//2]
        self.body = [self.head]
        self.gen_apple()
        self.last_key = 0
        self.step = [0,0]