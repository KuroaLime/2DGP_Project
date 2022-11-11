from pico2d import *
import game_framework
import play_state

PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 10.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION_IDLE = 12
FRAMES_PER_ACTION_RUN = 12

class Cheerleader:
    image=None
    def __init__(self):
        self.x, self.y, self.t= 0, 0,0.0
        self.sx,self.sy=self.x, self.y
        self.ax,self.ay = play_state.Player.x,play_state.Player.y
        self.frame = 0
        self.last_frame=[12,    #idle
                         12,    #walk
                         16     #run
                         ]
        self.frame_turn=0   #0:idle 1:walk
        self.dir_lr= 0 #오른쪽 왼쪽
        self.dir_ud =0 # 위 아래
        self.dir_last =1 #오른쪽 왼쪽 전 상태
        if Cheerleader.image == None:
            Cheerleader.image = load_image('Character/enermy_cheerleader.png')
        #self.image_L = load_image('Player_kyoko_L.png')

    def arrival_point_changer(self):
        if self.ax!=play_state.Player.x or self.ay!=play_state.Player.y:
            # if self.t >= 1.0:
            #     self.t = 0
            self.sx, self.sy = self.x, self.y
            self.ax, self.ay = play_state.Player.x, play_state.Player.y
    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION_RUN * ACTION_PER_TIME * game_framework.frame_time) % 12
        #self.t += 0.0005
        if self.x != self.ax:
            if self.x > self.ax:
                self.dir_lr= -1
            elif self.x < self.ax:
                self.dir_lr = 1
        if self.y != self.ay:
            if self.y > self.ay:
                self.dir_ud = -1
            elif self.y < self.ay:
                self.dir_ud = 1
        self.x+=self.dir_lr * RUN_SPEED_PPS * game_framework.frame_time
        self.y+=self.dir_ud * RUN_SPEED_PPS * game_framework.frame_time
        self.arrival_point_changer()

    def frame_turn_changer(self):
        if self.dir_lr != 0 or self.dir_ud != 0:
            if self.frame_turn != 1:
                self.frame_turn == 1
        elif self.dir_lr == 0 and self.dir_ud == 0:
            self.frame_turn == 0
    def draw(self):

        if self.dir_lr > 0 and self.dir_ud == 0: # 오른쪽 이동
            self.image.clip_composite_draw(int(self.frame) * 74, 0, 72, 73,0,'', self.x, self.y, 200,200)
        elif self.dir_lr < 0 and self.dir_ud == 0:    #왼쪽 이동
            self.image.clip_composite_draw(int(self.frame) * 74, 0, 72, 73,0,'h', self.x, self.y, 200,200)
        elif self.dir_lr == 0 and self.dir_ud == 0:   #idle
            if self.dir_last > 0:   #오른쪽을 보는 상태
                self.image.clip_composite_draw(int(self.frame) * 90, 273, 80, 72,0,'', self.x, self.y, 200,200)
            else:               #왼쪽을 보는 상태
                self.image.clip_composite_draw(int(self.frame) * 90, 273, 80, 72,0,'h', self.x, self.y, 200,200)
        elif self.dir_ud > 0:    #위쪽 이동
            if self.dir_last >0:
                self.image.clip_composite_draw(int(self.frame) * 74, 0, 72, 73,0,'', self.x, self.y, 200,200)
            else:
                self.image.clip_composite_draw(int(self.frame) * 74, 0, 72, 73,0,'h', self.x, self.y, 200,200)
        elif self.dir_ud < 0:    #아래쪽 이동
            if self.dir_last > 0:
                self.image.clip_composite_draw(int(self.frame) * 74, 0, 72, 73,0,'', self.x, self.y, 200,200)
            else:
                self.image.clip_composite_draw(int(self.frame) * 74, 0, 72, 73,0,'h', self.x, self.y, 200,200)


