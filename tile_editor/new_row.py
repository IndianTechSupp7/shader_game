from tile_editor import Widget



class Row(Widget):
    def construct_widget(self, app, parent):
        super().construct_widget(app, parent)
        self.childs = self.args.get("childs") or []

    def _get_wh(self, index = None, arg="w"):
        if index is None: index = len(self.childs)
        width = sum([getattr(i, arg) for i in self.childs[:index]])
        return width

    def _get_max(self, arg="h"): # get the maximus widgets width from the childs
        height = max([getattr(i, arg) for i in self.childs])
        return height

    def update(self):
        super().update()


