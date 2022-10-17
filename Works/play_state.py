from pico2d import *
import game_framework

import Screen_default_deco

#스테이트 임포트
import title_state
import first_stage

#적 임포트
import enermy_class
import Playable_Kyoko
# class Grass:
#     def __init__(self):
#         self.image = load_image('grass.png')
#
#     def draw(self):
#         self.image.draw(400, 30)
def handle_events():
    global running
    global Player


    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_SPACE: #메뉴창
                game_framework.quit()
                # game_framework.push_state(menu_state)

            elif event.key == SDLK_j:
                #공격 상태
                if Player.frame_turn<=0 and Player.jump_turn == False and Player.normal_attack_frame_state == 0:
                    if Player.normal_attack_stack == 0:
                        Player.frame=0
                        Player.frame_turn = 3
                    elif Player.normal_attack_stack ==1:
                        Player.frame = 0
                        Player.frame_turn =4
                    elif Player.normal_attack_stack ==2:
                        Player.frame = 0
                        Player.frame_turn =5
                    Player.normal_attack_frame_state = 1
                    Player.normal_attack_time=0
                    #초기화
                    Player.dir_lr =0
                    Player.dir_ud=0
                    Player.run_state=0

            elif Player.frame_turn <=2 or Player.frame_turn >5:
                if event.key == SDLK_a: # 왼쪽 이동
                    Player.dir_lr = -1
                    if Player.dir_last!=Player.dir_lr:
                        Player.dir_last = Player.dir_lr
                    Player.frame_turn_changer()
                elif event.key == SDLK_d: # 오른쪽 이동
                    Player.dir_lr = 1
                    if Player.dir_last!=Player.dir_lr:
                        Player.dir_last = Player.dir_lr
                    Player.frame_turn_changer
                elif event.key == SDLK_w: # 위쪽 이동
                    Player.dir_ud = 1
                    if Player.dir_last!=Player.dir_lr:
                        Player.dir_last = Player.dir_lr
                    Player.frame_turn_changer
                elif event.key == SDLK_s: # 아래쪽 이동
                    Player.dir_ud = -1
                    if Player.dir_last!=Player.dir_lr:
                        Player.dir_last = Player.dir_lr
                    Player.frame_turn_changer
                elif event.key == SDLK_TAB:
                    if Player.dir_lr == 1:
                        Player.run_state = 1
                    elif Player.dir_lr == -1:
                        Player.run_state = -1
                    elif Player.dir_ud == 1 or Player.dir_ud == -1:
                        if Player.dir_last == 1:
                            Player.run_state = 1
                        elif Player.dir_last == -1:
                            Player.run_state = -1
                elif event.key == SDLK_k: #jump key
                    Player.jump_turn=True
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_a or event.key == SDLK_d:
                Player.dir_lr = 0
                Player.frame_turn_changer()
                Player.frame=0
            elif event.key == SDLK_w or event.key == SDLK_s:
                Player.dir_ud = 0
                Player.frame = 0
                Player.frame_turn_changer()
            elif event.key == SDLK_TAB:
                Player.run_state=0
            elif event.key == SDLK_j:
                Player.j_keyup=1


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

    Player = Playable_Kyoko.kyoko()
    Enermy = [enermy_class.cheerleader(),enermy_class.cheerleader()]

    background=first_stage.first_stage()

    Default_deco_bar= Screen_default_deco.black_bar()

    running = True

def exit():
    global Player,Enermy
    global background, Default_deco_bar

    del Player,background,Default_deco_bar
    for enermys in Enermy:
        del enermys


def update():
    Player.update()
    for enermys in Enermy:
        enermys.update()
    # for i in range(0, len(Enermy)):
    #     Enermy[i].update()

    delay(0.01)
def draw():
    clear_canvas()
    draw_world()
    update_canvas()


def draw_world():
    #스테이지 배경
    background.draw()

    #움직임 가능한 객체
    Player.draw()
    draw_enermy()

    #기본 데코
    Default_deco_bar.draw()
def draw_enermy():
    for enermys in Enermy:
        enermys.draw()


def pause():
    pass

def resume():
    pass

# game main loop code
