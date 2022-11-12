from pico2d import *
import game_framework
import game_world

class Phone_background:
    def __init__(self):
        self.image=load_image('Resource/Menu/Phone.png')
    def update(self):
        pass
    def draw(self):
        self.image.clip_composite_draw(2050, 1880, 500, 755,0, '', 500, 550, 500, 800)