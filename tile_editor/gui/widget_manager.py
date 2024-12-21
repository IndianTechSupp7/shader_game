import pygame
from tile_editor.gui.widget import Widget
from tile_editor.row import Row


class WidgetManager:
    def __init__(self, app, child):
        self.app = app
        self.child = child
        self.surf = pygame.Surface(self.app.size, pygame.SRCALPHA)
        self.size = self.w, self.h = self.app.size
        self._last_size = self.size

        self.widgets = {}

        self.construct_widgets()

    def render(self, surf):
        surf.blit(self.surf, (0, 0))

    def repr(self, f):
        return self._get_widgets(f)

    def _init_widgets_wrapper(self, widget, parent, layer):
        print(widget)
        self.widgets[str(widget.id) + f"_{layer}"] = widget
        widget.construct_widget(self.app, parent)

    def construct_widgets(self):
        self._get_widgets(lambda widget, parent, layer: self._init_widgets_wrapper(widget, parent, layer))

    def update_widgets(self):
        self.size = self.w, self.h = self.app.size
        self.surf = pygame.Surface(self.size, pygame.SRCALPHA)
        if self._last_size != self.size:
            self.handle_widget_events()
            self._last_size = self.size
        self._get_widgets(lambda widget, *_,: widget.update())

    def render_widgets(self):
        for widget in sorted(self.widgets, key=lambda x: int(x.split("_")[-1]), reverse=True):
            self.widgets[widget].render()

    def handle_widget_events(self):
        for widget in sorted(self.widgets, key=lambda x: int(x.split("_")[-1]), reverse=True):
            for event in self.widgets[widget].events:
                event()

    def _get_childs(self, widget):
        # if "build" in dir(widget):
        #     return [widget.build()]
        if "childs" in vars(widget):
            if widget.childs: return widget.childs
        if "child" in vars(widget):
            if widget.child: return [widget.child]
        return []

    def _get_widgets(self, f):
        childs = [(self.child, self)] # widget, parent
        layer = 0
        while childs != []:
            layer+=1
            chs = childs.copy()
            childs = []
            for child, parent in chs:
                f(child, parent, layer)
                for ch in self._get_childs(child):
                    childs.append((ch, child))


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