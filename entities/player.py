import math

import pygame.draw

from utils.entity import Entity
from utils.sprite import Sprite
from utils.shader import Shader, DEFAULT_VERTEX_SHADER
from utils.dda import Ray
from utils.timer import Timer
from utils import interpolate, bezier, Assets
from utils.assest import MAIN_ROOT


class Player(Entity, Sprite):
    def __init__(self, game):
        assets = Assets()
        Entity.__init__(self, game, [100, 100], [10, 20])
        Sprite.__init__(self, self,
                        shaders = [Shader(frag_path=assets.shaders["player"]["splash.glsl"])],
                        #image = assets.images["entities"]["player.png"],
                        )

        self.jump_input= {
            "press" : False,
            "hold" : False
        }
        self._jump_buffer = False  # handle early jumps
        self.tile_size = self.game.tile_map.tile_size  # tile size of the current layer

        # a ray cast from the payler to the gorund, needed for early jumps
        self.platform_ray = Ray(self.game, self.game.tile_map.tile_map["layer1"]["tiles"], 1, tile_size=self.tile_size)
        self.platform_point = None

        # tracks the last floor tile touched, needed for late jumps
        self.last_floor_tile = None
        self.jump_threshold = Timer(0.2)

        # wall jump
        self._track_collision = [False, False] # left, right
        self._wall_jump_velocity = 0.2

        self._dx = 0
        self.speed = 160

    def release_jump(self):
        self.jump_input["hold"] = False

    def jump(self):
        self.jump_input["hold"] = True
        self.jump_input["press"] = True

    def _jump(self):
        if self.collison_types["bottom"]:
            self.vel[1] = -3
        elif self.jump_threshold.in_cooldown():
            self.vel[1] = -3.2
        else:
            if self.platform_point:
                self._jump_buffer = True

    def update(self, movement = [0, 0], layers = [], dt=1):
        # ---------------- movement --------------------------
        # movement :
        #   accelerate : 0.98,  0.116,  0.664,  0.411,
        #   max_speed : linear
        #   decelerate : 0.951,  0.829,  -0.104,  0.958,
        self._dx = next(interpolate(self._dx, movement[0], 0.06))
        if self._dx > 0:
            a = bezier(0.244,  0.327,  0.4,  1.038, self._dx)[1]
            #print(a ,self._dx)
            super().update([a, movement[1]], layers, dt=dt)
        elif self._dx < 0:
            a = bezier(0.244, 0.327, 0.4, 1.038, abs(self._dx))[1]
            # print(a ,self._dx)
            super().update([-a, movement[1]], layers, dt=dt)
        else:
            super().update(movement, layers)

        self.platform_point = self.platform_ray.update(list(self.rect().center), 90)



        # ---------------- jump logic --------------------------
        if self.jump_input["press"]:
            self._jump()
            self.jump_input["press"] = False

        if self.jump_input["hold"] or self.collison_types["left"] or self.collison_types["right"]:
            self._wall_jump(movement)

        if self.collison_types["bottom"] is not None:
            self.jump_threshold.reset()
            self.last_floor_tile = self.collison_types["bottom"]
            self._track_collision = [False, False]


        if self._jump_buffer and self.collison_types["bottom"] is not None:
            self._jump()
            self._jump_buffer = False

        if self.last_floor_tile:
            if not self.collison_types["bottom"] and self.rect().bottom > self.last_floor_tile:
                self.jump_threshold.start()

        # ---------------- fallout --------------------------

        if self.pos[1] > 710:
            self.pos[1] = -310


    def _wall_jump(self, movement):
        # change the _track_collision collision logic !!!!!!
        if self.collison_types["left"] or self._track_collision[0]:
            self._track_collision[0] = True
            self.vel[1] = self._wall_jump_velocity
            if movement[0] > 0:
                self._dx = 0.7
                self.vel[1] = -3
                self._track_collision[0] = False

        if self.collison_types["right"] or self._track_collision[1]:
            self._track_collision[1] = True
            self.vel[1] = self._wall_jump_velocity
            if movement[0] < 0:
                self._dx = -0.7
                self.vel[1] = -3
                self._track_collision[1] = False





    def render(self, surf, offset):
        surf.blit(Sprite.render(self), [int(self.pos[0] - offset[0]), int(self.pos[1] - offset[1])])
        # for point in self.platform_points:
        #     if self.platform_points[point]:
        #         pygame.draw.circle(surf, (0, 0, 255), [self.platform_points[point][0] * self.tile_size - offset[0], self.platform_points[point][1] * self.tile_size - offset[1]], 3)
