from pico2d import *
import game_framework
import game_world

class Phone_option_instruction:
    def __init__(self):
        self.image=load_image('Resource/Menu/Menu_option.png')
    def update(self):
        pass
    def draw(self):
        self.image.clip_composite_draw(175, 590, 67, 40,0, '', 500, 850, 80, 60)

class Phone_option_music:
    def __init__(self):
        self.image=load_image('Resource/Menu/Menu_option.png')
    def update(self):
        pass
    def draw(self):
        self.image.clip_composite_draw(20,483 ,50,30,0, '', 350, 750, 60, 50)

class Phone_option_soundEffect:
    def __init__(self):
        self.image=load_image('Resource/Menu/Menu_option.png')
    def update(self):
        pass
    def draw(self):
        self.image.clip_composite_draw(20, 445, 75, 30,0, '', 350, 700, 60, 50)

class Phone_option_voice:
    def __init__(self):
        self.image=load_image('Resource/Menu/Menu_option.png')
    def update(self):
        pass
    def draw(self):
        self.image.clip_composite_draw(20, 405, 50, 30,0, '', 350, 650, 60, 50)

class Phone_option_language:
    def __init__(self):
        self.image=load_image('Resource/Menu/Menu_option.png')
    def update(self):
        pass
    def draw(self):
        self.image.clip_composite_draw(20, 310,150 , 30,0, '', 350, 550, 60, 50)

class Phone_option_subtitle:
    def __init__(self):
        self.image=load_image('Resource/Menu/Menu_option.png')
    def update(self):
        pass
    def draw(self):
        self.image.clip_composite_draw(20, 275, 50, 30,0, '', 350, 500, 60, 50)

class Phone_option_textSpeed:
    def __init__(self):
        self.image=load_image('Resource/Menu/Menu_option.png')
    def update(self):
        pass
    def draw(self):
        self.image.clip_composite_draw(20, 235, 125, 30,0, '', 350, 450, 60, 50)

class Phone_option_save_exit:
    def __init__(self):
        self.image=load_image('Resource/Menu/Menu_option.png')
    def update(self):
        pass
    def draw(self):
        self.image.clip_composite_draw(35, 25, 155, 30,0, '', 375, 225, 130, 50)