from pico2d import *
import server

class Character_face:
    def __init__(self):

    def update(self):

    def draw(self):
class Hp_bar:
    image = None
    def load_images(self):
        if Hp_bar.image == None:
            Hp_bar.image = load_image('Resource/hp_bar/Hp.png')
    def __init__(self):
        self.load_images()
        self.x = 400
        self.y = 1030
    def update(self):
        pass
    def draw(self):
        sy = self.y - server.stage.window_bottom
        sx = self.x - server.stage.window_left

        for i in range(25):
            Hp_bar.image.composite_draw(0, '', sx + 15 * i, sy, 10, 20)
