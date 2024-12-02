from utils.entity import Entity
from utils.sprite import Sprite
from utils.shader import Shader, DEFAULT_VERTEX_SHADER

class Player(Entity, Sprite):
    def __init__(self, game):
        Entity.__init__(self, game, [100, 100], [10, 20])
        Sprite.__init__(self, self, shaders = [Shader(frag_path="shaders/player/spalsh.glsl")])

    def jump(self):
        self.vel[1] = -3



    def render(self, surf, offset):
        surf.blit(Sprite.render(self), [self.pos[0] - offset[0], self.pos[1] - offset[1]])