from pico2d import *
import game_framework
import play_state

class cheerleader:
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
        self.image = load_image('enermy_cheerleader.png')
        #self.image_L = load_image('Player_kyoko_L.png')

    def arrival_point_changer(self):
        if self.ax!=play_state.Player.x or self.ay!=play_state.Player.y:
            if self.t >= 1.0:
                self.t = 0
            self.sx, self.sy = self.x, self.y
            self.ax, self.ay = play_state.Player.x, play_state.Player.y
    def update(self):
        self.frame = (self.frame + 1) % self.last_frame[self.frame_turn]
        self.t += 0.0005
        self.x = (1-self.t)*self.sx+self.t*self.ax
        self.y = (1-self.t)*self.sy+self.t*self.ay
        self.arrival_point_changer()

    def frame_turn_changer(self):
        if self.dir_lr != 0 or self.dir_ud != 0:
            if self.frame_turn != 1:
                self.frame_turn == 1
        elif self.dir_lr == 0 and self.dir_ud == 0:
            self.frame_turn == 0
    def draw(self):

        if self.dir_lr > 0 and self.dir_ud == 0: # 오른쪽 이동
            self.image.clip_draw(self.frame * 74, 0, 72, 73, self.x, self.y)
        elif self.dir_lr < 0 and self.dir_ud == 0:    #왼쪽 이동
            self.image_L.clip_draw(self.frame * 74, 0, 72, 73, self.x, self.y)
        elif self.dir_lr == 0 and self.dir_ud == 0:   #idle
            if self.dir_last > 0:   #오른쪽을 보는 상태
                self.image.clip_draw(self.frame * 90, 273, 80, 72, self.x, self.y)
            else:               #왼쪽을 보는 상태
                self.image_L.clip_draw(self.frame * 90, 273, 80, 72, self.x, self.y)
        elif self.dir_ud > 0:    #위쪽 이동
            if self.dir_last >0:
                self.image.clip_draw(self.frame * 74, 0, 72, 73, self.x, self.y)
            else:
                self.image_L.clip_draw(self.frame * 74, 0, 72, 73, self.x, self.y)
        elif self.dir_ud < 0:    #아래쪽 이동
            if self.dir_last > 0:
                self.image.clip_draw(self.frame * 74, 0, 72, 73, self.x, self.y)
            else:
                self.image_L.clip_draw(self.frame * 74, 0, 72, 73, self.x, self.y)

