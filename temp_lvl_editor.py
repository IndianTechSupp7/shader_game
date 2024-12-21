from utils import Window
from level.tile_map import TileMap
from utils import save_json
import pygame

class App(Window):
    def __init__(self):
        super().__init__()

        self.tile_map = TileMap(self, "test_level")


    @Window.update
    def update(self):
        self.events(press={
            pygame.K_s : lambda: self.tile_map.save_map("test_level")
        })
        self.display.fill((0, 0, 0))

        tile_mx = self.mouse["pos"][0] // self.tile_map.tile_size
        tile_my = self.mouse["pos"][1] // self.tile_map.tile_size

        if self.mouse["hold"][0]:
            tile_pos = f"{int(tile_mx)};{int(tile_my)}"
            if tile_pos not in self.tile_map.tile_map["layer1"]["tiles"]:
                self.tile_map.tile_map["layer1"]["tiles"][tile_pos] = {"tile": "grass", "variant": 0, "pos": [int(tile_mx), int(tile_my)]}

        if self.mouse["hold"][2]:
            tile_pos = f"{int(tile_mx)};{int(tile_my)}"
            if tile_pos in self.tile_map.tile_map["layer1"]["tiles"]:
                self.tile_map.tile_map["layer1"]["tiles"].pop(tile_pos)
                print(self.tile_map.tile_map["layer1"])

        self.tile_map.render(self.display)





if __name__ == '__main__':
    App().run()
