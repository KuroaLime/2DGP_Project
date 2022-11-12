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
from Playable_Kyoko import Kyoko
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
# def handle_events():
#     global running
#     global Player
#
#
#     events = get_events()
#     for event in events:
#         if event.type == SDL_QUIT:
#             game_framework.quit()
#         elif event.type == SDL_KEYDOWN:
#             if event.key == SDLK_SPACE: #메뉴창
#                 game_framework.quit()
#                 # game_framework.push_state(menu_state)
#
#             elif event.key == SDLK_j:
#                 #공격 상태
#                 if Player.frame_turn<=0 and Player.jump_turn == False and Player.normal_attack_frame_state == 0:
#                     if Player.normal_attack_stack == 0:
#                         Player.frame=0
#                         Player.frame_turn = 3
#                     elif Player.normal_attack_stack ==1:
#                         Player.frame = 0
#                         Player.frame_turn =4
#                     elif Player.normal_attack_stack ==2:
#                         Player.frame = 0
#                         Player.frame_turn =5
#                     Player.normal_attack_frame_state = 1
#                     Player.normal_attack_time=0
#                     #초기화
#                     Player.dir_lr =0
#                     Player.dir_ud=0
#                     Player.run_state=0
#
#             elif Player.frame_turn <=2 or Player.frame_turn >5:
#                 if event.key == SDLK_a: # 왼쪽 이동
#                     Player.dir_lr = -1
#                     if Player.dir_last!=Player.dir_lr:
#                         Player.dir_last = Player.dir_lr
#                     Player.frame_turn_changer()
#                 elif event.key == SDLK_d: # 오른쪽 이동
#                     Player.dir_lr = 1
#                     if Player.dir_last!=Player.dir_lr:
#                         Player.dir_last = Player.dir_lr
#                     Player.frame_turn_changer
#                 elif event.key == SDLK_w: # 위쪽 이동
#                     Player.dir_ud = 1
#                     if Player.dir_last!=Player.dir_lr:
#                         Player.dir_last = Player.dir_lr
#                     Player.frame_turn_changer
#                 elif event.key == SDLK_s: # 아래쪽 이동
#                     Player.dir_ud = -1
#                     if Player.dir_last!=Player.dir_lr:
#                         Player.dir_last = Player.dir_lr
#                     Player.frame_turn_changer
#                 elif event.key == SDLK_TAB:
#                     if Player.dir_lr == 1:
#                         Player.run_state = 1
#                     elif Player.dir_lr == -1:
#                         Player.run_state = -1
#                     elif Player.dir_ud == 1 or Player.dir_ud == -1:
#                         if Player.dir_last == 1:
#                             Player.run_state = 1
#                         elif Player.dir_last == -1:
#                             Player.run_state = -1
#                 elif event.key == SDLK_k: #jump key
#                     Player.jump_turn=True
#         elif event.type == SDL_KEYUP:
#             if event.key == SDLK_a or event.key == SDLK_d:
#                 Player.dir_lr = 0
#                 Player.frame_turn_changer()
#                 Player.frame=0
#             elif event.key == SDLK_w or event.key == SDLK_s:
#                 Player.dir_ud = 0
#                 Player.frame = 0
#                 Player.frame_turn_changer()
#             elif event.key == SDLK_TAB:
#                 Player.run_state=0
#             elif event.key == SDLK_j:
#                 Player.j_keyup=1


Player=None
Enermy=None
background=None

running=None

Default_deco_bar = None


def enter():
    global Player,Enermy
    global background, running
    global Default_deco_bar

    hide_cursor()

    Player = Kyoko()
    Enermy = [Cheerleader(),School_Boy()]
    background=First_Stage(0)
    Default_deco_bar= Black_bar()
    #0 -> 배경
    #1 -> 오브젝트
    #2 -> 플레이어 상태 표기
    #3 -> 플레이어
    game_world.add_object(Player, 3)
    for i in range(len(Enermy)):
        game_world.add_object(Enermy[i], 3)
    game_world.add_object(background, 0)
    game_world.add_object(Default_deco_bar, 2)
    # running = True
    game_world.add_collison_pairs(Player, background, 'Player:First_stage')

def exit():
    game_world.clear()


def update():
    for game_object in game_world.all_objects():
        game_object.update()
    for a, b, group in game_world.all_collision_pairs():

        if group == 'Player:First_stage':
            if stage_collide(a, b):
                print('COLLISON : ', group)
                a.handle_collision(b, group)
                b.handle_collision(a, group)
        else:
            if collide(a, b):
                print('COLLISON : ', group)
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
