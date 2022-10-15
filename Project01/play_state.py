from pico2d import *
import game_framework

#스테이트 임포트
import title_state
import first_stage

#적 임포트
import enermy_class

# class Grass:
#     def __init__(self):
#         self.image = load_image('grass.png')
#
#     def draw(self):
#         self.image.draw(400, 30)

class kyoko:
    def __init__(self):
        self.x, self.y = 500, 500
        self.frame = 0
        self.last_frame=[12,    #idle
                         12,    #walk
                         16     #run
                         ]
        self.frame_turn=0   #0:idle 1:walk  2:run
        self.dir_lr= 0 #오른쪽 왼쪽
        self.dir_ud =0 # 위 아래
        self.dir_last =1 #오른쪽 왼쪽 전 상태
        self.run_state=0
        self.image = load_image('Player_kyoko.png')
        self.image_L = load_image('Player_kyoko_L.png')
    def update(self):
        self.frame = (self.frame + 1) % self.last_frame[self.frame_turn]

        if self.run_state ==0:
            self.x += self.dir_lr * 5
            self.y += self.dir_ud * 5
        else:
            self.x += self.dir_lr * 10
            self.y += self.dir_ud * 10
    def run_dir_R(self):
        if self.run_state > 0:
            self.image.clip_draw(self.frame * 59, 134, 58, 70, self.x, self.y)
        else:
            self.image.clip_draw(self.frame * 40, 0, 40, 70, self.x, self.y)
    def run_dir_L(self):
        if self.run_state < 0:
            self.image_L.clip_draw(self.frame * 62, 136, 58, 70, self.x, self.y)
        else:
            self.image_L.clip_draw(self.frame * 45, 69, 41, 68, self.x, self.y)
    def draw(self):

        if self.dir_lr == 1 and self.dir_ud == 0: # 오른쪽 이동
            self.run_dir_R()
        elif self.dir_lr == -1 and self.dir_ud == 0:    #왼쪽 이동
            self.run_dir_L()
        elif self.dir_lr == 0 and self.dir_ud == 0:   #idle
            if self.dir_last == 1:   #오른쪽을 보는 상태
                self.image.clip_draw(self.frame * 39, 415, 39, 69, self.x, self.y)
            else:               #왼쪽을 보는 상태
                self.image_L.clip_draw(self.frame * 41, 0, 37, 69, self.x, self.y)
        elif self.dir_ud == 1:    #위쪽 이동
            if self.dir_last > 0:
                self.run_dir_R()
            else:
                self.run_dir_L()
        elif self.dir_ud == -1:    #아래쪽 이동
            if self.dir_last > 0:
                self.run_dir_R()
            else:
                self.run_dir_L()



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

    Player = kyoko()
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
    for i in range(0, len(Enermy)):
        Enermy[i].update()

def draw():
    clear_canvas()
    draw_world()
    update_canvas()


def draw_world():
    background.draw()
    Player.draw()
    for i in range(0,len(Enermy)):
        Enermy[i].draw()


def pause():
    pass

def resume():
    pass

# game main loop code
