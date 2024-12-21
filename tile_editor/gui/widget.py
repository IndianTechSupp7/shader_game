import pygame
from utils import clamp



class Widget:
    def __init__(self, **kwargs):
        self.id = id(self)
        self.args = kwargs
        self._pos = self._x, self._y = (0, 0)
        self._size = self._w, self._h = (1, 1)

        self.events = [
            self.resize_event
        ]


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


    def set_width(self, width):
        self._w = max(1, width)
        self._size = (self._w, self._size[1])
        self.surf = pygame.Surface(self.size, pygame.SRCALPHA)

    def set_height(self, width):
        self._h = max(1, width)
        self._size = (self._size[0], self._h)
        self.surf = pygame.Surface(self.size, pygame.SRCALPHA)



    def set_size(self, size): # set the size of the widget
        self._w = max(1, size[0])
        self._h = max(1, size[1])
        self._size = [self._w, self._h]
        self.surf = pygame.Surface(self.size, pygame.SRCALPHA)

    def construct_widget(self, app, parent): # a constructor, its called on the WigetManager construct
        self.app = app
        self.parent = parent
        self.child = self.args.get("child") or None
        self.color = self.args.get("color") or (0, 0, 0, 0)  # color of the widget (test purposes)
        self.set_pos(self.args.get("pos") or [0, 0])  # the position of the widget
        self.set_size(self.args.get("size") or self.parent.size)  # the size of the wiget (min size is 1)
        self.set_width((self.args.get("width") or self.args.get("w")) or self.parent.w)
        self.set_height((self.args.get("height") or self.args.get("h")) or self.parent.h)
        self.get_expand()

        self.target_width = self.args.get("target_width") or self.parent.w
        self.target_height = self.args.get("target_height") or self.parent.h

        self.surf = pygame.Surface(self.size, pygame.SRCALPHA)


    def get_expand(self):
        size = self.args.get("size")
        if size:
            self.expand_w = False if size[0] else True
            self.expand_h = False if size[1] else True

        self.expand_w = not (self.args.get("width") or self.args.get("w"))
        self.expand_h = not (self.args.get("height") or self.args.get("h"))
        return self.expand_w, self.expand_h

    def resize_event(self):
        if self.expand_w:
            self.set_width(self.parent.w)
        if self.expand_h:
            self.set_height(self.parent.h)


    def update(self):
        self.clear()


    def render(self):
        self.parent.surf.blit(self.surf, (round(self.pos[0]), round(self.pos[1])))


