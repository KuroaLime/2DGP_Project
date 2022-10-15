from pico2d import *
import game_framework

#스테이트 임포트
import title_state
import first_stage

#적 임포트
import enermy_class
import Plable_Kyoko
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
                if Player.frame_turn<=0:
                    if Player.normal_attack_stack == 0:
                        Player.frame=0
                        Player.frame_turn = 3
                    elif Player.normal_attack_stack ==1:
                        Player.frame = 0
                        Player.frame_turn =4
                    elif Player.normal_attack_stack ==2:
                        Player.frame = 0
                        Player.frame_turn =5
                    Player.normal_attack_time=0
                    #초기화
                    Player.dir_lr =0
                    Player.dir_ud=0
                    Player.run_state=0

            elif Player.frame_turn <=2:
                if event.key == SDLK_a: # 왼쪽 이동
                    Player.dir_lr = -1
                    if Player.dir_last!=Player.dir_lr:
                        Player.dir_last = Player.dir_lr
                    frame_turn_changer()
                elif event.key == SDLK_d: # 오른쪽 이동
                    Player.dir_lr = 1
                    if Player.dir_last!=Player.dir_lr:
                        Player.dir_last = Player.dir_lr
                    frame_turn_changer
                elif event.key == SDLK_w: # 위쪽 이동
                    Player.dir_ud = 1
                    if Player.dir_last!=Player.dir_lr:
                        Player.dir_last = Player.dir_lr
                    frame_turn_changer
                elif event.key == SDLK_s: # 아래쪽 이동
                    Player.dir_ud = -1
                    if Player.dir_last!=Player.dir_lr:
                        Player.dir_last = Player.dir_lr
                    frame_turn_changer
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

        elif event.type == SDL_KEYUP:
            if event.key == SDLK_a or event.key == SDLK_d:
                Player.dir_lr = 0
                frame_turn_changer()
                Player.frame=0
            elif event.key == SDLK_w or event.key == SDLK_s:
                Player.dir_ud = 0
                Player.frame = 0
                frame_turn_changer()
            elif event.key == SDLK_TAB:
                Player.run_state=0
            elif event.key == SDLK_j:
                Player.j_keyup=1



def frame_turn_changer():
    if Player.run_state !=0:
        if Player.frame_turn != 2:
            Player.frame_turn == 2
    elif Player.dir_lr !=0 or Player.dir_ud !=0:
        if Player.frame_turn != 1:
            Player.frame_turn == 1
    elif Player.dir_lr==0 and Player.dir_ud==0:
        Player.frame_turn == 0


Player=None
Enermy=None
background=None

running=None


def enter():
    global Player,Enermy
    global background, running

    hide_cursor()

    Player = Plable_Kyoko.kyoko()
    Enermy = [enermy_class.cheerleader()]

    background=first_stage.first_stage()

    running = True

def exit():
    global Player,Enermy
    global background
    del Player,background
    for i in range(0, len(Enermy)):
        del Enermy[i]


def update():
    Player.update()
    # for i in range(0, len(Enermy)):
    #     Enermy[i].update()

def draw():
    clear_canvas()
    draw_world()
    # draw_enermy()
    update_canvas()


def draw_world():
    background.draw()
    Player.draw()
def draw_enermy():
    for i in range(0,len(Enermy)):
        Enermy[i].draw()


def pause():
    pass

def resume():
    pass

# game main loop code
