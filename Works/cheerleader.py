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

TIME_PER_ACTION = 1
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION_IDLE = 12
FRAMES_PER_ACTION_RUN = 12
FRAMES_PER_ACTION_ATK = 6
FRAMES_PER_ACTION_STUN = 3
FRAMES_PER_ACTION_DEAD = 24
animation_names = ['Idle', 'Run','Jab','Stun_one','Stun_two','Stun_three','Dead']
class Cheerleader:
    images = None
    Get_hit_sound =None
    def load_images(self):
        if Cheerleader.images == None:
            Cheerleader.images = {}
            for name in animation_names:
                if name == 'Jab':
                    Cheerleader.images[name] = [load_image(
                        "./Resource/classification/enermy/cheerleader/Occupied/" + name + " (%d)" % i + ".png") for i in
                        range(1, 7)]
                elif name == 'Stun_one' or name == 'Stun_two' or name == 'Stun_three':
                    Cheerleader.images[name] = [load_image(
                        "./Resource/classification/enermy/cheerleader/Occupied/" + name + " (%d)" % i + ".png") for i in
                        range(1, 4)]
                elif name == 'Dead':
                    Cheerleader.images[name] = [load_image(
                        "./Resource/classification/enermy/cheerleader/Occupied/" + name + " (%d)" % i + ".png") for i in
                        range(1, 25)]
                else:
                    Cheerleader.images[name] = [load_image(
                        "./Resource/classification/enermy/cheerleader/Occupied/" + name + " (%d)" % i + ".png") for i in
                                                range(1, 13)]

    def prepare_patrol_points(self):
        positions = [(random.randint(400, 1700), random.randint(33, 800)), (random.randint(400, 1700), random.randint(33, 800)),
                     (random.randint(400, 1700), random.randint(33, 800)), (random.randint(400, 1700), random.randint(33, 800)),
                     (random.randint(400, 1700), random.randint(33, 800)),(random.randint(400, 1700),random.randint(33, 800)),
                     (random.randint(400, 1700), random.randint(33, 800)), (random.randint(400, 1700),random.randint(33, 800))]
        self.patrol_points = []
        for p in positions:
            self.patrol_points.append((p[0], 1024-p[1]))
    def __init__(self):
        self.effect_Volume =32
        if Cheerleader.Get_hit_sound is None:
            Cheerleader.Get_hit_sound = load_wav('sound/Get_hit_enermy/gethit_knockdown_02.wav')
            Cheerleader.Get_hit_sound.set_volume(self.effect_Volume)
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
        self.wait_timer = 0.1
        self.atk_timer = 0.1
        self.load_images()
        self.build_behavior_tree()

        self.atk_state = False

        self.stun_timer =1.5
        self.stun_state = False

        self.dead_state = False
        self.dead_timer = 5
        self.collision_state = False
        self.dead = False

        self.hit_state = False
        #self.image_L = load_image('Player_kyoko_L.png')
    def __getstate__(self):
        state = {}
        return state
    def __setstate__(self, state):
        self.__init__()
        self.__dict__.update(state)
    def wander(self):
        if server.Player.attacking == False:
            if self.collision_state == True:
                self.collision_state = False
            self.speed = RUN_SPEED_PPS
            self.timer -= game_framework.frame_time
            if self.timer <= 0:
                self.timer = 2.0
                self.dir = random.random() * 2 * math.pi
                return BehaviorTree.SUCCESS
            else:
                return BehaviorTree.RUNNING
        else:
            return BehaviorTree.FAIL
    def wait(self):
        if server.Player.attacking == False:
            self.speed = 0
            if self.collision_state == True:
                self.collision_state = False
            self.wait_timer -= game_framework.frame_time
            if self.wait_timer <=0:
                self.wait_timer = 1.0
                return BehaviorTree.SUCCESS
            else:
                return BehaviorTree.RUNNING
        else:
            return BehaviorTree.FAIL

    def find_atk_player(self):
        distance2 = (server.Player.x - self.x) ** 2 + (server.Player.y - self.y) ** 2
        if server.Player.attacking == True:
            return BehaviorTree.FAIL
        elif distance2 <= (PIXEL_PER_METER * 2) ** 2:
            return BehaviorTree.SUCCESS
        else:
            self.speed = 0
            return BehaviorTree.FAIL
    def atk_player(self):
        self.speed = 0
        if server.Player.attacking == True:
            self.atk_state = False
            return BehaviorTree.FAIL
        else:
            self.atk_state = True
            self.atk_timer -= game_framework.frame_time
            if self.atk_timer <= 0:
                self.atk_timer = 1.0
                server.Player.hp -= 200
                self.atk_state = False
                Cheerleader.Get_hit_sound.play()
                return BehaviorTree.SUCCESS
            else:
                return BehaviorTree.RUNNING
    def find_player(self):
        distance2 = (server.Player.x - self.x)**2 + (server.Player.y - self.y)**2
        if distance2 <= (PIXEL_PER_METER*10)**2 and distance2 > (PIXEL_PER_METER*2)**2:
            return BehaviorTree.SUCCESS
        else:
            self.speed = 0
            return BehaviorTree.FAIL

    def move_to_player(self):
        self.speed = RUN_SPEED_PPS
        self.dir = math.atan2(server.Player.y - self.y, server.Player.x - self.x)
        return BehaviorTree.SUCCESS

    def stun(self):
        self.speed = 0

        if self.collision_state == True:
            if self.hit_state == True:
                print('stun state')
                self.stun_state = True
                self.dir = math.atan2(server.Player.y - self.y, server.Player.x - self.x)
                # self.stun_timer -= game_framework.frame_time
                if self.frame >= FRAMES_PER_ACTION_STUN- 1:
                    self.stun_timer = 2.0
                    self.stun_state = False
                    self.hit_state = False
                    self.frame =0
                    Cheerleader.Get_hit_sound.play()
                    return BehaviorTree.SUCCESS
                else:
                    return BehaviorTree.RUNNING
            else:
                return BehaviorTree.FAIL
        else:
            return BehaviorTree.FAIL
    def dead(self):
        self.speed = 0
        if self.hp <= 0:
            self.dead_state = True

            if self.frame >= FRAMES_PER_ACTION_DEAD- 1:
                self.dead_timer = 1.0
                self.dead = True
                self.frame = 0
                return BehaviorTree.SUCCESS
            else:
                return BehaviorTree.RUNNING
        else:
            return BehaviorTree.FAIL

    def build_behavior_tree(self):
        wander_node = LeafNode('Wander', self.wander)
        wait_node = LeafNode('Wait', self.wait)

        wander_wait_node = SequenceNode('WanderAndWait')
        wander_wait_node.add_children(wander_node, wait_node)

        find_atk_player_node = LeafNode('Find Player for atk', self.find_atk_player)
        atk_player_node = LeafNode('Atk Player', self.atk_player)
        stun_node = LeafNode('Stun Enermy', self.stun)
        dead_node = LeafNode('Dead Enermy', self.dead)
        atk_node = SequenceNode('Atk')
        atk_node.add_children(find_atk_player_node, atk_player_node)

        # get_next_position_node = LeafNode('Get Next Position', self.get_next_position())
        # move_to_target_node = LeafNode('Move to Target', self.move_to_target)
        # patrol_node = SequenceNode('Patrol')
        # patrol_node.add_children(get_next_position_node, move_to_target_node)

        find_player_node = LeafNode('Find Player', self.find_player)
        move_to_player_node = LeafNode('Move to Target', self.move_to_player)
        chase_node = SequenceNode('Chase')
        chase_node.add_children(find_player_node, move_to_player_node)

        chase_wander_node = SelectorNode('Chase or Wander')
        chase_wander_node.add_children(dead_node, stun_node, atk_node,chase_node, wander_wait_node)

        self.bt = BehaviorTree(chase_wander_node)

    def update(self):
        # if self.stage_numbers != server.stage.stage_number:
        #     self.hp = 200
        #     self.stage_numbers = server.stage.stage_number
        if self.effect_Volume != server.effect_volume:
            self.effect_Volume = server.effect_volume
            self.Get_hit_sound.set_volume(self.effect_Volume)
        if server.Player.attacking == True:
            self.hit_state = True
        if self.dead == True:
            server.stage.dead_enermy += 1
            game_world.remove_object(self)
        if server.stage.next_stage == True:
            game_world.remove_object(self)
        self.bt.run()

        if self.dead_state == True:
            self.frame = (self.frame + FRAMES_PER_ACTION_DEAD * (ACTION_PER_TIME-0.5) * game_framework.frame_time) % FRAMES_PER_ACTION_DEAD
        elif self.atk_state == True:
            self.frame = (self.frame + FRAMES_PER_ACTION_ATK * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION_ATK
        elif self.stun_state == True:
            self.frame = (self.frame + FRAMES_PER_ACTION_STUN * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION_STUN
        else:
            self.frame = (self.frame + FRAMES_PER_ACTION_RUN * ACTION_PER_TIME * game_framework.frame_time)%FRAMES_PER_ACTION_RUN
        self.x += self.speed * math.cos(self.dir) * game_framework.frame_time
        self.y += self.speed * math.sin(self.dir) * game_framework.frame_time
        self.y = clamp(restricted_area.Min_HEI[server.stage_number], self.y, server.stage.HEI - restricted_area.Max_HEI[server.stage_number])
        self.x = clamp(restricted_area.Min_WID[server.stage_number], self.x, server.stage.WID - restricted_area.Max_WID[server.stage_number])
    def draw(self):
        # draw_rectangle(*self.get_bb())
        # draw_rectangle(*self.get_TT())
        sy = self.y - server.stage.window_bottom
        sx = self.x - server.stage.window_left

        if self.stun_state == True:
            if server.Player.attack_turn == 0:
                if math.cos(self.dir) < 0:
                    Cheerleader.images['Stun_one'][int(self.frame)].composite_draw(0, 'h', sx, sy, 190, 200)
                else:
                    Cheerleader.images['Stun_one'][int(self.frame)].draw(sx, sy, 190, 200)
            elif server.Player.attack_turn == 1:
                if math.cos(self.dir) < 0:
                    Cheerleader.images['Stun_two'][int(self.frame)].composite_draw(0, 'h', sx, sy, 190, 200)
                else:
                    Cheerleader.images['Stun_two'][int(self.frame)].draw(sx, sy, 190, 200)
            elif server.Player.attack_turn == 2:
                if math.cos(self.dir) < 0:
                    Cheerleader.images['Stun_three'][int(self.frame)].composite_draw(0, 'h', sx, sy, 190, 200)
                else:
                    Cheerleader.images['Stun_three'][int(self.frame)].draw(sx, sy, 190, 200)
        elif self.dead_state == True:
            if math.cos(self.dir) < 0:
                Cheerleader.images['Dead'][int(self.frame)].composite_draw(0, 'h', sx, sy, 190, 200)
            else:
                Cheerleader.images['Dead'][int(self.frame)].draw(sx, sy, 190, 200)
        elif self.atk_state == True:
            if math.cos(self.dir) < 0:
                Cheerleader.images['Jab'][int(self.frame)].composite_draw(0, 'h', sx, sy, 190, 200)
            else:
                Cheerleader.images['Jab'][int(self.frame)].draw(sx, sy, 190, 200)
        else:
            if math.cos(self.dir) < 0:
                if self.speed == 0:
                    Cheerleader.images['Idle'][int(self.frame)].composite_draw(0, 'h', sx, sy, 190, 200)
                else:
                    Cheerleader.images['Run'][int(self.frame)].composite_draw(0, 'h', sx, sy, 190, 200)
            else:
                if self.speed == 0:
                    Cheerleader.images['Idle'][int(self.frame)].draw(sx, sy, 190, 200)
                else:
                    Cheerleader.images['Run'][int(self.frame)].draw(sx, sy, 190, 200)

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
        print('collision state : ', self.collision_state)
        self.collision_state = True
            # if left_a < left_b:
            #     self.x += 1
            # if right_a > right_b:
            #     self.x += -1
            # if top_a-165 > top_b-165:
            #     self.y += -1
            # if bottom_a < bottom_b:
            #     self.y += 1

