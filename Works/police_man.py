from pico2d import *
import game_framework
import server
import random
import game_world
from BehaviorTree import BehaviorTree, SelectorNode, SequenceNode, LeafNode
import restricted_area

PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 10.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION_IDLE = 12
FRAMES_PER_ACTION_RUN = 12

animation_names = ['Idle', 'Walk']
class Police_man:
    images=None
    def load_images(self):
        if Police_man.images == None:
            Police_man.images = {}
            for name in animation_names:
                Police_man.images[name] = [load_image("./Resource/classification/enermy/police_man/Occupied/"+ name + " (%d)" % i + ".png") for i in range(1, 13)]

    def prepare_patrol_points(self):
        positions = [(900, 850), (1118, 750), (1050, 530), (575, 220), (235, 33), (575,220), (1050, 530), (1118,750)]
        self.patrol_points = []
        for p in positions:
            self.patrol_points.append((p[0], 1024-p[1]))
    def __init__(self):
        self.prepare_patrol_points()
        self.patrol_order = 1
        self.hp = 20
        self.x, self.y= self.patrol_points[0]
        self.frame = 0
        # self.last_frame=[12,    #idle
        #                  12,    #walk
        #                  16     #run
        #                  ]
        self.dir = random.random()*2*math.pi
        self.speed = 0
        self.timer = 1.0
        self.wait_timer = 2.0
        self.load_images()
        self.build_behavior_tree()
        #self.image_L = load_image('Player_kyoko_L.png')

    def wander(self):
        self.speed = RUN_SPEED_PPS
        self.timer -= game_framework.frame_time
        if self.timer <= 0:
            self.timer = 1.0
            self.dir = random.random() * 2 * math.pi
            return BehaviorTree.SUCCESS
    def wait(self):
        self.speed = 0
        self.wait_timer -= game_framework.frame_time
        if self.wait_timer <=0:
            self.wait_timer = 2.0
            return BehaviorTree.SUCCESS
        else:
            return BehaviorTree.RUNNING

    def find_player(self):
        distance2 = (server.Player.x - self.x)**2 + (server.Player.y - self.y)**2
        if distance2 <= (PIXEL_PER_METER*10)**2:
            return BehaviorTree.SUCCESS
        else:
            self.speed = 0
            return BehaviorTree.FAIL

    def move_to_player(self):
        self.speed = RUN_SPEED_PPS
        self.dir = math.atan2(server.Player.y - self.y, server.Player.x - self.x)
        return BehaviorTree.SUCCESS

    def get_next_position(self):
        self.target_x, self.target_y = self.patrol_points[self.patrol_order % len(self.patrol_points)]
        self.patrol_order += 1
        self.dir = math.atan2(self.target_y - self.y, self.target_x - self.x)
        return BehaviorTree.SUCCESS

    def move_to_target(self):
        self.speed = RUN_SPEED_PPS
        distance2 = (server.Player.x - self.x)**2 + (server.Player.y - self.y)**2
        if distance2 <= PIXEL_PER_METER**2:
            return BehaviorTree.SUCCESS
        else:
            return BehaviorTree.RUNNING

    def build_behavior_tree(self):
        wander_node = LeafNode('Wander', self.wander)
        wait_node = LeafNode('Wait', self.wait)

        wander_wait_node = SequenceNode('WanderAndWait')
        wander_wait_node.add_children(wander_node, wait_node)

        get_next_position_node = LeafNode('Get Next Position', self.get_next_position())
        move_to_target_node = LeafNode('Move to Target', self.move_to_target)
        patrol_node = SequenceNode('Patrol')
        patrol_node.add_children(get_next_position_node, move_to_target_node)

        find_player_node = LeafNode('Find Player', self.find_player)
        move_to_player_node = LeafNode('Move to Target', self.move_to_player)
        chase_node = SequenceNode('Chase')
        chase_node.add_children(find_player_node, move_to_player_node)

        chase_wander_node = SelectorNode('Chase or Wander')
        chase_wander_node.add_children(chase_node, wander_node)

        self.bt = BehaviorTree(chase_wander_node)

    def update(self):
        # if self.stage_numbers != server.stage.stage_number:
        #     self.hp = 200
        #     self.stage_numbers = server.stage.stage_number
        if self.hp <= 0:
            server.stage.dead_enermy += 1
            game_world.remove_object(self)
        if server.stage.next_stage == True:
            game_world.remove_object(self)
        self.bt.run()

        self.frame = (self.frame + FRAMES_PER_ACTION_RUN * ACTION_PER_TIME * game_framework.frame_time)%FRAMES_PER_ACTION_RUN
        self.x += self.speed * math.cos(self.dir) * game_framework.frame_time
        self.y += self.speed * math.sin(self.dir) * game_framework.frame_time

        self.y = clamp(restricted_area.Min_HEI[server.stage.stage_number], self.y, server.stage.HEI - restricted_area.Max_HEI[server.stage.stage_number])
        self.x = clamp(restricted_area.Min_WID[server.stage.stage_number], self.x, server.stage.WID - restricted_area.Max_WID[server.stage.stage_number])
    def draw(self):
        draw_rectangle(*self.get_bb())
        draw_rectangle(*self.get_TT())
        sy = self.y - server.stage.window_bottom
        sx = self.x - server.stage.window_left
        if math.cos(self.dir) < 0:
            if self.speed == 0:
                Police_man.images['Idle'][int(self.frame)].composite_draw(0, 'h', sx, sy, 190, 200)
            else:
                Police_man.images['Walk'][int(self.frame)].composite_draw(0, 'h', sx, sy, 190, 200)
        else:
            if self.speed == 0:
                Police_man.images['Idle'][int(self.frame)].draw(sx, sy, 190, 200)
            else:
                Police_man.images['Walk'][int(self.frame)].draw(sx, sy, 190, 200)

    def get_bb(self):  # 적, 자판기등의 오브젝트와의 충돌범위
        sy = self.y - server.stage.window_bottom
        sx = self.x - server.stage.window_left
        return sx - 60, sy - 95, sx + 60, sy + 85

    def get_TT(self):  # 스테이지와의 충돌
        sy = self.y - server.stage.window_bottom
        sx = self.x - server.stage.window_left
        return sx - 60, sy - 95, sx + 60, sy - 80
    def handle_collision(self, other, group):
        left_a, bottom_a, right_a, top_a = other.get_bb()
        left_b, bottom_b, right_b, top_b = self.get_bb()
        # if left_a < left_b:
        #     self.x += 1
        # if right_a > right_b:
        #     self.x += -1
        # if top_a-165 > top_b-165:
        #     self.y += -1
        # if bottom_a < bottom_b:
        #     self.y += 1

