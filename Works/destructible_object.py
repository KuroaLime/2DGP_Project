from pico2d import *
import game_framework
import play_state
import random
import Playable_Kyoko
class Vending_machine:
    image=None
    def __init__(self):
        self.x, self.y= 800,500
        self.frame = 0
        self.state=0 #0:평범한 상태 1:파괴된 상태
        if Vending_machine.image == None:
            Vending_machine.image = load_image('Resource/destructible_object/vending_machine_Normal.png')

    def update(self):
        self.x = play_state.background.WID
        self.y = play_state.background.HEI
        if self.state == 1:
            Vending_machine.image = load_image('Resource/destructible_object/vending_machine_broken.png')
            self.state += 1
    def draw(self):
        draw_rectangle(*self.get_bb())
        if self.state == 0:
            self.image.clip_composite_draw(0, 0, 81, 81, 0, '', self.x, self.y, 200, 200)
        elif self.state == 1 or self.state == 2 :
            self.image.clip_composite_draw(23, 23, 101, 101, 0, '', self.x, self.y, 200, 200)
    def get_bb(self):  # 적, 자판기등의 오브젝트와의 충돌범위
        return self.x - 72, self.y - 95, self.x + 45, self.y + 70


    def handle_collision(self, other, group):
        print('Boy and Player collsion')
        left_a, bottom_a, right_a, top_a = other.get_bb()
        left_b, bottom_b, right_b, top_b = self.get_bb()


