from pico2d import *
import game_framework
import game_world
import canvas_size
import math
import time

PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

DASH_SPEED_KMPH = 30.0
DASH_SPEED_MPM = (DASH_SPEED_KMPH * 1000.0 / 60.0)
DASH_SPEED_MPS = (DASH_SPEED_MPM / 60.0)
DASH_SPEED_PPS = (DASH_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION_IDLE = 12
FRAMES_PER_ACTION_RUN = 12
FRAMES_PER_ACTION_NORMAL_ATTACK00 = 6
FRAMES_PER_ACTION_NORMAL_ATTACK01 = 7
FRAMES_PER_ACTION_NORMAL_ATTACK02 = 12
JUMP_VELOCITY = 10
PLAYER_WEIGHT = 2
GRAVITY =0.05

JUMP_SPEED_KMPH = 10.0
JUMP_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
JUMP_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
JUMP_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

RD,RU,LD,LU,UD,UU,DD,DU,DASHD,DASHU,ATKD,ATKU,JUMPD,JUMPU,ATK_END, TIMER=range(16)
event_name=['RD','RU','LD','LU','DASHD','DASHU','TIMER','JD','KD','JUMPD','JUMPU','ATK_END']

key_event_table = {
    (SDL_KEYDOWN, SDLK_d): RD,
    (SDL_KEYDOWN, SDLK_a): LD,
    (SDL_KEYDOWN, SDLK_w): UD,
    (SDL_KEYDOWN, SDLK_s): DD,
    (SDL_KEYDOWN, SDLK_TAB): DASHD,
    (SDL_KEYDOWN, SDLK_k): JUMPD,
    (SDL_KEYDOWN, SDLK_j): ATKD,

    (SDL_KEYUP, SDLK_d): RU,
    (SDL_KEYUP, SDLK_a): LU,
    (SDL_KEYUP, SDLK_w): UU,
    (SDL_KEYUP, SDLK_s): DU,
    (SDL_KEYUP, SDLK_TAB): DASHU,
    # (SDL_KEYUP, SDLK_j): ATKU
}
class IDLE:
    @staticmethod
    def enter(self, event):
        print('ENTER IDLE')
        self.dir_lr = 0
        self.dir_ud = 0
        self.timer = 1000
        self.DashState = False
        self.dash_lr =0
        self.dash_ud =0
        self.last_attack_frame = 0
        self.frame = 0
        self.attacking = False
    @staticmethod
    def exit(self, event):
        print('EXIT IDLE')
    @staticmethod
    def do(self):
        self.frame = (self.frame + FRAMES_PER_ACTION_IDLE * ACTION_PER_TIME * game_framework.frame_time) % 12
        self.timer -= 1
        if self.timer == 0:
            self.attack_turn =0
            self.add_event(TIMER)
        if self.JumpState:
            self.JUMP()
            self.y += self.JumpHeight
            self.all_jumpHeight += self.JumpHeight

        if self.Jump_V<-1 * JUMP_VELOCITY:
            self.JumpState =False
            self.JumpHeight = 0.0
            self.Jump_V = JUMP_VELOCITY
            self.all_jumpHeight = 0
    @staticmethod
    def draw(self):
        if self.JumpState:
            if self.face_dir == 1:
                self.image.clip_composite_draw(0 * 45, 346, 45, 69,0,'', self.x, self.y,140,200)
            else:
                self.image.clip_composite_draw(1 * 45, 346, 45, 69,0, 'h', self.x, self.y,140,200)

        else:
            if self.face_dir == 1:
                self.image.clip_composite_draw(int(self.frame) * 39, 415, 39, 69, 0, '', self.x, self.y,140,200)
            else:
                self.image.clip_composite_draw(int(self.frame) * 39, 415, 39, 69, 0, 'h', self.x, self.y,140,200)



class RUN_lr:
    @staticmethod
    def enter(self, event):
        print('ENTER RUN_lr')
        if event == RD:
            self.dir_lr += 1
        elif event == LD:
            self.dir_lr -= 1
        elif event == RU:
            self.dir_lr -= 1
        elif event == LU:
            self.dir_lr += 1

    @staticmethod
    def exit(self, event):
        print('EXIT RUN_lr')
        self.face_dir = self.dir_lr
    @staticmethod
    def do(self):
        self.frame = (self.frame + FRAMES_PER_ACTION_RUN * ACTION_PER_TIME * game_framework.frame_time) % 12
        if self.DashState:
            self.x += self.dir_lr * (DASH_SPEED_PPS) * game_framework.frame_time
        else:
            self.x += self.dir_lr * (RUN_SPEED_PPS) * game_framework.frame_time
        self.x = clamp(0, self.x, canvas_size.WID)

        if self.JumpState:
            self.JUMP()
            self.y += self.JumpHeight
            self.all_jumpHeight += self.JumpHeight
        if self.Jump_V<-1 * JUMP_VELOCITY:
            self.JumpState =False
            self.JumpHeight = 0.0
            self.Jump_V = JUMP_VELOCITY
            self.all_jumpHeight = 0
        if self.DashState:
            self.Dash()



    @staticmethod
    def draw(self):
        if self.JumpState:
            if self.face_dir == 1:
                self.image.clip_composite_draw(0 * 45, 346, 45, 69,0,'', self.x, self.y,140,200)
            else:
                self.image.clip_composite_draw(1 * 45, 346, 45, 69,0, 'h', self.x, self.y,140,200)

        else:
            if self.dir_lr == 1:
                self.image.clip_composite_draw(int(self.frame) * 59, 134, 58, 70,0,'', self.x, self.y,140,200)
            else:
                self.image.clip_composite_draw(int(self.frame) * 59, 134, 58, 70,0,'h', self.x, self.y,140,200)
class RUN_ud:
    @staticmethod
    def enter(self, event):
        print('ENTER RUN_ud')
        if event == UD:
            self.dir_ud = 1
        elif event == DD:
            self.dir_ud = -1
        elif event == UU:
            self.dir_ud -= 1
        elif event == DU:
            self.dir_ud += 1
    @staticmethod
    def exit(self, event):
        print('EXIT RUN_ud')
    @staticmethod
    def do(self):
        self.frame = (self.frame + FRAMES_PER_ACTION_RUN * ACTION_PER_TIME * game_framework.frame_time) % 12
        if self.DashState:
            self.y += self.dir_ud * DASH_SPEED_PPS * game_framework.frame_time
        else:
            self.y += self.dir_ud  * RUN_SPEED_PPS * game_framework.frame_time
        self.y = clamp(0, self.y, canvas_size.HEI)
        if self.JumpState:
            self.JUMP()
            self.y += self.JumpHeight
            self.all_jumpHeight += self.JumpHeight
        if self.Jump_V<-1 * JUMP_VELOCITY:
            self.JumpState =False
            self.JumpHeight = 0.0
            self.Jump_V = JUMP_VELOCITY
            self.all_jumpHeight = 0
    @staticmethod
    def draw(self):
        if self.JumpState:
            if self.face_dir == 1:
                self.image.clip_composite_draw(0 * 45, 346, 45, 69,0,'', self.x, self.y,140,200)
            else:
                self.image.clip_composite_draw(1 * 45, 346, 45, 69,0, 'h', self.x, self.y,140,200)

        else:
            if self.face_dir == 1:
                self.image.clip_composite_draw(int(self.frame) * 59, 134, 58, 70,0,'', self.x, self.y,140,200)
            else:
                self.image.clip_composite_draw(int(self.frame) * 59, 134, 58, 70,0,'h', self.x, self.y,140,200)

class RUN_diag: #대각선 이동
    @staticmethod
    def enter(self, event):
        print('ENTER RUN_diag')
        if event == RD:
            self.dir_lr += 1
        elif event == LD:
            self.dir_lr -= 1
        elif event == RU:
            self.dir_lr -= 1
        elif event == LU:
            self.dir_lr += 1
        if event == UD:
            self.dir_ud = 1
        elif event == DD:
            self.dir_ud = -1
        elif event == UU:
            self.dir_ud -= 1
        elif event == DU:
            self.dir_ud += 1
    @staticmethod
    def exit(self, event):
        print('EXIT RUN_diag')
        self.face_dir = self.dir_lr
        if event == UU or event == DU:
            self.dir_ud = 0
        if event == RU or event ==LU:
            self.dir_lr = 0
    @staticmethod
    def do(self):
        self.frame = (self.frame + FRAMES_PER_ACTION_RUN * ACTION_PER_TIME * game_framework.frame_time) % 12
        if self.DashState:
            self.x += self.dir_lr * (DASH_SPEED_PPS) * game_framework.frame_time
            self.y += self.dir_ud * (DASH_SPEED_PPS) * game_framework.frame_time
        else:
            self.x += self.dir_lr * RUN_SPEED_PPS * game_framework.frame_time
            self.y += self.dir_ud * RUN_SPEED_PPS * game_framework.frame_time
        self.y = clamp(0, self.y, canvas_size.HEI)
        self.x = clamp(0, self.x, canvas_size.WID)

        if self.JumpState:
            self.JUMP()
            self.y += self.JumpHeight
            self.all_jumpHeight += self.JumpHeight
        if self.Jump_V<-1 * JUMP_VELOCITY:
            self.JumpState =False
            self.JumpHeight = 0.0
            self.Jump_V = JUMP_VELOCITY
            self.all_jumpHeight = 0
            self.all_jumpHeight += self.JumpHeight
    @staticmethod
    def draw(self):
        if self.JumpState:
            if self.face_dir == 1:
                self.image.clip_composite_draw(0 * 45, 346, 45, 69,0,'', self.x, self.y,140,200)
            else:
                self.image.clip_composite_draw(1 * 45, 346, 45, 69,0, 'h', self.x, self.y,140,200)

        else:
            if self.dir_lr == 1:
                self.image.clip_composite_draw(int(self.frame) * 59, 134, 58, 70, 0, '', self.x, self.y, 140, 200)
            else:
                self.image.clip_composite_draw(int(self.frame) * 59, 134, 58, 70, 0, 'h', self.x, self.y, 140, 200)
class SLEEP:
    @staticmethod
    def enter(self, event):
        print('ENTER SLEEP')
        self.dir = 0  # 정지 상태

    @staticmethod
    def exit(self, event):
        print('EXIT SLEEP')

    @staticmethod
    def do(self):
        self.frame = (self.frame + FRAMES_PER_ACTION_IDLE * ACTION_PER_TIME * game_framework.frame_time) % 12

    @staticmethod
    def draw(self):
        if self.face_dir == 1:
            self.image.clip_composite_draw(int(self.frame) * 39, 415, 39, 69, 0, '', self.x, self.y, 140, 200)
        else:
            self.image.clip_composite_draw(int(self.frame) * 39, 415, 39, 69, 0, 'h', self.x, self.y, 140, 200)

class Normal_attack:
    @staticmethod
    def enter(self, event):
        print('ENTER Normal_attack')
        if self.attacking == False:
            self.frame = 0
            self.attacking = True
    @staticmethod
    def exit(self, event):
        print('EXIT Normal_attack')
    @staticmethod
    def do(self):
        if self.attacking == True:
            print('attack_turn : ', self.attack_turn)
            if self.attack_turn == 0:
                self.frame = (self.frame + FRAMES_PER_ACTION_NORMAL_ATTACK00 * ACTION_PER_TIME * game_framework.frame_time) % 6
            elif self.attack_turn == 1:
                self.frame = (self.frame + FRAMES_PER_ACTION_NORMAL_ATTACK01 * ACTION_PER_TIME * game_framework.frame_time) % 7
            elif self.attack_turn == 2:
                self.frame = (self.frame + FRAMES_PER_ACTION_NORMAL_ATTACK02 * ACTION_PER_TIME * game_framework.frame_time) % 12

            print('frame : ', self.frame, 'last_attack_frame : ',self.last_attack_frame)
            if self.frame < self.last_attack_frame:
                self.attack_turn += 1
                if self.attack_turn == 3:
                    self.attack_turn = 0
                self.attacking =False
                self.Complete_ATK()
            self.last_attack_frame = self.frame
        else:
            self.frame = (self.frame + FRAMES_PER_ACTION_IDLE * ACTION_PER_TIME * game_framework.frame_time) % 12
    @staticmethod
    def draw(self):
        if self.attacking == True:
            if self.attack_turn == 0:
                if self.face_dir == 1:
                    self.image.clip_composite_draw(int(self.frame) * 65, 484, 60, 67, 0, '', self.x, self.y, 180, 200)
                else:
                    self.image.clip_composite_draw(int(self.frame) * 65, 484, 60, 67, 0, 'h', self.x, self.y, 180, 200)
            elif self.attack_turn == 1:
                if self.face_dir == 1:
                    self.image.clip_composite_draw(int(self.frame) * 69, 549, 68, 69, 0, '', self.x, self.y, 180, 200)
                else:
                    self.image.clip_composite_draw(int(self.frame) * 69, 549, 68, 69, 0, 'h', self.x, self.y, 180, 200)
            elif self.attack_turn == 2:
                if self.face_dir == 1:
                    self.image.clip_composite_draw(int(self.frame) * 84, 620, 83, 72, 0, '', self.x, self.y, 180, 200)
                else:
                    self.image.clip_composite_draw(int(self.frame) * 84, 620, 83, 72, 0, 'h', self.x, self.y, 180, 200)
        else:
            if self.face_dir == 1:
                self.image.clip_composite_draw(int(self.frame) * 39, 415, 39, 69, 0, '', self.x, self.y, 140, 200)
            else:
                self.image.clip_composite_draw(int(self.frame) * 39, 415, 39, 69, 0, 'h', self.x, self.y, 140, 200)
next_state = {
    IDLE: {RU: IDLE, LU: IDLE, RD: RUN_lr, LD: RUN_lr, UU: IDLE, DU: IDLE, UD: RUN_ud, DD: RUN_ud,JUMPD: IDLE, TIMER: SLEEP,ATKD:Normal_attack,ATK_END:IDLE},
    RUN_lr: {RU: IDLE, LU: IDLE, RD: IDLE, LD: IDLE, UU: RUN_diag, DU: RUN_diag, UD: RUN_diag, DD: RUN_diag,JUMPD: RUN_lr,ATKD:Normal_attack,ATK_END:IDLE},
    RUN_ud: {RU: RUN_diag, LU: RUN_diag, RD: RUN_diag, LD: RUN_diag, UU: IDLE, DU: IDLE, UD: IDLE, DD: IDLE,JUMPD: RUN_ud,ATKD:Normal_attack,ATK_END:IDLE},
    RUN_diag: {RU: RUN_ud, LU: RUN_ud, RD: RUN_ud, LD: RUN_ud, UU: RUN_lr, DU: RUN_lr, UD: RUN_lr, DD: RUN_lr,JUMPD: RUN_diag,ATKD:Normal_attack,ATK_END:IDLE},
    Normal_attack: {RU: Normal_attack, LU: Normal_attack, RD: Normal_attack, LD: Normal_attack, UU: Normal_attack, DU: Normal_attack, UD: Normal_attack, DD: Normal_attack,JUMPD: Normal_attack,ATKD:Normal_attack,ATK_END:IDLE},
    SLEEP: {RU: RUN_lr, LU: RUN_lr, RD: RUN_lr, LD: RUN_lr, UU: RUN_ud, DU: RUN_ud, UD: RUN_ud, DD: RUN_ud, JUMPD: IDLE, TIMER: SLEEP,ATKD:Normal_attack,ATK_END:IDLE}
}
class Kyoko:
    image =None
    def __init__(self):
        self.x, self.y = 500, 500
        self.frame = 0
        # self.last_frame=[12,    #idle                           #점프는 따로 필요 없어서 추가 안함
        #                  12,    #walk
        #                  16,     #run
        #                  6,7,12,     # 첫 어택: 6,  두번째 어택: 7,      세번째 어택: 12
        #                  ]
        self.JumpHeight = 0.0
        self.Jump_V = JUMP_VELOCITY
        self.JumpState = False
        self.JumpTime = 0
        self.all_jumpHeight = 0

        self.DashState = False
        self.Dash_lr = 0
        self.Dash_ud = 0

        self.attack_turn=0
        self.attacking =False
        self.last_attack_frame=0

        self.dir_lr = 0 #오른쪽 왼쪽
        self.dir_ud = 0 # 위 아래
        self.face_dir = 1 #오른쪽 왼쪽 전 상태
        self.dash_state = 0 #Dash 상태
        if Kyoko.image == None:
            Kyoko.image = load_image('Character/Player_kyoko.png')
        self.event_que = []
        self.cur_state = IDLE
        self.cur_state.enter(self, None)
        self.event_test = None

        self.item = [0, 0, 0]
    def update(self):
        self.cur_state.do(self)

        if self.event_que:
            event = self.event_que.pop()
            self.event_test = event
            if event == JUMPD and self.JumpState == False:
                self.Jump_state()
            elif event == DASHD and self.JumpState == False:
                self.Dash_state()
            self.cur_state.exit(self, event)
            try:
                self.cur_state = next_state[self.cur_state][event]
            except KeyError:
                print('ERROR: ', self.cur_state, event_name[event])
            self.cur_state.enter(self, event)
        if self.JumpState:
            self.JUMP()
    def draw(self):
        self.cur_state.draw(self)
        draw_rectangle(*self.get_bb())
        draw_rectangle(*self.get_TT())
        debug_print('PPPP')
        debug_print(f'Face Dir: {self.face_dir}, Dir: {self.dir_lr}')
        # if self.jump_turn == True:
        #     if self.jump_last_v>=self.jump_progress_v:
        #         if self.dir_last >0:
        #             self.image.clip_draw(2 * 45, 346, 45, 69, self.x, self.y)
        #         else:
        #             self.image_L.clip_draw(2 * 50, 410, 50, 69, self.x, self.y)
        #     elif self.dir_lr == 1 and self.dir_ud == 0: # 오른쪽 이동
        #         self.jump_dir_R()
        #     elif self.dir_lr == -1 and self.dir_ud == 0:    #왼쪽 이동
        #         self.jump_dir_L()
        #     elif self.dir_ud != 0:    #위쪽 이동
        #         if self.dir_last > 0:
        #             self.jump_dir_R()
        #         else:
        #             self.jump_dir_L()
        #     else:    #아래쪽 이동
        #         if self.dir_last > 0:
        #             self.jump_dir_R()
        #         else:
        #             self.jump_dir_L()
        # elif self.frame_turn <= 2:    #캐릭터 이동 그리기
        #     if self.dir_lr == 1 and self.dir_ud == 0: # 오른쪽 이동
        #         self.run_dir_R()
        #     elif self.dir_lr == -1 and self.dir_ud == 0:    #왼쪽 이동
        #         self.run_dir_L()
        #     elif self.dir_lr == 0 and self.dir_ud == 0:   #idle
        #         if self.dir_last == 1:   #오른쪽을 보는 상태
        #             self.image.clip_draw(self.frame * 39, 415, 39, 69, self.x, self.y)
        #         else:               #왼쪽을 보는 상태
        #             self.image_L.clip_draw(self.frame * 41, 0, 37, 69, self.x, self.y)
        #     elif self.dir_ud == 1:    #위쪽 이동
        #         if self.dir_last > 0:
        #             self.run_dir_R()
        #         else:
        #             self.run_dir_L()
        #     elif self.dir_ud == -1:    #아래쪽 이동
        #         if self.dir_last > 0:
        #             self.run_dir_R()
        #         else:
        #             self.run_dir_L()
        # elif self.frame_turn <=5:   #노멀 공격
        #     if self.normal_attack_stack <= 0:
        #         if self.dir_last > 0:
        #             self.image.clip_draw(self.frame * 65, 484, 60, 67, self.x, self.y)
        #         else:
        #             self.image_L.clip_draw(self.frame * 62, 210, 61, 65, self.x, self.y)
        #     elif self.normal_attack_stack <= 1:
        #         if self.dir_last > 0:
        #             self.image.clip_draw(self.frame * 69, 549, 68, 69, self.x, self.y)
        #         else:
        #             self.image_L.clip_draw(self.frame * 70, 275, 70, 66, self.x, self.y)
        #     elif self.normal_attack_stack <= 2:
        #         if self.dir_last > 0:
        #             self.image.clip_draw(self.frame * 84, 620, 83, 72, self.x, self.y)
        #         else:
        #             self.image_L.clip_draw(self.frame * 86, 341, 86, 69, self.x, self.y)
        #     self.normal_attack_changer()

    def add_event(self, event):
        self.event_que.insert(0, event)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            # print('event_type : ',event.type,', event_key : ',event.key)
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

    def get_bb(self):   #적, 자판기등의 오브젝트와의 충돌범위
        return self.x - 45, self.y - 95, self.x + 45, self.y + 85
    def get_TT(self):   #스테이지와의 충돌
        return self.x - 45, (self.y-self.all_jumpHeight) - 95, self.x + 45, (self.y -self.all_jumpHeight) -80

    def handle_collision(self, other, group):
        if group == 'Player:Vending_machine':
            if self.event_test == ATKD:
                other.state = 1

    def JUMP(self):
            # if self.Jump_V > 0:
            #     self.JumpHeight = (0.5 * PLAYER_WEIGHT * (self.Jump_V * self.Jump_V))
            # else:
            #     self.JumpHeight = -(0.5 * PLAYER_WEIGHT * (self.Jump_V * self.Jump_V))
            # self.Jump_V -=GRAVITY*game_framework.frame_time
        self.JumpHeight = self.Jump_V * JUMP_SPEED_PPS*game_framework.frame_time
        self.Jump_V -= GRAVITY
    def Jump_state(self):

        if self.JumpState:
            self.JumpState = False
        else:
            self.JumpState = True

    def Dash(self):
        if self. dir_lr == 1:
            self.dash_lr +=1
        elif self.dir_lr == -1:
            self.dash_lr -= 1
        if self.dir_ud == 1:
            self.dash_ud +=1
        elif self.dir_ud == -1:
            self.dash_ud -= 1
    def Dash_state(self):

        if self.DashState:
            self.DashState = False
        else:
            self.DashState = True
    def Complete_ATK(self):
        self.add_event(ATK_END)