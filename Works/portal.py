from pico2d import *
import game_framework
import server
import random
max_dead_enermy = [4,4,4,4,4,4,4,1]
portal_location_x = [[1920,960,2500,2500,1920],[-50,1920,200,200]]
portal_location_y = [[700,700,400,400,700],[0,700,400,400,400]]
class Portal:
    def __init__(self):
        self.x, self.y = portal_location_x[0][server.stage_number], portal_location_y[0][server.stage_number]
        self.stage_location = server.stage_number
    def update(self):
        if self.x != portal_location_x[0][server.stage_number] or self.y != portal_location_y[0][server.stage_number]:
            self.x = portal_location_x[0][server.stage_number]
            self.y = portal_location_y[0][server.stage_number]
    def draw(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        sx, sy = self.x - server.stage.window_left, self.y - server.stage.window_bottom
        return sx - 190, sy - 170, sx + 190, sy + 240

    def handle_collision(self, other, group):
        # print('Boy and Player collsion')
        # left_a, bottom_a, right_a, top_a = other.get_bb()
        # left_b, bottom_b, right_b, top_b = self.get_bb()
        # print('collision Portal!!!!!!')]
        if server.stage.next_stage == True and server.stage_number == self.stage_location:
            server.stage_number += 1
            print('Portal1 : stage number : ', server.stage_number)
            self.stage_location, server.portal[1].stage_location = server.stage_number, server.stage_number

        if server.stage.dead_enermy >= max_dead_enermy[server.stage_number] and other.portalState == False:
            other.portalState = True



class Portal2:
    def __init__(self):
        self.x, self.y = portal_location_x[1][server.stage_number], portal_location_y[1][server.stage_number]
        self.stage_location = server.stage_number
    def update(self):
        if self.x != portal_location_x[1][server.stage_number] or self.y != portal_location_y[1][server.stage_number]:
            self.x = portal_location_x[1][server.stage_number]
            self.y = portal_location_y[1][server.stage_number]
    def draw(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        sx, sy = self.x - server.stage.window_left, self.y - server.stage.window_bottom
        return sx - 190, sy - 170, sx + 190, sy + 240

    def handle_collision(self, other, group):
        # print('Boy and Player collsion')
        # left_a, bottom_a, right_a, top_a = other.get_bb()
        # left_b, bottom_b, right_b, top_b = self.get_bb()
        # print('collision Portal!!!!!!')
        if server.stage.next_stage == True and server.stage_number == self.stage_location:
            server.stage_number -= 1
            print('Portal2 : stage number : ', server.stage_number)
            self.stage_location, server.portal[0].stage_location = server.stage_number, server.stage_number

        if server.stage.dead_enermy >= max_dead_enermy[server.stage_number] and other.portalState == False:
            other.portalState = True