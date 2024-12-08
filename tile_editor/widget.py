import pygame
import time
class Widget:
    def __init__(self, child = None, pos = [0, 0], size = [0, 0], **kwargs):
        self.id = id(self)
        self.child = child
        self.set_pos(pos)
        self.set_size(size)

        self.color = kwargs.get("color") or (0, 0, 0)

        self.surf = pygame.Surface(self.size, pygame.SRCALPHA)

    def clear(self, r=100, g=0, b=0, a=255):
        self.surf.fill(self.color)

    def set_pos(self, pos):
        self.pos = self.x, self.y = list(pos)

    def set_size(self, size):
        self.size = self.w, self.h = size

    def __str__(self):
        return str(self.size)

    def construct(self, app, parent):
        self.app = app
        self.parent = parent

    def update(self):
        self.clear()

    def render(self):
        self.parent.surf.blit(self.surf, self.pos)

