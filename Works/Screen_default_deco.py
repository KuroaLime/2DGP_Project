from pico2d import *
from canvas_size import *

class Black_bar:
    def __init__(self):
        self.image = load_image('Resource/deco/LETTERBOX.png')
    def update(self):
        pass
    def draw(self):
        self.image.draw(WID//2,HEI//2)