import pygame
from tile_editor.gui.widget import Widget

class Column(Widget):
    # a flag, if its used, and the child size didn't set, it will didnt update the size to its parent size in the update() method
    RESIZE = True
    def __init__(self, childs, **kwargs):
        super().__init__(**kwargs)
        self.childs = childs

        self._expanded = []

    def _expand_check(self):
        if self.expand_w:
            self.set_width(self.parent.w)
        else:
            self.set_width(self._get_max("w"))
        if self.expand_h:
            self.set_height(self.parent.h)
        else:
            self.set_height(self._get_height(self.childs))

    def construct_widget(self, app, parent):
        super().construct_widget(app, parent)
        self._expand_check()
        #self.surf = pygame.Surface(self.size, pygame.SRCALPHA)

    def _get_size_bef_init(self, childs):
        height = sum([i.h for i in childs])
        width = max([i.w for i in childs])
        if width and height:return width, height
        elif width: return width, self.parent.h
        elif height: return self.parent.w, height


    def _get_height(self, childs, k = None): # get the widgets whole width (sums up)
        if k == None: k = len(childs)
        height = sum([i.h for i in childs[:k]])
        return height

    def _get_max(self, arg="h"): # get the maximus widgets width from the childs
        height = max([getattr(i, arg) for i in self.childs])
        return height

    def _get_height_ratio(self, childs): # return a ratio (from 0 to 1) for each widget from childs
        max_height = self._get_height(childs,len(childs))
        height_ratio = [i.h/max_height for i in childs]
        remain = (1 - sum(height_ratio)) / len(height_ratio)
        height_ratio = [(i+remain) for i in height_ratio]
        return height_ratio

    def update(self):
        super().update()
        self._expand_check()

        self._expanded = [i for i in self.childs if i.expand_h]
        if self._expanded:
            self._not_expaned = [i for i in self.childs if not i.expand_h]
            for ratio, child in zip(self._get_height_ratio(self._expanded), self._expanded):
                child.set_size((self.w if child.expand_w else child.w, (self.h - self._get_height(self._not_expaned)) * ratio))

        for i, child in enumerate(self.childs):
            y = self._get_height(self.childs, i)
            x = 0
            child.set_pos((x, y))
            child.set_size((self.w if child.expand_w else child.w, child.h))

    def render(self):
        super().render()
