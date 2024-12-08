import pygame
from tile_editor.widget import Widget
class Row(Widget):
    def __init__(self, childs, **kwargs):
        super().__init__(**kwargs)
        self.childs = childs

    def construct(self, app, parent):
        super().construct(app, parent)
        self.size = [self._get_width(len(self.childs)), self._get_height()]
        self.surf = pygame.Surface(self.size, pygame.SRCALPHA)

    def _get_width(self, i):
        width = sum([i.w for i in self.childs[:i]])
        return width

    def _get_height(self):
        height = max([i.h for i in self.childs])
        return height

    def update(self):
        super().update()
        self.size = [self._get_width(len(self.childs)), self._get_height()]
        for i, child in enumerate(self.childs):
            x = self._get_width(i)
            y = 0
            child.set_pos((x, y))

    def render(self):
        for c in self.childs:
            c.render()
        super().render()
