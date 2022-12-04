from pico2d import *
import game_framework
import game_world
from Screen_default_deco import Black_bar

#스테이트 임포트
import title_state
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

import os.path
import pickle
# class Grass:
#     def __init__(self):
#         self.image = load_image('grass.png')
#
#     def draw(self):
#         self.image.draw(400, 30)

file='D:\\GIT\\2DGP_Project\\Works'
def new_world():
    server.Player = Kyoko()
    server.Enermy = [School_boy(), School_girl(), School_boy(), School_girl()]
    server.Boss = [Misuzu()]

    server.Player_hp_bar = [Hp_bar(), Character_face()]

    server.stage = Stage()
    server.Default_deco_bar = Black_bar()
    server.Destructible_object = [Vending_machine(), Gold_statue()]
    server.item = [Apple(), Salad(), Chicken()]

    server.portal = [Portal(), Portal2()]

    server.loading = [Loading(), Punch_loading()]
    # 0 -> 배경
    # 1 -> 오브젝트
    # 2 -> 플레이어 상태 표기
    # 3 -> 플레이어
    game_world.add_object(server.Player, 2)
    game_world.add_object(server.stage, 0)
    game_world.add_objects(server.portal, 1)
    game_world.add_object(server.Default_deco_bar, 4)
    game_world.add_objects(server.Enermy, 3)
    # game_world.add_objects(server.Boss, 3)

    # game_world.add_objects(server.item,1)

    game_world.add_objects(server.loading, 6)
    game_world.add_objects(server.Player_hp_bar, 5)

    game_world.add_collison_pairs(server.Player, server.stage, 'Player:stage')
    game_world.add_collison_pairs(server.Player, server.Enermy, 'Player:Enermy')
    game_world.add_collison_pairs(server.Enermy, server.stage, 'Enermy:stage')
    # game_world.add_collison_pairs(server.Player, server.Boss, 'Player:Boss')
    # game_world.add_collison_pairs(server.Boss,server.stage, 'Boss:stage')
    # game_world.add_collison_pairs(server.Player, server.item, 'Player:Item')
    game_world.add_collison_pairs(server.Player, server.portal, 'Player:Portal')
count = 0
def enter():
    hide_cursor()
    new_world()
    if os.path.isfile(file) == False:
        # new_world()
        game_world.save()
def exit():
    game_world.clear()
def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        # elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_F1):
        #     game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.push_state(Menu_state)
        else:
            server.Player.handle_event(event)
def update():
    for game_object in game_world.all_objects():
        game_object.update()
    for a, b, group in game_world.all_collision_pairs():

        if group == 'Player:stage' or group == 'Enermy:stage' or group == 'Boss:stage':
            if stage_collide(a, b):
                # print('COLLISON : ', group)
                b.handle_collision(a, group)
        elif group == 'Player:Portal':
            if portal_collide(a,b):
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
    add_enermy()
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
def portal_collide(a,b):
    left_a, bottom_a, right_a, top_a = a.get_TT()
    left_b, bottom_b, right_b, top_b = b.get_bb()
    if left_a > right_b : return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True
def add_enermy():
    if server.stage.next_stage == True:
        if server.stage.Timer >= 5.0:
            if server.stage_number < 2:
                server.Enermy = [School_boy(), School_girl(), School_boy(), School_girl()]
            elif server.stage_number < 3:
                server.Enermy = [School_girl(), School_girl(), School_girl(), School_girl(), School_girl()]
            elif server.stage_number < 4:
                server.Enermy = [School_girl(), School_girl(), School_boy(), School_boy(), Cheerleader(), Cheerleader(), Cheerleader()]
            elif server.stage_number < 6:
                server.Enermy = [Cheerleader(), School_boy(), School_girl(), Cyborg(), Police_man()]

            if server.stage_number == 6:
                game_world.add_objects(server.Boss, 3)
                game_world.add_collison_pairs(server.Player, server.Boss, 'Player:Boss')
                game_world.add_collison_pairs(server.Boss, server.stage, 'Boss:stage')
            else:
                game_world.add_objects(server.Enermy, 2)
                game_world.add_collison_pairs(server.Player, server.Enermy, 'Player:Enermy')
                game_world.add_collison_pairs(server.Enermy, server.stage, 'Enermy:stage')

            if server.stage_number == 1 or server.stage_number == 3 or server.stage_number == 5:
                server.Destructible_object = Vending_machine()
                game_world.add_object(server.Destructible_object, 1)
                game_world.add_collison_pairs(server.Player, server.Destructible_object, 'Player:Vending_machine')

                server.item = [Apple()]
                game_world.add_objects(server.item, 1)
                game_world.add_collison_pairs(server.Player, server.item, 'Player:Item')
            if server.stage_number == 2 or server.stage_number == 4:

                server.Destructible_object =Gold_statue()
                game_world.add_object(server.Destructible_object, 1)
                game_world.add_collison_pairs(server.Player, server.Destructible_object, 'Player:Gold_statue')

                server.item = [Salad(), Chicken()]
                game_world.add_objects(server.item, 1)
                game_world.add_collison_pairs(server.Player, server.item, 'Player:Item')

def pause():
    pass

def resume():
    pass

# game main loop code
