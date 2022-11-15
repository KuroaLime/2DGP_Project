from pico2d import *
import game_framework
import play_state
import random
import Playable_Kyoko
import game_world
class Apple:
    image=None
    def __init__(self):
        self.x, self.y = 0, 0
        self.rand_x, self.rand_y = random.randint(200, 900), random.randint(-200, 0)
        self.frame = 0
        self.state=0 #0:평범한 상태 1:파괴된 상태
        if Apple.image == None:
            Apple.image = load_image('Resource/Food/apple.png')

    def update(self):
        self.x = self.rand_x+play_state.background.WID
        self.y = self.rand_y+play_state.background.HEI
    def draw(self):
        draw_rectangle(*self.get_bb())
        self.image.clip_composite_draw(59, 54, 14, 18, 0, '', self.x, self.y, 30, 30)
    def get_bb(self):  # 적, 자판기등의 오브젝트와의 충돌범위
        return self.x - 20, self.y - 20, self.x +20, self.y + 20


    def handle_collision(self, other, group):
        print('Boy and Player collsion')
        left_a, bottom_a, right_a, top_a = other.get_bb()
        left_b, bottom_b, right_b, top_b = self.get_bb()

        if left_a < left_b:
            other.item[0] += 1
            game_world.remove_object(self)
        elif right_a > right_b:
            other.item[0] += 1
            game_world.remove_object(self)
        elif top_a - 165 > top_b - 165:
            other.item[0] += 1
            game_world.remove_object(self)
        elif bottom_a < bottom_b:
            other.item[0] += 1
            game_world.remove_object(self)

class Salad:
    image=None
    def __init__(self):
        self.x, self.y = 0, 0
        self.rand_x, self.rand_y = random.randint(200, 900), random.randint(-200, 0)
        self.frame = 0
        self.state=0 #0:평범한 상태 1:파괴된 상태
        if Salad.image == None:
            Salad.image = load_image('Resource/Food/salad.png')

    def update(self):
        self.x = self.rand_x+play_state.background.WID
        self.y = self.rand_y+play_state.background.HEI
    def draw(self):
        draw_rectangle(*self.get_bb())
        self.image.clip_composite_draw(55, 54, 20, 14, 0, '', self.x, self.y, 30, 30)
    def get_bb(self):  # 적, 자판기등의 오브젝트와의 충돌범위
        return self.x - 20, self.y - 20, self.x +20, self.y + 20


    def handle_collision(self, other, group):
        print('Boy and Player collsion')
        left_a, bottom_a, right_a, top_a = other.get_bb()
        left_b, bottom_b, right_b, top_b = self.get_bb()

        if left_a < left_b:
            other.item[0] += 1
            game_world.remove_object(self)
        elif right_a > right_b:
            other.item[0] += 1
            game_world.remove_object(self)
        elif top_a - 165 > top_b - 165:
            other.item[0] += 1
            game_world.remove_object(self)
        elif bottom_a < bottom_b:
            other.item[0] += 1
            game_world.remove_object(self)

class Chicken:
    image=None
    def __init__(self):
        self.x, self.y = 0, 0
        self.rand_x, self.rand_y = random.randint(200, 900), random.randint(-200, 0)
        self.frame = 0
        self.state=0 #0:평범한 상태 1:파괴된 상태
        if Chicken.image == None:
            Chicken.image = load_image('Resource/Food/chicken.png')

    def update(self):
        self.x = self.rand_x+play_state.background.WID
        self.y = self.rand_y+play_state.background.HEI
    def draw(self):
        draw_rectangle(*self.get_bb())
        self.image.clip_composite_draw(44, 51, 42, 21, 0, '', self.x, self.y, 30, 30)
    def get_bb(self):  # 적, 자판기등의 오브젝트와의 충돌범위
        return self.x - 20, self.y - 20, self.x +20, self.y + 20


    def handle_collision(self, other, group):
        print('Boy and Player collsion')
        left_a, bottom_a, right_a, top_a = other.get_bb()
        left_b, bottom_b, right_b, top_b = self.get_bb()

        if left_a < left_b:
            other.item[0] += 1
            game_world.remove_object(self)
        elif right_a > right_b:
            other.item[0] += 1
            game_world.remove_object(self)
        elif top_a - 165 > top_b - 165:
            other.item[0] += 1
            game_world.remove_object(self)
        elif bottom_a < bottom_b:
            other.item[0] += 1
            game_world.remove_object(self)

