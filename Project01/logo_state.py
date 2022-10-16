import game_framework
from pico2d import *

import title_state
from canvas_size import *

running=True
logo_image=None
logo_time=0.0
logo_image_count=0

def enter():
    global logo_image
    logo_image=[load_image('Resource/logo/first_logo.png'),load_image('Resource/logo/second_logo.png'), load_image('Resource/logo/third_logo.png')]

    pass

def exit():
    global logo_image

    for i in range(0,len(logo_image)-1):
        del logo_image[i]

    pass

def update():
    global logo_time, logo_image_count

    #global running
    if logo_time>0.5:
        logo_time = 0
        if logo_image_count >= 2:
            logo_image_count=0
            game_framework.change_state(title_state)
        else:
            logo_image_count=logo_image_count+1
    delay(0.01)
    logo_time+=0.01

def draw():
    global logo_image_count

    clear_canvas()
    if logo_image_count <= len(logo_image)-1:
        logo_image[logo_image_count].draw(WID//2, HEI//2)
    update_canvas()
    pass

def handle_events():
    events = get_events()





