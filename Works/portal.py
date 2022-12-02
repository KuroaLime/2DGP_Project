from pico2d import *
import game_framework
import server
import random
max_dead_enermy = [4,4,4,4,4,4,4,1]
portal_location_x = [[1920,1920,1920],[0,960,240]]
portal_location_y = [[700,700,700],[0,700,400]]
class Portal:
    def __init__(self):
        self.x, self.y = portal_location_x[0][server.stage_number], portal_location_y[0][server.stage_number]

    def update(self):
        if self.x != portal_location_x[0][server.stage_number] or self.y != portal_location_y[0][server.stage_number]:
            self.x = portal_location_x[0][server.stage_number]
            self.y = portal_location_y[0][server.stage_number]
    def draw(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        sx, sy = self.x - server.stage.window_left, self.y - server.stage.window_bottom
        return sx - 200, sy - 170, sx + 200, sy + 240

    def handle_collision(self, other, group):
        # print('Boy and Player collsion')
        left_a, bottom_a, right_a, top_a = other.get_bb()
        left_b, bottom_b, right_b, top_b = self.get_bb()
        # print('collision Portal!!!!!!')
        if server.stage.dead_enermy >= max_dead_enermy[server.stage_number]:
            other.portalState = True


class Portal2:
    def __init__(self):
        self.x, self.y = portal_location_x[1][server.stage_number], portal_location_y[1][server.stage_number]

    def update(self):
        if self.x != portal_location_x[1][server.stage_number] or self.y != portal_location_y[1][server.stage_number]:
            self.x = portal_location_x[1][server.stage_number]
            self.y = portal_location_y[1][server.stage_number]
    def draw(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        sx, sy = self.x - server.stage.window_left, self.y - server.stage.window_bottom
        return sx - 200, sy - 170, sx + 200, sy + 240

    def handle_collision(self, other, group):
        # print('Boy and Player collsion')
        left_a, bottom_a, right_a, top_a = other.get_bb()
        left_b, bottom_b, right_b, top_b = self.get_bb()
        # print('collision Portal!!!!!!')

        if server.stage.dead_enermy >= max_dead_enermy[server.stage_number]:
            other.portalState = True