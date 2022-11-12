import game_framework
from pico2d import *

import title_state
import play_state
import random
image=None


def enter():
    global image
    image=load_image('Resource/Menu/Phone.png')

    pass

def exit():
    global image
    del image

    pass

def update():
    pass

def draw():
    clear_canvas()
    play_state.draw_world()
    image.clip_composite_draw(0, 0, 845, 1128, 0, 'h',500,550,700, 1000)
    update_canvas()
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            match event.key:
                case pico2d.SDLK_ESCAPE:
                    game_framework.pop_state()



