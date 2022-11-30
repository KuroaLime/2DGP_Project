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
from school_boy import School_boy
from school_girl import School_girl
from cyborg import Cyborg
from police_man import Police_man

from Playable_Kyoko import Kyoko

from misuzu import Misuzu
from hibari import Hibari

from destructible_object import Vending_machine, Gold_statue
from item import Apple, Salad, Chicken
from portal import Portal

import server

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
            server.Player.handle_event(event)



def enter():

    hide_cursor()

    server.Player = Kyoko()
    server.Enermy = [Cheerleader(), School_boy(), School_girl(), Cyborg(), Police_man()]
    server.Boss = [Misuzu(),Hibari()]

    server.background = First_Stage(0)
    server.Default_deco_bar = Black_bar()
    server.Destructible_object = [Vending_machine(), Gold_statue()]
    server.item = [Apple(), Salad(), Chicken()]

    server.portal = Portal()

    #0 -> 배경
    #1 -> 오브젝트
    #2 -> 플레이어 상태 표기
    #3 -> 플레이어
    game_world.add_object(server.Player, 3)
    game_world.add_object(server.background, 0)
    game_world.add_object(server.portal, 1)
    game_world.add_object(server.Default_deco_bar, 2)
    for i in range(len(server.Enermy)):
        game_world.add_object(server.Enermy[i], 3)
    for i in range(len(server.Boss)):
        game_world.add_object(server.Boss[i], 3)
    for i in range(len(server.item)):
        game_world.add_object(server.item[i],1)
    for i in range(len(server.Destructible_object)):
        game_world.add_object(server.Destructible_object[i], 1)
        game_world.add_collison_pairs(server.Player, server.Destructible_object[i], 'Player:Destructible_object')

    game_world.add_collison_pairs(server.Player, server.background, 'Player:First_stage')
    for i in range(len(server.Enermy)):
        game_world.add_collison_pairs(server.Player, server.Enermy[i], 'Player:Enermy')
        game_world.add_collison_pairs(server.Enermy[i], server.background, 'Enermy:First_stage')
    for i in range(len(server.Boss)):
        game_world.add_collison_pairs(server.Player, server.Boss[i], 'Player:Boss')
        game_world.add_collison_pairs(server.Boss[i],server.background, 'Boss:First_stage')
    for i in range(len(server.item)):
        game_world.add_collison_pairs(server.Player, server.item[i], 'Player:Item')
    game_world.add_collison_pairs(server.Player, server.portal, 'Player:Portal')

def exit():
    game_world.clear()


def update():
    for game_object in game_world.all_objects():
        game_object.update()
    for a, b, group in game_world.all_collision_pairs():

        if group == 'Player:First_stage' or group == 'Enermy:First_stage' or group == 'Boss:First_stage':
            if stage_collide(a, b):
                # print('COLLISON : ', group)
                b.handle_collision(a, group)
        elif group == 'Player:Enermy' or group == 'Plyaer:Boss':
            if moving_obj_collide(a, b):
                # print('COLLISON : ', group)
                a.handle_collision(b,group)
                b.handle_collision(a, group)
        else:
            if collide(a, b):
                # print('COLLISON : ', group)
                a.handle_collision(b, group)
                b.handle_collision(a, group)

    # if Player.next_stage == True:
    #     for i in range(len(Enermy)):
    #         game_world.remove_object(Enermy[i])

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
