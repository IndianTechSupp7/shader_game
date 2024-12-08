
import pygame
from utils import Window
from level.tile_map import TileMap
from tile_editor.grid import Grid
from tile_editor import WidgetManager, Widget, Row

class App(Window):
    def __init__(self):
        super().__init__()
        #self.size = list(self.display.get_size())
        self.tile_map = TileMap(self, "test_level", tile_size=32)
        self.manager = WidgetManager(
            app=self,
            child=Row(childs=[
                Widget(size=(100, 50), color=(100, 0, 0)),
                Widget(size=(100, 200), color=(0, 100, 0)),
            ],
            color = (0, 0, 100),
            pos = (100, 100))
        )


    @Window.update
    def update(self):
        self.events()
        self.display.fill((0, 0, 0))
        self.manager.update_widgets()
        self.manager.render_widgets()

        self.manager.render(self.display)



if __name__ == '__main__':
    App().run()