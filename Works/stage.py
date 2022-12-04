from pico2d import *
import game_framework
import canvas_size
# from camera import *
import server
import Playable_Kyoko
stage_max_enermy = [4,4,4,4,4,4,4,1]
stage_name = ['School']

FRAMES_PER_ACTION_NORMAL_ATTACK00 = 6
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION

class Stage:
    images =None
    def load_images(self):
        if Stage.images == None:
            Stage.images = {}
            for name in stage_name:
                Stage.images[name] = [load_image("./Resource/stage/"+ name + " (%d)" % i + ".png") for i in range(1, 8)]
    def __init__(self):
        self.stage_numbers= 0
        self.load_images()
        # self.stage_number = 0
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.WID = self.images['School'][server.stage_number].w
        self.HEI = self.images['School'][server.stage_number].h
        self.next_stage = False
        self.dead_enermy = 0
        self.Timer = 0
        self.loading = False
        self.Volume = 32
        self.bgm = load_music('sound/deafault_music.wav')
        self.bgm.set_volume(self.Volume)
        self.bgm.repeat_play()
        self.game_over = load_wav('sound/game_over/game_over_sound.wav')
        self.game_over.set_volume(self.Volume)
        self.stage_number = 0

    def __getstate__(self):
        state = {'dead_enermy':self.dead_enermy, 'stage_number':self.stage_number}
        return state
    def __setstate__(self, state):
        self.__init__()
        self.__dict__.update(state)

    def update(self):
        if self.Volume != server.music_volume:
            self.Volume = server.music_volume
            self.bgm.set_volume(self.Volume)
        if server.Player.dead_state == True:
            self.bgm.stop()
            self.game_over.play(1)

        self.window_left = clamp(0,
                                  int(server.Player.x)- self.canvas_width//2,
                                  self.WID - self.canvas_width - 1)

        self.window_bottom = clamp(0,
                                   int(server.Player.y) - self.canvas_height//2,
                                   self.HEI - self.canvas_height - 1)
        if self.next_stage == True:
            if self.Timer >= 5.0:
                self.next_stage = False
                server.Player.move_stage = False
                server.Player.portalTimer = 0
                self.dead_enermy = 0
                self.WID = self.images['School'][server.stage_number].w
                self.HEI = self.images['School'][server.stage_number].h
                self.Timer = 0
                if server.Player.stage_location < server.stage_number:
                    server.Player.x, server.Player.y = Playable_Kyoko.next_stage_location[server.stage_number]
                else:
                    server.Player.x, server.Player.y = Playable_Kyoko.behind_stage_location[server.stage_number]
                for i in range(2):
                    server.portal[i].work_portal = False
            elif self.Timer <=5:
                self.Timer += FRAMES_PER_ACTION_NORMAL_ATTACK00 * ACTION_PER_TIME * game_framework.frame_time
        # if self.WID+(canvas_size.WID//2+401)>=canvas_size.WID and self.WID-(canvas_size.WID//2+401) <=10:
        #     if self.WID > 0 and self.WID < canvas_size.WID:
        #         if server.Player.dir_lr != 0:
        #             self.WID -= server.Player.dir_lr * Playable_Kyoko.RUN_SPEED_PPS * game_framework.frame_time
        #     elif (self.WID -400)*2 >= canvas_size.WID:
        #         self.WID+=10
        #     else:
        #         self.WID -= 10
        # elif(self.WID-400)*2<canvas_size.WID:
        #     self.WID+=1
        # else:
        #     self.WID -= 1
        #
        # if self.HEI+(canvas_size.HEI//2)>=canvas_size.HEI and self.HEI-(canvas_size.HEI//2) <=10:
        #     if self.HEI > 0 and self.HEI < canvas_size.HEI:
        #         if server.Player.dir_ud != 0:
        #             self.HEI -= server.Player.dir_ud * Playable_Kyoko.RUN_SPEED_PPS * game_framework.frame_time
        #     elif (self.HEI -400)*2 >= canvas_size.HEI:
        #         self.HEI+=10
        #     else:
        #         self.HEI -= 10
        # elif self.HEI*2<canvas_size.HEI:
        #     self.HEI+=1
        # else:
        #     self.HEI -= 1

    def draw(self):
        Stage.images['School'][server.stage_number].clip_draw_to_origin(self.window_left, self.window_bottom,
                                       self.canvas_width, self.canvas_height,
                                       0, 0)


        # self.image.draw(self.WID,self.HEI,2970,990)
        # draw_rectangle(*self.get_bb())
    def get_bb(self):
        return self.WID - 900, self.HEI-100, self.WID + 900, self.HEI + 400

    def handle_collision(self, other, group):
        left_a, bottom_a, right_a, top_a = other.get_TT()
        left_b, bottom_b, right_b, top_b = self.get_bb()

        # if left_a < left_b:
        #     other.x += 1
        # if right_a > right_b:
        #     other.x += -1
        # if top_a > top_b:
        #     other.y += -1
        # if bottom_a < bottom_b:
        #     other.y += 1
