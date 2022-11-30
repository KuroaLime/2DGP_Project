from pico2d import *
import game_framework
import server
import random
class Vending_machine:
    image=None
    def __init__(self):
        self.x, self.y= 800,500
        self.frame = 0
        self.state=0 #0:평범한 상태 1:파괴된 상태
        if Vending_machine.image == None:
            Vending_machine.image = load_image('Resource/destructible_object/vending_machine_Normal.png')
        self.under_attack = False

    def update(self):
        print('state : ', self.state)
        if self.state == 1:
            Vending_machine.image = load_image('Resource/destructible_object/vending_machine_broken.png')
            self.state += 1
    def draw(self):
        draw_rectangle(*self.get_bb())
        sx, sy = self.x - server.background.window_left, self.y - server.background.window_bottom
        if self.state == 0:
            self.image.clip_composite_draw(0, 0, 81, 81, 0, '', sx, sy, 300, 300)
        elif self.state == 1 or self.state == 2 :
            self.image.clip_composite_draw(23, 23, 101, 101, 0, '', sx, sy, 300, 300)
    def get_bb(self):  # 적, 자판기등의 오브젝트와의 충돌범위
        sx, sy = self.x - server.background.window_left, self.y - server.background.window_bottom
        return sx - 160, sy - 110, sx + 160, sy + 130


    def handle_collision(self, other, group):
        left_a, bottom_a, right_a, top_a = other.get_bb()
        left_b, bottom_b, right_b, top_b = self.get_bb()


class Gold_statue:
    image = None
    def __init__(self):
        self.x, self.y = 0, 0
        self.rand_x, self.rand_y = random.randint(400, 800), 500
        self.frame = 0
        self.state = 0
        if Gold_statue.image == None:
            Gold_statue.image = load_image('Resource/destructible_object/Different_types of_destructible_objects.png')
    def update(self):
        pass
    def draw(self):
        draw_rectangle(*self.get_bb())
        sx, sy = self.x - server.background.window_left, self.y - server.background.window_bottom
        if self.state == 0:
            self.image.clip_composite_draw(1470, 100, 90, 170, 0, '', sx, sy, 200, 250)
        elif self.state == 1:
            self.image.clip_composite_draw(1000, 420, 85, 175, 0, '', sx, sy, 200, 250)
        elif self.state == 2:
            self.image.clip_composite_draw(1185, 490, 85, 145, 0, '', sx, sy, 200, 250)
        else:
            self.image.clip_composite_draw(1265, 655, 80, 80, 0, '', sx, sy, 200, 250)
    def get_bb(self):
        sx, sy = self.x - server.background.window_left, self.y - server.background.window_bottom
        return sx-100, sy - 130, sx+100, sy + 130
    def handle_collision(self, other, group):
        pass


