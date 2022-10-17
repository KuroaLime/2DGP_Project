from pico2d import *
import game_framework

# class Grass:
#     def __init__(self):
#         self.image = load_image('grass.png')
#
#     def draw(self):
#         self.image.draw(400, 30)

class kyoko:
    def __init__(self):
        self.x, self.y = 500, 500
        self.jump_progress_v, self.jump_g=15, 1
        self.jump_last_v= -15
        self.jump_y=self.y
        self.jump_turn=False
        self.frame = 0
        self.last_frame=[12,    #idle                           #점프는 따로 필요 없어서 추가 안함
                         12,    #walk
                         16,     #run
                         6,7,12,     # 첫 어택: 6,  두번째 어택: 7,      세번째 어택: 12
                         ]
        self.frame_turn=0   #0:idle 1:walk  2:run   3: 첫 어택 4:두번째 어택    5:세번째 어택
        self.dir_lr= 0 #오른쪽 왼쪽
        self.dir_ud =0 # 위 아래
        self.dir_last =1 #오른쪽 왼쪽 전 상태
        self.run_state=0 #Run 상태
        self.normal_attack_stack=0 #일반공격 콤보 스택 0:스냅 1:옆차기 2: 돌려차기
        self.normal_attack_time=0
        self.normal_attack_frame_state=0
        self.image = load_image('Player_kyoko.png')
        self.image_L = load_image('Player_kyoko_L.png')
        self.j_keyup=0
    def update(self):
        self.frame = (self.frame + 1) % self.last_frame[self.frame_turn]

        if self.dir_lr != 0 or self.dir_ud != 0:
            if self.run_state ==0:  #걷기와 달리기 속도 차이
                self.x += self.dir_lr * 5
                self.y += self.dir_ud * 5
            else:
                self.x += self.dir_lr * 10
                self.y += self.dir_ud * 10

        elif self.frame_turn <6 :   #노멀 어택 대기 시간
            if self.frame>=self.last_frame[self.frame_turn]-1 and self.normal_attack_frame_state == 1:
                self.normal_attack_frame_state = 0
            self.normal_attack_time += 0.1
            if self.normal_attack_time >=1.0:
                self.normal_attack_stack=0

        if self.jump_turn == True:
            self.y += self.jump_progress_v
            self.jump_progress_v = self.jump_progress_v - self.jump_g

            if self.jump_last_v-1 == self.jump_progress_v:
                self.jump_turn = False
                self.jump_progress_v=15
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

    def jump_dir_R(self):
        if self.jump_progress_v > 0:
            self.image.clip_draw(0 * 45, 346, 45, 69, self.x, self.y)
        else:
            self.image.clip_draw(1 * 45, 346, 45, 69, self.x, self.y)
    def jump_dir_L(self):
        if self.jump_progress_v > 0:
            self.image_L.clip_draw(0 * 50, 410, 50, 69, self.x, self.y)
        else:
            self.image_L.clip_draw(1 * 50, 410, 50, 69, self.x, self.y)
    def normal_attack_changer(self):
        if self.last_frame[self.frame_turn] - 1 == self.frame:
            self.frame = 0
            self.frame_turn = 0
            if self.j_keyup >= 1:
                self.j_keyup =0
                self.normal_attack_stack = self.normal_attack_stack + 1
                if self.normal_attack_stack >= 3:
                    self.normal_attack_stack = 0

    def frame_turn_changer(self):
        if self.jump_turn == False:
            if self.run_state != 0:
                if self.frame_turn != 2:
                    self.frame_turn == 2
            elif self.dir_lr != 0 or self.dir_ud != 0:
                if self.frame_turn != 1:
                    self.frame_turn == 1
            elif self.dir_lr == 0 and self.dir_ud == 0:
                self.frame_turn == 0
    def draw(self):
        if self.jump_turn == True:
            if self.jump_last_v>=self.jump_progress_v:
                if self.dir_last >0:
                    self.image.clip_draw(2 * 45, 346, 45, 69, self.x, self.y)
                else:
                    self.image_L.clip_draw(2 * 50, 410, 50, 69, self.x, self.y)
            elif self.dir_lr == 1 and self.dir_ud == 0: # 오른쪽 이동
                self.jump_dir_R()
            elif self.dir_lr == -1 and self.dir_ud == 0:    #왼쪽 이동
                self.jump_dir_L()
            elif self.dir_ud != 0:    #위쪽 이동
                if self.dir_last > 0:
                    self.jump_dir_R()
                else:
                    self.jump_dir_L()
            else:    #아래쪽 이동
                if self.dir_last > 0:
                    self.jump_dir_R()
                else:
                    self.jump_dir_L()
        elif self.frame_turn <= 2:    #캐릭터 이동 그리기
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
        elif self.frame_turn <=5:   #노멀 공격
            if self.normal_attack_stack <= 0:
                if self.dir_last > 0:
                    self.image.clip_draw(self.frame * 65, 484, 60, 67, self.x, self.y)
                else:
                    self.image_L.clip_draw(self.frame * 62, 210, 61, 65, self.x, self.y)
            elif self.normal_attack_stack <= 1:
                if self.dir_last > 0:
                    self.image.clip_draw(self.frame * 69, 549, 68, 69, self.x, self.y)
                else:
                    self.image_L.clip_draw(self.frame * 70, 275, 70, 66, self.x, self.y)
            elif self.normal_attack_stack <= 2:
                if self.dir_last > 0:
                    self.image.clip_draw(self.frame * 84, 620, 83, 72, self.x, self.y)
                else:
                    self.image_L.clip_draw(self.frame * 86, 341, 86, 69, self.x, self.y)
            self.normal_attack_changer()

