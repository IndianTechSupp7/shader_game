import pygame
from utils import clamp


class Widget:
    def __init__(self, **kwargs):
        self.id = id(self)

        self.child = kwargs.get("child") or None
        self.expanded = kwargs.get("expanded") or False # used in row or any other widget, that can expand it widgets to ist own size
        self.color = kwargs.get("color") or (0, 0, 0, 0) # color of the widget (test purposes)
        self.set_pos(kwargs.get("pos") or [0, 0]) # the position of the widget
        self.set_size(kwargs.get("size") or [0, 0]) # the size of the wiget (min size is 1)

        self.surf = pygame.Surface(self.size, pygame.SRCALPHA)

    def clear(self):
        self.surf.fill(self.color)

    def set_pos(self, pos): # set the pos of the widget
        self._pos = self._x, self._y = list(pos)

    @property
    def pos(self):
        return self._pos
    @property
    def x(self):
        return self._x
    @property
    def y(self):
        return self._y
    @property
    def size(self):
        return self._size
    @property
    def w(self):
        return self._w
    @property
    def h(self):
        return self._h



    def set_size(self, size): # set the size of the widget
        self._w = max(1, size[0])
        self._h = max(1, size[1])
        self._size = [self._w, self._h]
        self.surf = pygame.Surface(self.size, pygame.SRCALPHA)

    def construct(self, app, parent): # a constructor, its called on the WigetManager construct
        self.app = app
        self.parent = parent

    def update(self):
        self.clear()

    def render(self):
        self.parent.surf.blit(self.surf, self.pos)

