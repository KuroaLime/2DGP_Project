from pico2d import *
from canvas_size import *

class first_stage:
    def __init__(self):
        self.image = load_image('Resource/stage/stage01/first_stage_sheet.png')
        self.image = self.image.clip_image(804,0,677,233)

    def draw(self):
        self.image.draw(WID//2+400,HEI//2,2970,990)

