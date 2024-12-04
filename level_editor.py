import pygame

from utils import Window
from level.tile_map import TileMap

class App(Window):
    def __init__(self):
        super().__init__()
        self.tile_map = TileMap(self, "test_level", tile_size=32)

        self.offset = [0, 0]
    
    
    def run(self):
        while True:
            self.events()
            self.display.fill((0, 0, 0))
            # movement
            if self.mouse["hold"][1]:
                self.offset[0] -= self.mouse["rel"][0]/2
                self.offset[1] -= self.mouse["rel"][1]/2
            if self.mouse["scroll_down"]:
                self.tile_map.tile_size = min(64, self.tile_map.tile_size+1)
            if self.mouse["scroll_up"]:
                self.tile_map.tile_size = max(10, self.tile_map.tile_size-1)
            # set_tiles
            if self.mouse["press"][0]:
                mouse_pos = (int(self.mouse['pos'][0] + self.offset[0])//self.tile_map.tile_size), int((self.mouse['pos'][1] + self.offset[1])//self.tile_map.tile_size)
                self.tile_map.tile_map["layer1"]["tiles"][f"{mouse_pos[0]};{mouse_pos[1]}"] = {"tile": "grass", "variant": 0, "pos": list(mouse_pos)}
                print(f"{mouse_pos[0]};{mouse_pos[1]}")
            if self.mouse["press"][2]:
                mouse_pos = (self.mouse['pos'][0] - self.offset[0]) // self.tile_map.tile_size, (
                            self.mouse['pos'][1] - self.offset[1]) // self.tile_map.tile_size
                if f"{mouse_pos[0]};{mouse_pos[1]}" in self.tile_map.tile_map["layer1"]["tiles"]:
                    self.tile_map.tile_map["layer1"]["tiles"].pop(f"{mouse_pos[0]};{mouse_pos[1]}")
            self.tile_map.render(self.display, self.offset)
            super().run()

class Tile:
    def __init__(self, pos, t, variant):
        self.pos = pos
        self.type = t
        self.variant = variant


if __name__ == '__main__':
    App().run()