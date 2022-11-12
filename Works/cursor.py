from pico2d import *
import game_framework
import game_world

class Cursor:
    def __init__(self):
        self.my_button_dir = 0
        self.image_dir = [(500, 750), (350, 700), (350, 650), (350, 550), (350, 500), (350, 450), (375, 225)]
        self.image=load_image('Resource/title/title_component.png')
    def update(self):

        pass
    def draw(self):
        self.image.clip_draw(175, 590, 67, 40, self.image_dir[self.my_button_dir][0], self.image_dir[self.my_button_dir][1])

