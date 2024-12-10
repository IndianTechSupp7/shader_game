from tile_editor import BuildWidget, Widget
from typing import override

class Btn(BuildWidget):
    def construct(self): ...



    def build(self):
        return Widget(
            size=(100, 100),
            color=(200, 200, 0),
            child=Widget(
                size=(50, 50),
                color=(100, 100, 100)
            )
        )
