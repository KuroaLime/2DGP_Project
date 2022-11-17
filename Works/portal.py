from pico2d import *
import game_framework
import play_state
import random

class Portal:
    def __init__(self):
        self.x, self.y = 0, 0

    def update(self):
        pass
    def draw(self):
        draw_rectangle(*self.get_bb())
        draw_rectangle(*self.get_TT())

    def get_bb(self):  # 적, 자판기등의 오브젝트와의 충돌범위
        return self.x - 72, self.y - 95, self.x + 45, self.y + 85

    def get_TT(self):  # 스테이지와의 충돌
        return self.x - 70, self.y - 95, self.x + 45, self.y - 80

    def handle_collision(self, other, group):
        # print('Boy and Player collsion')
        left_a, bottom_a, right_a, top_a = other.get_bb()
        left_b, bottom_b, right_b, top_b = self.get_bb()

        if left_a < left_b:
            self.x += 1
        if right_a > right_b:
            self.x += -1
        if top_a > top_b:
            self.y += -1
        if bottom_a < bottom_b:
            self.y += 1