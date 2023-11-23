from pico2d import *
import game_world
import game_framework
import random

import server


class Ball:
    image = None

    def __init__(self, x = None, y = None):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x = x if x else random.randint(100, 1180)
        self.y = y if y else random.randint(100, 924)

    def draw(self):
        self.sx, self.sy = self.x - server.background.window_left, self.y - server.background.window_bottom
        # 소년을 화면 한 가운데 그림
        self.image.clip_draw(0,0,21, 21, self.sx, self.sy)


        draw_rectangle(*self.get_bb())

    def update(self):

        pass

    def get_bb(self):
        self.sx, self.sy = self.x - server.background.window_left, self.y - server.background.window_bottom
        return self.sx - 10, self.sy - 10, self.sx + 10, self.sy + 10

    def handle_collision(self, group, other):
        match group:
            case 'boy:ball':
                game_world.remove_object(self)
                print('a')
