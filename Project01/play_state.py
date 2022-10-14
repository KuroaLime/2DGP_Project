from pico2d import *
import game_framework
import title_state

import first_stage

# class Grass:
#     def __init__(self):
#         self.image = load_image('grass.png')
#
#     def draw(self):
#         self.image.draw(400, 30)

class kyoko:
    def __init__(self):
        self.x, self.y = 100, 90
        self.frame = 0
        self.last_frame=[12,    #idle
                         12,    #walk
                         16     #run
                         ]
        self.frame_turn=0   #0:idle 1:walk  2:run
        self.dir_lr= 0 #오른쪽 왼쪽
        self.dir_ud =0 # 위 아래
        self.dir_last =1 #오른쪽 왼쪽 전 상태
        self.image = load_image('Player_kyoko.png')

    def update(self):
        self.frame = (self.frame + 1) % self.last_frame[self.frame_turn]
        delay(0.05)
        self.x += self.dir_lr * 5
        self.y += self.dir_ud * 5
    
    def draw(self):

        if self.dir_lr > 0 and self.dir_ud == 0: # 오른쪽 이동
            self.image.clip_draw(self.frame * 40, 0, 40, 70, self.x, self.y)
        elif self.dir_lr < 0 and self.dir_ud == 0:    #왼쪽 이동
            self.image.clip_draw(self.frame * 40, 0, 40, 70, self.x, self.y)
        elif self.dir_lr == 0 and self.dir_ud == 0:   #idle
            if self.dir_last > 0:   #오른쪽을 보는 상태
                self.image.clip_draw(self.frame * 39, 415, 35, 69, self.x, self.y)
            else:               #왼쪽을 보는 상태
                self.image.clip_draw(self.frame * 39, 415, 35, 69, self.x, self.y)
        elif self.dir_ud > 0:    #위쪽 이동
            if self.dir_last == 1:
                self.image.clip_draw(self.frame * 40, 0, 40, 70, self.x, self.y)
            else:
                self.image.clip_draw(self.frame * 40, 0, 40, 70, self.x, self.y)
        elif self.dir_ud < 0:    #아래쪽 이동
            if self.dir_last == 1:
                self.image.clip_draw(self.frame * 40, 0, 40, 70, self.x, self.y)
            else:
                self.image.clip_draw(self.frame * 40, 0, 40, 70, self.x, self.y)



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
            elif event.key == SDLK_a: # 왼쪽 이동
                Player.dir_lr = -1
                frame_turn_changer()
            elif event.key == SDLK_d: # 오른쪽 이동
                Player.dir_lr = 1
                frame_turn_changer
            elif event.key == SDLK_w: # 위쪽 이동
                Player.dir_ud = 1
                frame_turn_changer
            elif event.key == SDLK_s: # 아래쪽 이동
                Player.dir_ud = -1
                frame_turn_changer
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_a or event.key == SDLK_d:
                Player.dir_last=Player.dir_lr
                Player.dir_lr = 0
                frame_turn_changer()
                Player.frame=0
            elif event.key == SDLK_w or event.key == SDLK_s:
                Player.dir_ud = 0
                Player.frame = 0
                frame_turn_changer()


def frame_turn_changer():
    if Player.dir_lr !=0 or Player.dir_ud !=0:
        if Player.frame_turn != 1:
            Player.frame_turn == 1
    elif Player.dir_lr==0 and Player.dir_ud==0:
        Player.frame_turn == 0


Player=None
background=None
running=None
player_count=0


def enter():
    global Player,background, running

    Player = kyoko()
    background=first_stage.first_stage()

    running = True

def exit():
    global Player,background
    del Player, background


def update():
    Player.update()

def draw():
    clear_canvas()
    draw_world()
    update_canvas()


def draw_world():
    background.draw()
    Player.draw()


def pause():
    pass

def resume():
    pass

# game main loop code
