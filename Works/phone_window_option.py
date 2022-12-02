from pico2d import *
import game_framework
import game_world
import server

# class Phone_option_instruction:
#     images = None
#
#     def __init__(self):
#         if Phone_option_instruction.images == None:
#             Phone_option_instruction.images=[load_image('Resource/Menu/Menu_option.png'),load_image('Resource/Menu/Menu_option.png')]
#     def update(self):
#         pass
#     def draw(self):
#         if Menu_button_location == 0:
#             Phone_option_instruction.images[1].composite_draw(0, '', 500, 850, 80, 60)
#         else:
#             Phone_option_instruction.images[0].composite_draw(0, '', 500, 850, 80, 60)

class Phone_option_music:
    images=None
    def __init__(self):
        if Phone_option_music.images == None:
            Phone_option_music.images = [load_image('Resource/Menu/icon/music(1).png'),
                                               load_image('Resource/Menu/icon/music(2).png')]
    def update(self):
        pass
    def draw(self):
        if server.Menu_button_location == 0:
            Phone_option_music.images[1].composite_draw(0, '', 350, 750, 60, 50)
        else:
            Phone_option_music.images[0].composite_draw(0, '', 350, 750, 60, 50)

class Phone_option_soundEffect:
    images = None
    def __init__(self):
        if Phone_option_soundEffect.images == None:
            Phone_option_soundEffect.images = [load_image('Resource/Menu/icon/sound_effect(1).png'),
                                         load_image('Resource/Menu/icon/sound_effect(2).png')]
    def update(self):
        pass
    def draw(self):
        if server.Menu_button_location == 1:
            Phone_option_soundEffect.images[1].composite_draw(0, '', 350, 700, 60, 50)
        else:
            Phone_option_soundEffect.images[0].composite_draw(0, '', 350, 700, 60, 50)

class Phone_option_voice:
    images = None
    def __init__(self):
        if Phone_option_voice.images == None:
            Phone_option_voice.images = [load_image('Resource/Menu/icon/voice(1).png'),
                                               load_image('Resource/Menu/icon/voice(2).png')]
    def update(self):
        pass
    def draw(self):
        if server.Menu_button_location == 2:
            Phone_option_voice.images[1].composite_draw(0, '', 350, 650, 60, 50)
        else:
            Phone_option_voice.images[0].composite_draw(0, '', 350, 650, 60, 50)

class Phone_option_save_exit:
    images = None
    def __init__(self):
        if Phone_option_save_exit.images == None:
            Phone_option_save_exit.images = [load_image('Resource/Menu/icon/save_and_exit(1).png'), load_image('Resource/Menu/icon/save_and_exit(2).png')]
    def update(self):
        pass
    def draw(self):
        if server.Menu_button_location == 3:
            Phone_option_save_exit.images[1].composite_draw(0, '', 375, 225, 130, 50)
        else:
            Phone_option_save_exit.images[0].composite_draw(0, '', 375, 225, 130, 50)