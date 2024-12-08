import pygame
from tile_editor.widget import Widget
class Row(Widget):
    def __init__(self, childs, **kwargs):
        super().__init__(**kwargs)
        self.childs = childs

        self._expanded = []
        self.expand_y = kwargs.get("expand_y") or False # expand the widgets along the yaxis based on self.pos[1]


    def construct(self, app, parent):
        super().construct(app, parent)
        self.set_size([self._get_width(self.childs, len(self.childs)), self._get_max("h")])
        self.surf = pygame.Surface(self.size, pygame.SRCALPHA)

    def _get_width(self, childs, k = None): # get the widgets whole width (sums up)
        if k == None: k = len(childs)
        width = sum([i.w for i in childs[:k]])
        return width

    def _get_max(self, arg="h"): # get the maximus widgets width from the childs
        height = max([getattr(i, arg) for i in self.childs])
        return height

    def _get_width_ratio(self, childs): # return a ratio (from 0 to 1) for each widget from childs
        max_width = self._get_width(childs,len(childs))
        width_ratio = [i.w/max_width for i in childs]
        remain = (1 - sum(width_ratio)) / len(width_ratio)
        width_ratio = [(i+remain) for i in width_ratio]
        return width_ratio

    def update(self):
        super().update()
        self.set_size(self.parent.size)
        self._expanded = [i for i in self.childs if i.expanded]
        if self._expanded:
            self._not_expaned = [i for i in self.childs if not i.expanded]
            for ratio, child in zip(self._get_width_ratio(self._expanded), self._expanded):
                child.set_size(((self.size[0] - self._get_width(self._not_expaned)) * ratio, self.size[1] if self.expand_y else child.h))

        for i, child in enumerate(self.childs):
            x = self._get_width(self.childs, i)
            y = 0
            child.set_pos((x, y))
            child.set_size((child.w, self.size[1] if self.expand_y else child.h))

    def render(self):
        super().render()
