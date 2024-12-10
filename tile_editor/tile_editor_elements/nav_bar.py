from tile_editor import *


class NavBar(BuildWidget):
    def build(self):
        return Widget(
            width = 150,
            child=Padding(
                padding=Padding.only(top=20),
                child=Column(
                childs=[
                    Padding(
                        padding=Padding.symetric(vertical=5, horizontal=10),
                        child=Widget(
                        height = 30,
                        color = (100, 0, 0)
                        )
                    ) for i in range(5)


                ]
            ))
        )