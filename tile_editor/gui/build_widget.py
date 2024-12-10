from tile_editor import Widget
import inspect

class BuildWidget(Widget):
    def construct_widget(self, app, parent):
        child = self.build()
        child.construct_widget(app, parent)
        super().__init__(**child.args)
        super().construct_widget(app, parent)
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        sig = inspect.signature(self.construct)
        params = {name: self.args[name] for name, _ in sig.parameters.items() if name in self.args}
        if params:self.construct(**params)
        else: self.construct()
    def construct(self):
        pass

    def build(self):
        raise "build must be implemented, and has to be return a Widget"
