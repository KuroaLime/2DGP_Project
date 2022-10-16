from pico2d import *
from canvas_size import *

class black_bar:
    def __init__(self):
        self.image = load_image('Resource/deco/LETTERBOX.png')

    def draw(self):
        self.image.draw(WID//2,HEI//2)