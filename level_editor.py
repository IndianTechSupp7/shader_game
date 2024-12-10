import pygame
from utils import Window
from level.tile_map import TileMap
from tile_editor.grid import Grid
from tile_editor import WidgetManager, Widget, Row, Btn, Padding, Column
from tile_editor.tile_editor_elements import NavBar


class App(Window):
    def __init__(self):
        super().__init__()
        # self.size = list(self.display.get_size())
        self.tile_map = TileMap(self, "test_level", tile_size=32)
        self.manager = WidgetManager(
            app=self,
            child=Row(
                childs=[
                    NavBar(),
                    Widget(
                        color = (0, 100, 100)
                    )
                ]

            )
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
