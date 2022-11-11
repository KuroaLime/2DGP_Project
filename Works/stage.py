from pico2d import *
import game_framework
import canvas_size
# from camera import *
import play_state
import Playable_Kyoko
Stage_image = {0: (804,0,677,233)}
class First_Stage:
    def __init__(self,Stage_location):
        self.image = load_image('Resource/stage/stage01/first_stage_sheet.png')
        self.image = self.image.clip_image(Stage_image[Stage_location][0],Stage_image[Stage_location][1],Stage_image[Stage_location][2],Stage_image[Stage_location][3])
        self.WID, self.HEI = canvas_size.WID // 2 + 400, canvas_size.HEI // 2
    def update(self):
        if self.WID+(canvas_size.WID//2+401)>=canvas_size.WID and self.WID-(canvas_size.WID//2+401) <=10:
            if self.WID > 0 and self.WID < canvas_size.WID:
                if play_state.Player.dir_lr != 0:
                    self.WID -= play_state.Player.dir_lr * Playable_Kyoko.RUN_SPEED_PPS * game_framework.frame_time
            elif (self.WID -400)*2 >= canvas_size.WID:
                self.WID+=10
            else:
                self.WID -= 10
        elif(self.WID-400)*2<canvas_size.WID:
            self.WID+=1
        else:
            self.WID -= 1

        if self.HEI+(canvas_size.HEI//2)>=canvas_size.HEI and self.HEI-(canvas_size.HEI//2) <=10:
            if self.HEI > 0 and self.HEI < canvas_size.HEI:
                if play_state.Player.dir_ud != 0:
                    self.HEI -= play_state.Player.dir_ud * Playable_Kyoko.RUN_SPEED_PPS * game_framework.frame_time
            elif (self.HEI -400)*2 >= canvas_size.HEI:
                self.HEI+=10
            else:
                self.HEI -= 10
        elif self.HEI*2<canvas_size.HEI:
            self.HEI+=1
        else:
            self.HEI -= 1

    def draw(self):
        self.image.draw(self.WID,self.HEI,2970,990)
        draw_rectangle(*self.get_bb())
    def get_bb(self):
        return self.WID - 900, self.HEI - 420, self.WID + 900, self.HEI-90

    def handle_collision(self, other, group):
        left_a, bottom_a, right_a, top_a = other.get_TT()
        left_b, bottom_b, right_b, top_b = self.get_bb()

        if left_a < left_b:
            other.x += 1
        if right_a > right_b:
            other.x += -1
        if top_a > top_b:
            other.y += -1
        if bottom_a < bottom_b:
            other.y += 1
