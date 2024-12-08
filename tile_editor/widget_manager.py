import pygame
from utils import generate_dict_tree
from tile_editor.widget import Widget
from tile_editor.row import Row


class WidgetManager:
    def __init__(self, app, child):
        self.app = app
        self.child = child
        self.surf = pygame.Surface(self.app.size, pygame.SRCALPHA)

        self.construct_widgets()

    def render(self, surf):
        surf.blit(self.surf, (0, 0))

    def repr(self, f):
        return self._get_widgets(f)

    def construct_widgets(self):
        self._get_widgets(lambda widget, parent: widget.construct(self.app, parent))

    def update_widgets(self):
        self.surf.fill((0, 0, 0, 0))
        self._get_widgets(lambda widget, _: widget.update())

    def render_widgets(self):
        self._get_widgets(lambda widget, _: widget.render())

    def _get_childs(self, widget):
        if "childs" in vars(widget):
            if widget.childs: return widget.childs
        if "child" in vars(widget):
            if widget.child: return [widget.child]
        return []

    def _get_widgets(self, f):
        parent = self
        childs = [self.child]
        while childs != []:
            chs = childs.copy()
            childs = []
            for child in chs:
                f(child, parent)
                parent = child
                for ch in self._get_childs(child):
                    childs.append(ch)


if __name__ == '__main__':
    manager = WidgetManager(
        app=None,
        child=Row(
            childs=[
                Widget(size=(100, 100)),
                Widget(size=(100, 100))
            ]
        ),
    )
    manager.construct_widgets()
    manager.update_widgets()
    manager.repr(lambda x: print(x.x))
    print(manager)