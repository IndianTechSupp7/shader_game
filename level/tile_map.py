import pygame
import math
from utils.window import Window
import random
from utils import load_json, save_json
from utils import Sprite, Assets, Shader
from utils.assest import MAIN_ROOT

OFFSETS = [(-1, -1), (0, -1), (1, -1), (-1, 0), (0, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
GRID_COLOR = (20, 20, 20)


class TileMap:
    BASE_PATH = "tile_maps/"
    def __init__(self, game, level, tile_size=16):
        self.game = game
        self.level = level
        self.assets = Assets()
        self.tile_map = self.load_map(self.assets.maps[level + ".json"])


        # self.colors = {c : (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for c in self.tile_map["layer1"]["tiles"]}

        self.tile_size = tile_size

        # self.sprite = Sprite(self,
        #                      shaders=[Shader(frag_path=Assets().shaders["tile"]["waving.glsl"])],
        #                      size=(self.tile_size, self.tile_size)
        #                      )

    def load_map(self, path):
        data = load_json(path)
        self.tile_map = data
        return data

    def save_map(self, path):
        save_json(self.tile_map, self.assets.maps_filter(path) + ".json")

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

    def _render_layer(self, layer, surf, offset = (0, 0), sh_grid = False):
        # self.sprite.update_renderer()
        for x in range(int(offset[0]//self.tile_size), math.ceil((self.game.size[0] + offset[0]) / self.tile_size)):
            for y in range(int(offset[1]//self.tile_size), math.ceil((self.game.size[1] + offset[1]) / self.tile_size)):
                coord = f"{x};{y}"
                # test purposes
                if sh_grid:
                    pygame.draw.rect(surf, GRID_COLOR, (
                    (x * self.tile_size) - offset[0], (y * self.tile_size) - offset[1], self.tile_size,
                    self.tile_size), 1)
                if coord in self.tile_map[layer]["tiles"]:
                    pos = self.tile_map[layer]["tiles"][coord]["pos"]
                    # self.sprite.shaders[0].clear((0, 0, 0, 1))
                    # self.sprite.surf.fill(self.colors[coord])

                    #self.sprite.shaders[0].send("offset", [(pos[0] * self.tile_size)/self.game.w, (pos[1] * self.tile_size)/self.game.h])
                    #print((pos[0] * self.tile_size)/self.game.w, (pos[1] * self.tile_size)/self.game.h)
                    #self.sprite.shaders[0].send("offset", pos[0]/3)
                    #self.sprite.shaders[0].clear((0, 0, 0, 1))
                    # surf.blit(self.sprite.render(update=False), ((pos[0] * self.tile_size) - offset[0], (pos[1] * self.tile_size) - offset[1], self.tile_size, self.tile_size))
                    # pygame.draw.rect(surf, self.colors[coord], ((pos[0] * self.tile_size) - offset[0], (pos[1] * self.tile_size) - offset[1], self.tile_size, self.tile_size))
                    pygame.draw.rect(surf, (255, 255, 255), ((pos[0] * self.tile_size) - offset[0], (pos[1] * self.tile_size) - offset[1], self.tile_size, self.tile_size))

    def render(self, surf, offset = (0, 0), sh_grid = False):
        for layer in sorted(self.tile_map, key=lambda x: self.tile_map[x]["z"]):
            self._render_layer(layer, surf, offset, sh_grid=sh_grid)

if __name__ == '__main__':
    tile_map = TileMap(None, "lvl1")