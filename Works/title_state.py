from pico2d import *
from canvas_size import *

import game_framework
import game_world
import play_state
import logo_state
from stage import Stage

import Menu_state
#적 임포트
from cheerleader import Cheerleader
from school_boy import School_boy
from school_girl import School_girl
from cyborg import Cyborg
from police_man import Police_man

from Playable_Kyoko import Kyoko

from misuzu import Misuzu
from hibari import Hibari

from destructible_object import Vending_machine, Gold_statue
from item import Apple, Salad, Chicken
from portal import Portal, Portal2

from loading import Loading, Punch_loading
from hp_bar import Hp_bar, Character_face
import server
from Playable_Kyoko import Kyoko
image_background = None
image_component=None

component_x=None
component_y=None

my_button_x=None
my_button_y=None

my_button_dir=None
def enter():
    global image_background
    global image_component
    global component_x, component_y
    global my_button_x, my_button_y, my_button_dir

    hide_cursor()

    component_x = [485, 485, 485]
    component_y = [750, 400, 335]

    my_button_x = 350
    my_button_y = [390, 320]  # start = 390    end= 320

    my_button_dir = 0

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
def load_saved_world():
    count = 0
    game_world.load()
    for o in game_world.all_objects():
        print(count)
        if count >=10:
            break
        if isinstance(o, Kyoko):
            server.Player = o
            count += 1
            continue
        elif isinstance(o, Stage):
            server.stage = o
            count += 1
            continue
        # elif isinstance(o, Portal):
        #     server.portal[0] = o
        #     continue
        # elif isinstance(o,Portal2):
        #     server.portal[1] = o
        #     continue
        # elif isinstance(o,Misuzu):
        #     server.Boss = o
        #     continue
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
                    # load_saved_world()
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






