import math

import pygame.draw

from utils.entity import Entity
from utils.sprite import Sprite
from utils.shader import Shader, DEFAULT_VERTEX_SHADER
from utils.dda import Ray
from utils.timer import Timer

class Player(Entity, Sprite):
    def __init__(self, game):
        Entity.__init__(self, game, [100, 100], [10, 20])
        Sprite.__init__(self, self, shaders = [Shader(frag_path="shaders/player/spalsh.glsl")])

        self._jump_buffer = False  # handle early jumps
        self.tile_size = self.game.tile_map.tile_size  # tile size of the current layer

        self.platform_ray = Ray(self.game, self.game.tile_map.tile_map["layer1"], self.tile_size, tile_size=self.tile_size) #a ray cast from the payler to the gorund, needed for early jumps
        self.platform_point = None # the point where the platform ray hit the ground

        self.jump_threshold = Timer(0.2)

    def jump(self):
        if self.air_time < 5 or self.jump_threshold.get():
            if self.jump_threshold.get():
                self.jump_threshold.reset()
            self.vel[1] = -3
        else:
            if self.platform_point:
                self._jump_buffer = True

    
    def update(self, movement = [0, 0], layers = [], dt=1):
        super().update(movement, layers)
        self.platform_point = self.platform_ray.update(list(self.rect().center), 90)


        if self._jump_buffer and self.collison_types["bottom"]:
            self.jump()
            self._jump_buffer = False
        if self.air_time > 5 and not self.platform_point:
            self.jump_threshold.step(dt=dt)
            print(self.jump_threshold)
        else:
            self.jump_threshold.reset()

    def render(self, surf, offset):
        surf.blit(Sprite.render(self), [self.pos[0] - offset[0], self.pos[1] - offset[1]])
