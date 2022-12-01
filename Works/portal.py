from pico2d import *
import game_framework
import server
import random
max_dead_enermy = [4,4,4,4,4,4,4,1]
class Portal:
    def __init__(self):
        self.x, self.y = 1920, 700

    def update(self):
        pass
    def draw(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        sx, sy = self.x - server.stage.window_left, self.y - server.stage.window_bottom
        return sx - 200, sy - 170, sx + 200, sy + 240

    def handle_collision(self, other, group):
        # print('Boy and Player collsion')
        left_a, bottom_a, right_a, top_a = other.get_bb()
        left_b, bottom_b, right_b, top_b = self.get_bb()
        # print('collision Portal!!!!!!')
        if server.stage.dead_enermy == max_dead_enermy[server.stage.stage_number]:
            other.portalState = True


class Portal2:
    def __init__(self):
        self.x, self.y = 1920, 700

    def update(self):
        pass
    def draw(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        sx, sy = self.x - server.stage.window_left, self.y - server.stage.window_bottom
        return sx - 200, sy - 170, sx + 200, sy + 240

    def handle_collision(self, other, group):
        # print('Boy and Player collsion')
        left_a, bottom_a, right_a, top_a = other.get_bb()
        left_b, bottom_b, right_b, top_b = self.get_bb()
        # print('collision Portal!!!!!!')

        other.portalState = True