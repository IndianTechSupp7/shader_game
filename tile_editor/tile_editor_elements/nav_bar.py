from tile_editor import *


class NavBar(BuildWidget):
    def build(self):
        return Widget(
            width = 200,
            color = (0, 0, 100),
            child=Column(
                childs=[

                    Widget(
                    height = 30,
                    color = (100, 0, 0)
                    ) for _ in range(10)
                ]
            )
        )