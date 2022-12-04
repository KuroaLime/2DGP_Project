from pico2d import *
import game_framework
import game_world
import server
animation_name = ['non-selection', 'selection']
class non_select_Menu_icon:
    images = None
    def load_images(self):
        if non_select_Menu_icon.images == None:
            non_select_Menu_icon.images = [load_image("./Resource/Menu/non_selection.png")]
    def __init__(self):
        self.load_images()
        self.x= [500, 500,500]
        self.y = [730, 690, 650]
    def update(self):
        pass
    def draw(self):
        if server.Menu_button_location != 0:
            non_select_Menu_icon.images[0].draw(self.x[0], self.y[0], 20, 20)
        if server.Menu_button_location != 1:
            non_select_Menu_icon.images[0].draw(self.x[1], self.y[1], 20, 20)
        if server.Menu_button_location != 2:
            non_select_Menu_icon.images[0].draw(self.x[2], self.y[2], 20, 20)


class select_Menu_icon:
    images = None
    def load_images(self):
        if select_Menu_icon.images == None:
            select_Menu_icon.images = [load_image("./Resource/Menu/non_selection.png")]
    def __init__(self):
        self.load_images()
        self.x= [500, 500,500]
        self.y = [730, 690, 650]
    def update(self):
        pass
    def draw(self):
        if server.Menu_button_location == 0:
            select_Menu_icon.images[0].draw(self.x[0], self.y[0], 20, 20)
        elif server.Menu_button_location == 1:
            select_Menu_icon.images[0].draw(self.x[1], self.y[1], 20, 20)
        elif server.Menu_button_location == 2:
            select_Menu_icon.images[0].draw(self.x[2], self.y[2], 20, 20)