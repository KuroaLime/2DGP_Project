from pico2d import *
import game_framework
import game_world

class Phone_boarder:
    def __init__(self):
        self.image=load_image('Resource/Menu/Phone.png')
    def update(self):
        pass
    def draw(self):
        self.image.clip_composite_draw(2060, 820, 609, 1053,0, '', 500, 550, 595, 1050)