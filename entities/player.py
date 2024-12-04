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
                        image = assets.images["entities"]["player.png"],
                        )


        self._jump_buffer = False  # handle early jumps
        self.tile_size = self.game.tile_map.tile_size  # tile size of the current layer

        # a ray cast from the payler to the gorund, needed for early jumps
        self.platform_rays = {
            "bottom_left": Ray(self.game, self.game.tile_map.tile_map["layer1"]["tiles"], 1, tile_size=self.tile_size),
            "bottom": Ray(self.game, self.game.tile_map.tile_map["layer1"]["tiles"], 1, tile_size=self.tile_size),
            "bottom_right": Ray(self.game, self.game.tile_map.tile_map["layer1"]["tiles"], 1, tile_size=self.tile_size),
        }

        # the point where the platform ray hit the ground
        self.platform_points = {
            "bottom_left" : None,
            "bottom" : None,
            "bottom_right" : None,
        }

        self.jump_threshold = Timer(0.2)
        self._dx = 0
        self.speed = 1.6

    def jump(self):
        if self.collison_types["bottom"]:
            self.vel[1] = -3
        elif not self.collison_types["bottom"] and (self.platform_points["bottom_left"] or self.platform_points["bottom_right"]):
            self.vel[1] = -3.2
        else:
            if self.platform_points["bottom"]:
                self._jump_buffer = True


    
    def update(self, movement = [0, 0], layers = [], dt=1):
        self._dx = next(interpolate(self._dx, movement[0], 0.06))
        if self._dx > 0:
            a = bezier(0.244,  0.327,  0.4,  1.038, self._dx)[1]
            #print(a ,self._dx)
            super().update([a, movement[1]], layers)
        elif self._dx < 0:
            a = bezier(0.244, 0.327, 0.4, 1.038, abs(self._dx))[1]
            # print(a ,self._dx)
            super().update([-a, movement[1]], layers)
        else:
            super().update(movement, layers)
        self.platform_points["bottom_left"] = self.platform_rays["bottom_left"].update(list(self.rect().center), 140)
        self.platform_points["bottom"] = self.platform_rays["bottom"].update(list(self.rect().center), 90)
        self.platform_points["bottom_right"] = self.platform_rays["bottom_right"].update(list(self.rect().center), 40)


        if self._jump_buffer and self.collison_types["bottom"]:
            self.jump()
            self._jump_buffer = False

        # movement :
        #   accelerate : 0.98,  0.116,  0.664,  0.411,
        #   max_speed : linear
        #   decelerate : 0.951,  0.829,  -0.104,  0.958,
        if self.pos[1] > 710:
            self.pos[1] = -310



    def render(self, surf, offset):
        surf.blit(Sprite.render(self), [self.pos[0] - offset[0], self.pos[1] - offset[1]])
        # for point in self.platform_points:
        #     if self.platform_points[point]:
        #         pygame.draw.circle(surf, (0, 0, 255), [self.platform_points[point][0] * self.tile_size - offset[0], self.platform_points[point][1] * self.tile_size - offset[1]], 3)
