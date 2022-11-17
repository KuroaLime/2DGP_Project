from pico2d import *
import game_framework
import game_world
from Screen_default_deco import Black_bar

#스테이트 임포트
import title_state
from stage import *

import Menu_state
#적 임포트
from cheerleader import Cheerleader
from school_boy import School_Boy
from school_girl import School_Girl
from Playable_Kyoko import Kyoko
from destructible_object import Vending_machine
from item import Apple, Salad, Chicken
from portal import Portal

# class Grass:
#     def __init__(self):
#         self.image = load_image('grass.png')
#
#     def draw(self):
#         self.image.draw(400, 30)
def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_F1):
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.push_state(Menu_state)
        else:
            Player.handle_event(event)

Player = None
Enermy = None
background = None

running = None

Default_deco_bar = None
vending_maching = None
item = None

portal = None
def enter():
    global Player,Enermy
    global background, running
    global Default_deco_bar,vending_maching, item
    global portal

    hide_cursor()

    Player = Kyoko()
    Enermy = [Cheerleader(), School_Boy(), School_Girl()]
    background = First_Stage(0)
    Default_deco_bar = Black_bar()
    vending_maching = Vending_machine()
    item = [Apple(),Salad(),Chicken()]

    portal = Portal()
    #0 -> 배경
    #1 -> 오브젝트
    #2 -> 플레이어 상태 표기
    #3 -> 플레이어
    game_world.add_object(Player, 3)
    for i in range(len(Enermy)):
        game_world.add_object(Enermy[i], 3)
    for i in range(len(item)):
        game_world.add_object(item[i],1)
    game_world.add_object(background, 0)
    game_world.add_object(Default_deco_bar, 2)
    game_world.add_object(vending_maching, 1)
    game_world.add_object(portal, 1)
    # running = True
    game_world.add_collison_pairs(Player, background, 'Player:First_stage')
    game_world.add_collison_pairs(Player, vending_maching, 'Player:Vending_machine')
    for i in range(len(Enermy)):
        game_world.add_collison_pairs(Player, Enermy[i], 'Player:Enermy')
        game_world.add_collison_pairs(Enermy[i], background, 'Enermy:First_stage')
    for i in range(len(item)):
        game_world.add_collison_pairs(Player, item[i], 'Player:Item')
    game_world.add_collison_pairs(Player, portal, 'Player:Portal')

def exit():
    game_world.clear()


def update():
    for game_object in game_world.all_objects():
        game_object.update()
    for a, b, group in game_world.all_collision_pairs():

        if group == 'Player:First_stage' or group == 'Enermy:First_stage':
            if stage_collide(a, b):
                # print('COLLISON : ', group)
                b.handle_collision(a, group)
        elif group == 'Player:Enermy':
            if moving_obj_collide(a, b):
                # print('COLLISON : ', group)
                b.handle_collision(a, group)
        else:
            if collide(a, b):
                # print('COLLISON : ', group)
                a.handle_collision(b, group)
                b.handle_collision(a, group)
def draw():
    clear_canvas()
    draw_world()
    update_canvas()


def draw_world():
    for game_object in game_world.all_objects():
        game_object.draw()

def collide(a,b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b : return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True
def moving_obj_collide(a,b):
    left_a, bottom_a, right_a, top_a = a.get_TT()
    left_b, bottom_b, right_b, top_b = b.get_TT()

    if left_a > right_b : return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True
def stage_collide(a,b):
    left_a, bottom_a, right_a, top_a = a.get_TT()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a < left_b: return True
    if right_a > right_b: return True
    if top_a > top_b: return True
    if bottom_a < bottom_b: return True

    return False
def pause():
    pass

def resume():
    pass

# game main loop code
