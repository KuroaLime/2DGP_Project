from pico2d import *
from canvas_size import *

import game_framework
import play_state
import logo_state

image_background = None
image_component=None

component_x=[485,485,485]
component_y=[750,400,335]

my_button_x=350
my_button_y=[390,320] #start = 390    end= 320

my_button_dir=0
def enter():
    global image_background
    global image_component

    image_background=load_image('Resource/title/title.png')
    image_component=load_image('Resource/title/title_component.png')

def exit():
    global image_background, image_component
    global component_x, component_y
    global my_button_y, my_button_x

    del image_background
    del image_component
    del component_x, component_y
    del my_button_y, my_button_x

def handle_events():
    global my_button_dir

    events=get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:        #타이틀 스테이트 완성하면 없앱시다. 필요가 읎어요
                game_framework.change_state(logo_state)
            elif event.key == SDLK_s and my_button_dir == 0:
                my_button_dir =1
            elif event.key == SDLK_w and my_button_dir == 1:
                my_button_dir =0
            elif event.key == SDLK_j:
                if my_button_dir == 0:
                    game_framework.change_state(play_state)
                else:
                    game_framework.quit()

def draw():
    clear_canvas()
    image_background.draw(WID//2,HEI//2)
    image_component.clip_draw(110, 0, 649, 380, component_x[0], component_y[0]) #name logo
    image_component.clip_draw(830, 70, 193, 69, component_x[1], component_y[1]) # start 버튼
    image_component.clip_draw(830, 0, 193, 69, component_x[2], component_y[2])  # end 버튼

    image_component.clip_draw(749, 46, 81, 81, my_button_x, my_button_y[my_button_dir])  # 화살표
    update_canvas()

def update():
    pass

def pause():
    pass

def resume():
    pass






