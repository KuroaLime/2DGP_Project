from pico2d import *
from canvas_size import *

class Black_bar:
    def __init__(self):
        self.image = load_image('Resource/deco/LETTERBOX.png')
        self.x =WID//2
        self.y =HEI//2

    def __getstate__(self):
        state = {}
        return state

    def __setstate__(self, state):
        self.__init__()
        self.__dict__.update(state)
    def update(self):
        pass
    def draw(self):
        self.image.draw(WID//2,HEI//2)