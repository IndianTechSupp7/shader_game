import pygame
import math
from utils.window import Window

OFFSETS = [(-1, -1), (0, -1), (1, -1), (-1, 0), (0, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]


class TileMap:
    BASE_PATH = "tile_maps/"
    def __init__(self, game, path, tile_size=16):
        self.game = game
        self.path = self.BASE_PATH + path + ".json"
        #self.tile_map = load_json(self.path) # {layer1 : {z = 0, tiles : {0;0 : {tile : grass, variant : 0, pos : (0, 0)}}}}
        self.tile_map = {
            "layer1" : {
                "z" : 0,
                "tiles":
                    {f"{i};10" : {"tile" : "grass", "variant" : 0, "pos" : (i, 10)} for i in range(30)} | {"0;9" : {"tile" : "grass", "variant" : 0, "pos" : (0, 9)}}
            }
        }


        self.tile_size = tile_size


    def get_collide_rects(self, pos, size, layer):
        offsets = []
        rects = []
        for w in range(math.ceil(size[0]/self.tile_size)):
            for h in range(math.ceil(size[1]/self.tile_size)):
                for x, y in OFFSETS:
                    offsets.append((w + x, h + y))
        offsets = set(offsets)
        for offset in offsets:
            tile_pos = (int(pos[0] // self.tile_size) + offset[0], int(pos[1] // self.tile_size) + offset[1])
            if f"{tile_pos[0]};{tile_pos[1]}" in self.tile_map[layer]["tiles"]:
                rects.append(pygame.Rect(tile_pos[0] * self.tile_size, tile_pos[1] * self.tile_size, self.tile_size, self.tile_size))
        return rects

    def _render_layer(self, layer, surf, offset = (0, 0)):

        for x in range(math.ceil(self.game.size[0] / self.tile_size)):
            for y in range(math.ceil(self.game.size[1] / self.tile_size)):
                coord = f"{x};{y}"
                # test purposes
                if coord in self.tile_map[layer]["tiles"]:
                    pos = self.tile_map[layer]["tiles"][coord]["pos"]
                    pygame.draw.rect(surf, (255, 255, 255), ((pos[0] * self.tile_size) - offset[0], (pos[1] * self.tile_size) - offset[1], self.tile_size, self.tile_size))

    def render(self, surf, offset = (0, 0)):
        for layer in sorted(self.tile_map, key=lambda x: self.tile_map[x]["z"]):
            self._render_layer(layer, surf, offset)

if __name__ == '__main__':
    tile_map = TileMap(None, "lvl1")
    tile_pos = tile_map.get_collide_rects([0, 0], [20, 20], "layer1")
    w = Window()
    offset = (100, 100)
    x, y = 0, 0
    while True:
        w.events()
        w.display.fill((0, 0, 0))

        keys = pygame.key.get_pressed()
        x += keys[pygame.K_d] - keys[pygame.K_a]
        y += keys[pygame.K_s] - keys[pygame.K_w]

        tile_pos = tile_map.get_collide_rects([x, y], [40, 20], "layer1")
        for t in tile_pos:
            pos = t.split(";")
            pygame.draw.rect(w.display, (255, 255, 255), (int(pos[0])*16, int(pos[1])*16, 16, 16), 1)
        pygame.draw.rect(w.display, (255, 255, 255), (x, y, 40, 20))

        w.run()