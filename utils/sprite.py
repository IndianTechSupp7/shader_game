import pygame
from utils.entity import Entity
from utils.shader import Shader, Texture
from utils.animation import Animation


class Sprite:
    def __init__(self, parent, **kwargs):
        self.parent: Entity = parent
        self.kwargs = kwargs
        self.animation = Animation(kwargs.get("animation")) if kwargs.get("animation") else None
        self.shaders = kwargs.get("shaders") or [] # [Shader(frag, vert)]

        self.surf = pygame.Surface(self.parent.size, pygame.SRCALPHA)
        self.surf.fill((255, 0, 0))

        for shader in self.shaders:
            shader.construct(self.surf)




    def render(self):
        if self.animation:
            self.surf = self.animation.render()

        for shader in self.shaders:
            shader.set_target_surface(self.surf)
            self.surf = shader.render()

        return self.surf
