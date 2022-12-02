from pico2d import *
import game_framework
import game_world

class Phone_background:
    images = None
    def __init__(self):
        if Phone_background.images == None:
            Phone_background.images = [load_image('Resource/Menu/Phone.png'),load_image('Resource/Menu/normal_ground.png')]
    def update(self):
        pass
    def draw(self):
        Phone_background.images[0].clip_composite_draw(2039,2632 ,496,756, 0, '', 500, 550, 500, 800)
        Phone_background.images[1].composite_draw(0, '', 500, 535, 450, 700)