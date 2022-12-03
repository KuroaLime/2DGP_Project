from pico2d import *
import server
import canvas_size
import game_framework

FRAMES_PER_ACTION_NORMAL_ATTACK00 = 6
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION_PUNCH = 3

animation_names = ['punch_load']

class Loading:
    image= None
    def __init__(self):
        if Loading.image == None:
            Loading.image = load_image('Resource/loading/black_screen.png')
        self.x = get_canvas_width() // 2
        self.y = get_canvas_height() // 2

    def update(self):
        pass
    def draw(self):
        if server.stage.next_stage == True :
            self.image.draw(self.x, self.y,canvas_size.WID,canvas_size.HEI)

class Punch_loading:
    images = None
    def load_images(self):
        if Punch_loading.images == None:
            Punch_loading.images = {}
            for name in animation_names:
                Punch_loading.images[name] = [load_image("./Resource/loading/"+ name + "(%d)" % i + ".png") for i in range(1, 4)]
    def __init__(self):
        self.load_images()
        self.x = get_canvas_width() -80
        self.y = 50
        self.frame = 0
    def update(self):
        if server.stage.next_stage == True:
            self.frame = (self.frame + FRAMES_PER_ACTION_PUNCH * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION_PUNCH

    def draw(self):
        if server.stage.next_stage == True:
            Punch_loading.images['punch_load'][int(self.frame)].draw(self.x, self.y)