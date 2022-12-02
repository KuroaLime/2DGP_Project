from pico2d import *
import server

class Character_face:
    image = None

    def load_images(self):
        if Character_face.image == None:
            Character_face.image = load_image('Resource/hp_bar/character_face.png')

    def __init__(self):
        self.load_images()
        self.x = 310
        self.y = 1000

    def update(self):
        pass

    def draw(self):

        Character_face.image.composite_draw(0, '', self.x, self.y, 185, 161)



class Hp_bar:
    image = None
    def load_images(self):
        if Hp_bar.image == None:
            Hp_bar.image = load_image('Resource/hp_bar/Hp.png')
    def __init__(self):
        self.load_images()
        self.x = 400
        self.y = 1020
    def update(self):
        pass
    def draw(self):


        for i in range(25):
            Hp_bar.image.composite_draw(0, '', self.x + 15 * i, self.y, 10, 20)
