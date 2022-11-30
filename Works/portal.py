from pico2d import *
import game_framework
import server
import random

class Portal:
    def __init__(self):
        self.x, self.y = 1920, 700

    def update(self):
        pass
    def draw(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):  # 적, 자판기등의 오브젝트와의 충돌범위
        sx, sy = self.x - server.background.window_left, self.y - server.background.window_bottom
        return sx - 200, sy - 170, sx + 200, sy + 240

    def handle_collision(self, other, group):
        # print('Boy and Player collsion')
        left_a, bottom_a, right_a, top_a = other.get_bb()
        left_b, bottom_b, right_b, top_b = self.get_bb()
        # print('collision Portal!!!!!!')
        if left_a > left_b and right_a < right_b and top_a > top_b:
            other.portalState = True
